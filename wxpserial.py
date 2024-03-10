"""
  The MIT License (MIT)
 
  Copyright (C) 2024 Guilherme Bertoldo
  (UTFPR) Federal University of Technology - Parana

  Permission is hereby granted, free of charge, to any person obtaining a 
  copy of this software and associated documentation files (the “Software”), 
  to deal in the Software without restriction, including without limitation 
  the rights to use, copy, modify, merge, publish, distribute, sublicense, 
  and/or sell copies of the Software, and to permit persons to whom the Software 
  is furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all 
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""

    wxpserial simplifies the serial port communication in wxPython.

    The received data may be parsed using one of the message parser defined
    in this module or by an user-defined parser.

    To release the main application from the communication, this version of 
    the module uses Threads (threading library) or Processes (multiprocessing library).
    When threading is applied, the CPU time for the application is distributed between
    the threads. On the other hand, when multiprocessing is used, another instance of
    the application is created, allowing the use of multicore resources. In this way,
    multiprocessing is faster than threading, but consumes more memory. The user must
    choose the best option for his/her application. 
    
    Set the variable THREADS=True for threading and THREADS=False for multiprocessing.

    DO NOT FORGET to add the following code in the main application:
        if __name__ == '__main__':   
            wxpserial.init()

            
    Parsers
    -------
        The parser classes must have a 'parse' method that receives an input text,
        searches for messages and returns a list 'result' with two elements:
            result[0]: contains the remainder of the text that do not for a message (yet)
            result[1]: contains a list of messages

        There are two message parses in this module:
        - FSMessageParser:
            The messages are separated by a symbol (field separator FS)
        - BracketsMessageParser
            The messages are within brackets (for instance '<' '>')
        
"""

import wx
import os
import time
import serial
import serial.tools.list_ports


######################################################################################## 

"""
    The following code defines a common interface for threading 
    and multiprocessing libraries in the current module.
"""
THREADS=True # THREADS=True for threading and THREADS=False for multiprocessing

if THREADS: # Using threads
    import threading as wk
    from threading import Thread as Worker
    from queue import Queue as wkQueue

    def init():
        pass
    def workerId():
        return wk.current_thread().name
    def finish(worker: Worker):
        worker.join(0.001)

else: # Using multiprocessing
    import multiprocessing as wk
    from multiprocessing import Process as Worker
    from multiprocessing import Queue as wkQueue

    def init():
        wk.freeze_support()
        wk.set_start_method('spawn')
    def workerId():
        return os.getpid()
    def finish(worker: Worker):
        worker.terminate()


########################################################################################

"""

    Message parsers

"""

class FSMessageParser:
    """
    Message parser for PSerial that uses only one character as field separator FS. 
    
    Caution: the method 'parse' must return a list where the first element
    is the remainder of the input text and the second element is a list of
    messages. For instance, for the input text 'a&b&c' and the field 
    separator '&', the return must be ['c',['a','b']]. In this case, 'c' is
    not a new field because the input text may be incomplete.
    """
    def __init__(self, FS):
        self.FS = FS
    def parse(self, text):
        msglist = text.split(self.FS)
        return [msglist[-1],msglist[0:-1]]


class BracketsMessageParser:
    """
    Finds messages enclosed by brackets FSB and FSE  
    """
    def __init__(self, FSB, FSE):
      if FSB==FSE:
        raise(ValueError())
      self.FSB = FSB
      self.FSE = FSE
      return

    def parse(self, text):
      # Removing new line characters
      text = text.replace("\n","")
      text = text.replace("\r","")

      # Creating an empty message list
      msgList = []

      while True:
        # Separates the text in three parts: before the field separator, 
        # the field separator and after the field separator. Uses the end
        # field separator.
        beforeFS, fieldseparator, afterFS = text.partition(self.FSE) 
        
        # If the end field separator was found, may be the first part
        # of the text contains a message. Lets take a look...
        if fieldseparator:

          # Setting the new text to be parsed is the text after the field separator.
          text = afterFS

          try:
            # Search for the rightmost index of the begin field separator.
            # If no error occur, a message was found. Add it to the list.
            idxB = beforeFS.rindex(self.FSB)+1
            msgList.append(beforeFS[idxB:])
          except ValueError:
            pass  
        else:
          # If there is no field separator, just exit the loop
          break

      return [text,msgList]


########################################################################################

"""

    PSerial related classes

"""

class SerialParameters:
    """
        Parameters for initializing the serial object
    """
    def __init__(self
                , port
                , baudrate=9600
                , bytesize=8
                , parity=serial.PARITY_NONE
                , stopbits=serial.STOPBITS_ONE
                , timeout=0.05
                , xonxoff=False
                , rtscts=False
                , write_timeout=0.05
                , dsrdtr=False
                , inter_byte_timeout=None
                , exclusive=True
                , **kwargs):
        self.port               = port
        self.baudrate           = baudrate
        self.bytesize           = bytesize
        self.parity             = parity
        self.stopbits           = stopbits
        self.timeout            = timeout
        self.xonxoff            = xonxoff
        self.rtscts             = rtscts
        self.write_timeout      = write_timeout
        self.dsrdtr             = dsrdtr
        self.inter_byte_timeout = inter_byte_timeout
        self.exclusive          = exclusive
        self.kwargs             = kwargs


class PSerialComm:
    """
        PSerialComm is a data structure that contains
        the tools for secure communication between the producer
        class (PSerial) and the consumer class (the user of PSerial).
    """
    def __init__(self):
        self.qRXmsg = wkQueue() # Queue for received messages
        self.qRXraw = wkQueue() # Queue for raw input data
        self.qTXmsg = wkQueue() # Queue for transmited messages
        self.qerr   = wkQueue() # Queue for error reporting
        self.enableRXraw = wk.Event() # Event to enable/disable storing raw input data
        self.enableIO    = wk.Event() # Event to enable/disable IO operations
        self.isOpen      = wk.Event() # Event to signal if the connection is open=set or closed=clear

        # Default options
        self.enableRXraw.clear() # Do not transmit raw input
        self.enableIO.clear() # Read and write only after process starts
        self.isOpen.clear() # Connection was not openned yet

# Error codes
FAIL_TO_CREATE_SERIAL_OBJECT=1
FAIL_TO_OPEN_SERIAL_CONNECTION=2
FAIL_TO_READ_FROM_SERIAL=3
FAIL_TO_WRITE_TO_SERIAL=4
FAIL_TO_CLOSE_SERIAL_CONNECTION=5

class PSerial(Worker):
    """
        PSerial is a Worker (Thread or Process) dedicated
        to reading/wrinting a given serial port and to parse the input data.
        The parser is implemented externally to this class. The usage of the parser
        follows the Template design pattern.
    """
    def __init__(self, serPar: SerialParameters, psComm: PSerialComm, parser, **kwargs):
        super().__init__(**kwargs)
        
        # Detecting operating system
        self.isPosix = False # Windows
        if os.name == 'posix':
            self.isPosix = True # Linux or Mac

        # Defining the parameters for serial communication
        self.serPar = serPar

        # Defining the parameters for inter-worker comunication
        self.psComm = psComm

        # Setting the input message parser
        self.parser = parser

    def run(self):

        # Enabling communication        
        self.psComm.enableIO.set()
        
        # Trying to create a serial object
        try:
            self.ser = serial.Serial(
                    self.serPar.port
                , self.serPar.baudrate
                , self.serPar.bytesize
                , self.serPar.parity 
                , self.serPar.stopbits 
                , self.serPar.timeout
                , self.serPar.xonxoff
                , self.serPar.rtscts
                , self.serPar.write_timeout
                , self.serPar.dsrdtr
                , self.serPar.inter_byte_timeout
                , self.serPar.exclusive 
                #, **self.serPar.kwargs
            )
        except:
            #print("FAIL_TO_CREATE_SERIAL_OBJECT")
            self.psComm.qerr.put(FAIL_TO_CREATE_SERIAL_OBJECT)
            self.psComm.enableIO.clear()

        # Trying to open the serial connection
        try:
            if not (self.ser.is_open):
                self.ser.open()
            self.psComm.isOpen.set()
        except:
            self.psComm.qerr.put(FAIL_TO_OPEN_SERIAL_CONNECTION)
            self.psComm.isOpen.clear()
            self.psComm.enableIO.clear()
    
        # Defines a buffer to store input data
        buffer = ""

        # Creating the simulation path for fast return during the simulation
        import FlightDataImporter
        simulationPath = FlightDataImporter.LinearInterpolator([0.0,1.0],[0.0,0.0])
        tStart = 0.0

        # Trying to read/write (if enable)
        try:
            READING = 0
            WRITING = 1
            while self.psComm.enableIO.is_set():

                # Start reading
                state = READING

                # Getting the incomming bytes
                inflow = self.ser.read(self.ser.in_waiting or 1)

                # If any byte, adds it to the buffer. Parses the buffer. If there are messages
                # add them to the input queue. 
                if inflow:
                    # If in a posix system (linux or mac), removes return carriage character
                    if self.isPosix:
                        inflow = inflow.replace(b'\r\n', b'\n')
                    
                    inflow = inflow.decode('UTF-8', 'replace') # replaces bad characters with replacement character (U+FFFD)
                    
                    # If allowed to store raw input data to the queue, do it
                    if self.psComm.enableRXraw.is_set():
                        self.psComm.qRXraw.put(inflow)
                    
                    # Parsing data
                    buffer = buffer + inflow
                    result = self.parser.parse(buffer)
                    buffer = result[0]
                    for msg in result[1]:
                        #print("in: "+msg)
                        msgSplit=msg.split(",")
                        if msgSplit[0] == "1": # Request for the simulated altitude
                            t=int(msgSplit[1])*1e-3 # reading the time and converting it from ms to s
                            h=int(100.0*simulationPath.f(t+tStart)) # converts the altitude from m to cm
                            ans = "<7,"+str(h)+">"
                            #print("%9.3f%9.1f"%(t,h))
                            #print("out: "+ans)
                            self.ser.write(ans.encode('UTF-8'))
                            
                        else:
                            self.psComm.qRXmsg.put(msg)
                
                # Start writing
                state = WRITING

                # Transmitting data
                while not self.psComm.qTXmsg.empty():
                    msg = str(self.psComm.qTXmsg.get())
                    #print("out: "+msg)
                    if ( msg[0] == "6" ):  # Handling special message for the current thread to start simulation mode
                        filename = msg[1:]
                        #print("---> "+filename)
                        try:
                            data = FlightDataImporter.importData(filename)
                            tStart = data[0][0]
                            simulationPath = FlightDataImporter.LinearInterpolator(data[0], data[1])
                            txt="<6,1>"
                            self.ser.write(txt.encode('UTF-8'))
                            #print(txt)
                        except Exception as e: 
                            #print(e)
                            #print("Erro")
                            pass
                    else:
                        self.ser.write(msg.encode('UTF-8'))
                                
        except:
            # Adding the error to the list
            if state == READING:  
                self.psComm.qerr.put(FAIL_TO_READ_FROM_SERIAL)
                #print("FAIL_TO_READ_FROM_SERIAL")
            if state == WRITING:
                self.psComm.qerr.put(FAIL_TO_WRITE_TO_SERIAL)
                #print("FAIL_TO_WRITE_TO_SERIAL")

        # Trying to close the connection
        try:
            self.ser.close()
        except:
            self.psComm.qerr.put(FAIL_TO_CLOSE_SERIAL_CONNECTION)
            #print("FAIL_TO_CLOSE_SERIAL_CONNECTION")

        # Signaling the connection was interrupted
        self.psComm.isOpen.clear() 

        self.ser = None
        return

########################################################################################

"""

    Classes related to the wxPython that consumes from PSerial

"""

class wxPSerial(wx.EvtHandler):
    """
        wxPSerial is a consumer of PSerial that runs in a different Thread/Process than PSerial. 
        PSerial communicates with the serial port and parses the messages.
        wxPSerial checks for new messages every notificationPeriod milliseconds.
        
        wxPSerial also implements the Observer design pattern. If there are messages to communicate,
        it notifies all observers.
    """
    def __init__(self, parent):
        
        wx.EvtHandler.__init__(self)
        self.parent = parent
        # Creating the communication between this class (the consumer) and the PSerial (the producer)
        self.psComm = PSerialComm()

    def __del__( self ):
        """
            Closing the connection if still open
        """
        if self.isOpen():
           self.stop()
    
    def addObserver(self, observer):
        """
            Adds the observer to the list, if still not there
        """
        try:
            idx = self.observerList.index(observer)
        except:
            self.observerList.append(observer)

    def removeObserver(self, observer):
        """
            Removes the observer from the list, if it is there
        """
        try:
            self.observerList.remove(observer)
        except:
            return

    def timerUpdate(self, event):
        """
            Checks for new messages, errors and raw data every notificationPeriod milliseconds
        """
        errors  = self.getErrors()   # list of errors
        rawdata = self.getRawInput() # string
        msgs    = self.getMessages() # list of messages. The type of the messages depends on the parser

        if ( (len(rawdata)>0) or (len(msgs)>0) or (len(errors)>0) ):
            self.notify({"raw":rawdata,"msgs":msgs,"errors":errors})

            if len(errors)>0:
                self.stop()              
        event.Skip()

    def notify(self, msgs):
        """
            Notify all observers about the news
        """
        try:
            for observer in self.observerList:
                observer.wxPSerialUpdate(msgs)
        except:
            pass
        
    def sendMessage(self, msg):
        """
            Sends message msg to the serial port 
        """
        self.psComm.qTXmsg.put(msg)

    def getMessages(self):
        """
        Returns the list of messages in the input queue
        """
        msgs = []
        while not self.psComm.qRXmsg.empty():
            msgs.append(self.psComm.qRXmsg.get())
        return msgs

    def getErrors(self):
        """
        Returns the list of errors, if any
        """
        errors = []
        while not self.psComm.qerr.empty():
            errors.append(self.psComm.qerr.get())
        return errors

    def getRawInput(self):
        """
        Returns the raw input data
        """
        raw=""
        while not self.psComm.qRXraw.empty():
            raw+=self.psComm.qRXraw.get()
        return raw

    def enableRawInput(self):
        """
        Enables the PSerial to store the raw input
        """
        self.psComm.enableRXraw.set()

    def disableRawInput(self):
        """
        Disables the PSerial to store the raw input
        """
        self.psComm.enableRXraw.clear()

    def isOpen(self):
        """
        Returns true if the communication is available. Otherwise, returns false.
        """
        if self.psComm.isOpen.is_set():
            return True
        else:
            return False

    def start(self, serialParameters: SerialParameters, notificationPeriod=250, parser=BracketsMessageParser("<",">")):
        # Creating (not started yet) the dedicated thread/process to interact with the serial port
        self.serialWorker = PSerial(serialParameters, self.psComm, parser, daemon=True)
            
        # Creating a timer that will check for new messages from the PSerial every notificationPeriod (ms)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.timerUpdate, self.timer)
        self.timer.Start(milliseconds=notificationPeriod, oneShot=wx.TIMER_CONTINUOUS)
        
        # List of observers
        self.observerList = []

        # Adding parent as observer
        self.addObserver(self.parent)

        # Starting the serial communication
        self.serialWorker.start()

    def stop(self):
        """
        Stops the serial communication
        """
        while( self.psComm.enableIO.is_set() ):
            self.psComm.enableIO.clear()

        # Removing all elements from the queues before stopping
        errors  = self.getErrors()   # list of errors
        rawdata = self.getRawInput() # string
        msgs    = self.getMessages() # list of messages. The type of the messages depends on the parser

        if ( (len(rawdata)>0) or (len(msgs)>0) or (len(errors)>0) ):
            self.notify({"raw":rawdata,"msgs":msgs,"errors":errors})
        
        # Terminates the process
        finish(self.serialWorker)


class wxPSerialConnectionProgressDialog ( wx.Dialog ):
    """
        Creates a progress dialog during the connection to the serial port.
        The dialog creates a timer to check if the connection is open
        with a given frequency. After maxMillis, the dialog is closed.
    """
    def __init__( self, parent, title:str, wxpserial: wxPSerial, maxMillis=10000 ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Tentando estabelecer conexão com a porta serial. \nPor favor, aguarde...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

        self.progress = wx.Gauge( self.m_panel1, wx.ID_ANY, maxMillis, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.progress.SetValue( 0 )
        bSizer2.Add( self.progress, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.wxpserial = wxpserial
        self.maxMillis = maxMillis

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.timerUpdate, self.timer)
        self.timer.Start(milliseconds=300, oneShot=wx.TIMER_CONTINUOUS)
        self.time1 = time.time()

    def timerUpdate(self, event):
        elapsedTime = (time.time()-self.time1)*1000
                
        if self.wxpserial is None:
            self.timer.Stop()
            self.Destroy()
        else:
            if self.wxpserial.isOpen():
                self.timer.Stop()
                self.Destroy()

        if elapsedTime > self.maxMillis:
            self.timer.Stop()
            self.Destroy()
        else:
            self.progress.SetValue(elapsedTime)

# Lists the available serial ports
def availableSerialPorts():
    clist = []
    for p in serial.tools.list_ports.comports():
        clist.append(p.device)
    return clist