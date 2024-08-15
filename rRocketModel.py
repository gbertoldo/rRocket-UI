"""
  The MIT License (MIT)

  rRocket-UI Graphical User Interface for rRocket
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

import wxpserial
import FlightLogger

"""
    Codes for sending messages to rRocket
"""
class OutputMessageCode:
    def __init__(self):
        self.readStaticParameters                = "0"
        self.readDynamicParameters               = "1"
        self.writeDynamicParameters              = "2"
        self.restoreToFactoryParameters          = "3"
        self.clearFlightMemory                   = "4"
        self.readFlightReport                    = "5"
        self.setSimulationMode                   = "6"
        self.setSimulatedFlightAltitude          = "7"
        self.setSpeedForLiftoffDetection         = "8"
        self.setSpeedForFallDetection            = "9"
        self.setSpeedForApogeeDetection          = "10"
        self.setParachuteDeploymentAltitude      = "11"
        self.setDisplacementForLandingDetection  = "12"
        self.setMaxNumberOfDeploymentAttempts    = "13"
        self.setTimeStepScaler                   = "14"

"""
    Codes for receiving messages from rRocket
"""
class InputMessageCode:
    def __init__(self):
        self.errorLog                         = 0
        self.requestSimulatedAltitude         = 1
        self.simulatedFlightState             = 2
        self.flightPath                       = 3
        self.firmwareVersion                  = 4
        self.simulatedMode                    = 5
        self.startedInitialization           =  6
        self.finishedInitialization          =  7
        self.stardedSendingMemoryReport      =  8
        self.finishedSendingMemoryReport     =  9
        self.liftoffEvent                    = 10
        self.drogueEvent                     = 11
        self.parachuteEvent                  = 12
        self.landedEvent                     = 13
        self.actuatorDischargeTime           = 14
        self.capacitorRechargeTime           = 15
        self.N                               = 16
        self.deltaT                          = 17
        self.speedForLiftoffDetection        = 18
        self.speedForFallDetection           = 19
        self.speedForApogeeDetection         = 20
        self.parachuteDeploymentAltitude     = 21
        self.displacementForLandingDetection = 22
        self.maxNumberOfDeploymentAttempts   = 23
        self.timeStepScaler                  = 24

class rRocketErrorCode:
    def __init__(self):
        self.err = []
        self.err.append({"id":0,"msg":"Nenhum erro registrado"})
        self.err.append({"id":1,"msg":"Falha na inicialização do barômetro"})
        self.err.append({"id":2,"msg":"Falha na inicialização do atuador"})
        self.err.append({"id":3,"msg":"Altura inferior ao limite mínimo para registro na memória permanente"})
        self.err.append({"id":4,"msg":"Altura superior ao limite máximo para registro na memória permanente"})
        self.err.append({"id":5,"msg":"Voo iniciado com memória de voo anterior não apagada"})

    def getErrorByID(self, id):
        msg = "Erro desconhecido"
        for e in self.err:
            try:
                if e["id"] == int(id):
                    msg = e["msg"]
                    break
            except:
                pass
        return msg

class rRocketParameter:
    def __init__(self, name, description, recordedValue, desiredValue, digits, minValue, maxValue, initialValue, increment):
        self.name = name
        self.description = description 
        self.recordedValue = recordedValue 
        self.desiredValue = desiredValue
        self.digits = digits
        self.minValue = minValue 
        self.maxValue = maxValue 
        self.initialValue = initialValue 
        self.increment = increment  

rRocketState = {"Disconnected":1, "Ready":2, "Simulating":3, "BusyForDataTransfer":4, "Initializing":5}

class rRocketModel(wxpserial.wxPSerial):
    def __init__(self, parent):
        wxpserial.wxPSerial.__init__(self, parent)

        self.ocode = OutputMessageCode()
        self.icode = InputMessageCode()
        self.ecode = rRocketErrorCode()

        self.state = rRocketState["Disconnected"]
        self.simulationMode = 0

        self.firmwareVersion = ""
        self.errorLog = []
        self.actuatorDischargeTime = 0
        self.capacitorRechargeTime = 0
        self.N = 0
        self.deltaT = 0
        self.createFlightLogger()
        self.createFlightSimulationLogger()
        
        self.listOfParameters = []
        self.listOfParameters.append(rRocketParameter(name=u"speedForLiftoffDetection", description=u"Velocidade (em módulo) para detecção de decolagem (m/s)",recordedValue=30, desiredValue=30, digits=0, minValue=10, maxValue=50, initialValue=30, increment=1))
        self.listOfParameters.append(rRocketParameter(name=u"speedForFallDetection", description=u"Velocidade (em módulo) para detecção de queda (m/s)",recordedValue=30,  desiredValue=30, digits=0, minValue=5, maxValue=50, initialValue=30, increment=1))
        self.listOfParameters.append(rRocketParameter(name=u"speedForApogeeDetection", description=u"Velocidade para detecção de apogeu (m/s)",recordedValue=0,  desiredValue=0, digits=0, minValue=-15, maxValue=15, initialValue=0, increment=1))
        self.listOfParameters.append(rRocketParameter(name=u"parachuteDeploymentAltitude", description=u"Altura acima do ponto de lançamento para acionamento do paraquedas principal (m)",recordedValue=200,  desiredValue=200, digits=0, minValue=50, maxValue=10000, initialValue=200, increment=1))
        self.listOfParameters.append(rRocketParameter(name=u"displacementForLandingDetection", description=u"Deslocamento máximo para detecção de pouso (m)",recordedValue=3,  desiredValue=3, digits=0, minValue=2, maxValue=6, initialValue=3, increment=1))
        self.listOfParameters.append(rRocketParameter(name=u"maxNumberOfDeploymentAttempts", description=u"Número máximo de tentativas de acionamento de paraquedas (por paraquedas)",recordedValue=3,  desiredValue=3, digits=0, minValue=1, maxValue=100, initialValue=3, increment=1))
        self.listOfParameters.append(rRocketParameter(name=u"timeStepScaler", description=u"Multiplicador de passo de tempo para registro de trajetória após acionamento do drogue",recordedValue=10,  desiredValue=10, digits=0, minValue=1, maxValue=50, initialValue=10, increment=1))

    # Overriding the parent's method 
    def start(self, serialParameters: wxpserial.SerialParameters, notificationPeriod=250, parser=wxpserial.BracketsMessageParser("<",">")):
        wxpserial.wxPSerial.start(self, serialParameters, notificationPeriod,parser)
        self.clearFlightLogger()
        self.createFlightSimulationLogger()

    # Overriding the parent's method 
    def stop(self):
        wxpserial.wxPSerial.stop(self)
        self.setState(rRocketState["Disconnected"])

    def setState(self, state):
        self.state = state
        for observer in self.observerList:
            observer.rRocketModelStateUpdate()


    def parametersReport(self, cmt="# ", eol="\r\n"):
        log = []
        log.append("rRocket - Firmware "+self.firmwareVersion)
        log.append("")
        log.append("Parâmetros estáticos (definidos no firmware):")
        log.append("%9d: tempo para descarga do capacitor (ms)"%(self.actuatorDischargeTime))
        log.append("%9d: tempo para recarga do capacitor (ms)"%(self.capacitorRechargeTime))
        log.append("%9d: período de amostragem da altitude (ms)"%(self.deltaT))
        log.append("%9d: número de amostras para cálculo de estatística de voo"%(self.N+1))
        log.append("")

        log.append("Parâmetros de voo:")
        log.append("%14.1f: %s"%(self.getRecordedValue("speedForLiftoffDetection"),self.getDescription("speedForLiftoffDetection")))
        log.append("%14.1f: %s"%(self.getRecordedValue("speedForFallDetection"),self.getDescription("speedForFallDetection")))
        log.append("%14.1f: %s"%(self.getRecordedValue("speedForApogeeDetection"),self.getDescription("speedForApogeeDetection")))
        log.append("%14.1f: %s"%(self.getRecordedValue("parachuteDeploymentAltitude"),self.getDescription("parachuteDeploymentAltitude")))
        log.append("%14.1f: %s"%(self.getRecordedValue("displacementForLandingDetection"),self.getDescription("displacementForLandingDetection")))
        log.append("%14.1f: %s"%(self.getRecordedValue("maxNumberOfDeploymentAttempts"),self.getDescription("maxNumberOfDeploymentAttempts")))
        log.append("%14.1f: %s"%(self.getRecordedValue("timeStepScaler"),self.getDescription("timeStepScaler")))
        log.append("")
        txt = ""
        for line in log:
            txt = txt + cmt + line + eol
        return txt

    def errorsReport(self, cmt="# ", eol="\r\n"):
        log = []
        log.append("Códigos de erro reportados:")
        for i in self.errorLog:
            try:
                errorID = int(i)
                log.append(" --> Código %3d: "%(errorID)+self.ecode.getErrorByID(errorID))
            except:
                pass
        log.append("")
        txt = ""
        for line in log:
            txt = txt + cmt + line + eol
        return txt
    
    def eventsReport(self, cmt="# ", eol="\r\n"):
        log = []
        log.append("Eventos de voo:")
        for evt in self.flightEvents:
            if evt[4] == "F":
                log.append("%14.3f s: Voo detectado"%(evt[0]))
            if evt[4] == "D":
                log.append("%14.3f s: Drogue acionado"%(evt[0]))
            if evt[4] == "P":
                log.append("%14.3f s: Paraquedas principal acionado"%(evt[0]))
            if evt[4] == "L":
                log.append("%14.3f s: Aterrissagem detectada"%(evt[0]))
        log.append("")
        txt = ""
        for line in log:
            txt = txt + cmt + line + eol
        return txt
    
    def flightReport(self, cmt="# ", eol="\r\n"):
        log = []
        txt = self.parametersReport(cmt, eol) + self.errorsReport(cmt, eol) + self.eventsReport(cmt, eol)

        log.append(cmt)
        log.append(cmt+"Trajetória registrada na memória do altímetro")
        log.append(cmt+"%14s%14s"%("t (s)","h (m)"))
        for i in range(0,len(self.flightAltitudeLogger.t)):
            log.append("%14.3f%14.1f"%(self.flightAltitudeLogger.t[i],self.flightAltitudeLogger.h[i]))

        log.append("")
        for line in log:
            txt = txt + line + eol
        return txt
    
    def flightSimulationReport(self, cmt="# ", eol="\r\n"):
        txt = self.parametersReport(cmt, eol) + self.errorsReport(cmt, eol) 
        txt = txt + self.flightSimulationLogger.report()
        return txt
    
    def createFlightLogger(self):
        self.flightEvents = [] 
        self.flightAltitudeLogger = FlightLogger.FlightAltitudeLogger()
        try:
          for observer in self.observerList:
            observer.rRocketModelFlightUpdate()
        except:
            pass
        return 

    def clearFlightLogger(self):
        self.flightEvents = [] 
        self.flightAltitudeLogger.clear()
        try:
          for observer in self.observerList:
            observer.rRocketModelFlightUpdate()
        except:
            pass
        return 

    def createFlightSimulationLogger(self, filename=""):
        self.flightSimulationLogger = FlightLogger.FlightSimulationLogger(filename)
        self.flightSimulationLogger.addObserver(self)
        try:
          for observer in self.observerList:
            observer.rRocketModelSimulationModeUpdate()
            observer.rRocketModelSimulationUpdate()
        except:
            pass
        return 
    
    def updateSimulationFlightEvent(self, event):
      try:
        for observer in self.observerList:
          observer.rRocketModelSimulationFlightEventUpdate(event)
      except:
          pass
      return 

    def getDescription(self, name):
        for p in self.listOfParameters:
            if  p.name == name:
                return p.description
        return None  

    def getRecordedValue(self, name):
        for p in self.listOfParameters:
            if  p.name == name:
                return p.recordedValue
        return None    
    
    def getDesiredValue(self, name):
        for p in self.listOfParameters:
            if  p.name == name:
                return p.desiredValue
        return None    
    
    def readStaticParameters(self):
        self.sendMessage("<"+self.ocode.readStaticParameters+">")
    def readDynamicParameters(self):
        self.sendMessage("<"+self.ocode.readDynamicParameters+">")
    def writeDynamicParameters(self):
        self.clearFlightLogger()
        self.sendSpeedForLiftoffDetection(self.getDesiredValue("speedForLiftoffDetection"))
        self.sendSpeedForFallDetection(self.getDesiredValue("speedForFallDetection"))
        self.sendSpeedForApogeeDetection(self.getDesiredValue("speedForApogeeDetection"))
        self.sendParachuteDeploymentAltitude(self.getDesiredValue("parachuteDeploymentAltitude"))
        self.sendDisplacementForLandingDetection(self.getDesiredValue("displacementForLandingDetection"))
        self.sendMaxNumberOfDeploymentAttempts(self.getDesiredValue("maxNumberOfDeploymentAttempts"))
        self.sendTimeStepScaler(self.getDesiredValue("timeStepScaler"))
        self.sendMessage("<"+self.ocode.writeDynamicParameters+">")
    def resetToFactoryParameters(self):
        self.clearFlightLogger()
        self.sendMessage("<"+self.ocode.restoreToFactoryParameters+">")
    def clearLastFlight(self):
        self.clearFlightLogger()
        self.sendMessage("<"+self.ocode.clearFlightMemory+">")
    def readLastFlightData(self):
        self.clearFlightLogger()
        self.sendMessage("<"+self.ocode.readFlightReport+">")
    def startSimulationMode(self, filename, simfilename):
        self.clearFlightLogger()
        self.createFlightSimulationLogger(filename)
        self.sendMessage(self.ocode.setSimulationMode+simfilename) # Special message to be handled by the communication thread
    def stopSimulationMode(self):
        self.sendMessage("<"+self.ocode.setSimulationMode+",0"+">")
    def sendAltitude(self, h):
        # h: altitude (m)
        self.sendMessage("<"+self.ocode.setSimulatedFlightAltitude+","+str(int(h*100.0))+">") # converts altitude to cm
    def sendSpeedForLiftoffDetection(self, value):
        # value: speed (m/s)
        self.sendMessage("<"+self.ocode.setSpeedForLiftoffDetection+","+str(int(value*1.0))+">") # converts speed to m/s   
    def sendSpeedForFallDetection(self, value):
        # value: speed (m/s)
        self.sendMessage("<"+self.ocode.setSpeedForFallDetection+","+str(int(value*1.0))+">") # converts speed to m/s
    def sendSpeedForApogeeDetection(self, value):
        self.sendMessage("<"+self.ocode.setSpeedForApogeeDetection+","+str(int(value*1.0))+">") # converts speed to m/s
    def sendParachuteDeploymentAltitude(self, value):
        # value: altitude (m)
        self.sendMessage("<"+self.ocode.setParachuteDeploymentAltitude+","+str(int(value*1.0))+">") # converts value to m
    def sendDisplacementForLandingDetection(self, value):
        # value: displacement (m)
        self.sendMessage("<"+self.ocode.setDisplacementForLandingDetection+","+str(int(value*1.0))+">") # converts value to m
    def sendMaxNumberOfDeploymentAttempts(self, value):
        self.sendMessage("<"+self.ocode.setMaxNumberOfDeploymentAttempts+","+str(int(value))+">")
    def sendTimeStepScaler(self, value):
        self.sendMessage("<"+self.ocode.setTimeStepScaler+","+str(int(value))+">")

    def notify(self, data):
        """
            Notify all observers about the news
        """
        if len(data["msgs"]) > 0:
            updatedSimulation = False
            updatedParameters = False
            updatedFlight = False
            finishedMemoryReport = False
            for msg in data["msgs"]:
                msgSplit = msg.split(",")
                code = int(msgSplit[0])
                if code == self.icode.errorLog:
                    self.errorLog = msgSplit[1]
                    self.errorLog = ''.join(self.errorLog.split()) # Removing blanks
                    self.errorLog = self.errorLog.split(";")
                if code == self.icode.simulatedFlightState:
                    t=float(msgSplit[1])*1E-3 # ms to s
                    h=float(msgSplit[2])*0.1 # dm to m
                    v=float(msgSplit[3])*0.1 # dm/s to m/s
                    a=float(msgSplit[4])*0.1 # dm/s2 to m/s2
                    status=msgSplit[5]
                    #print(("%10.3f%10.1f%10.1f%10.1f %s")%(t,h,v,a,status))
                    self.flightSimulationLogger.appendData(t, h, v, a, status)
                    if len( self.flightSimulationLogger.status ) > 1:
                      if  (self.flightSimulationLogger.status[-1] == "L") and (self.flightSimulationLogger.status[-2] == "P"):
                        self.stopSimulationMode()
                        #self.readLastFlightData()

                    updatedSimulation = True
                if code == self.icode.flightPath:
                    self.flightAltitudeLogger.appendData(0.001*float(msgSplit[1]),0.1*float(msgSplit[2]))
                    updatedFlight = True
                if code == self.icode.firmwareVersion:
                    self.firmwareVersion = msgSplit[1]
                    updatedParameters = True
                if code == self.icode.simulatedMode:
                    if int(msgSplit[1]) == 1:
                        self.simulationMode = 1
                    else:
                        self.simulationMode = 0

                if code == self.icode.startedInitialization:
                    self.setState(rRocketState["Initializing"])
                if code == self.icode.finishedInitialization:
                    if self.simulationMode == 0:
                        self.readLastFlightData()
                        self.setState(rRocketState["Ready"])
                    else:
                        self.setState(rRocketState["Simulating"])
                if code == self.icode.stardedSendingMemoryReport:
                    self.clearFlightLogger()
                    self.setState(rRocketState["BusyForDataTransfer"])
                if code == self.icode.finishedSendingMemoryReport:
                    updatedFlight = False
                    for observer in self.observerList:
                        observer.rRocketModelFinishedReceivingMemoryReportUpdate()
                    if self.simulationMode == 0:
                        self.setState(rRocketState["Ready"]) 
                    else:
                        self.setState(rRocketState["Simulating"])                                         
                if code == self.icode.liftoffEvent:
                    evt=[float(msgSplit[1])*1E-3, 0, 0, 0, 'F']
                    self.flightEvents.append(evt)
                    for observer in self.observerList:
                        observer.rRocketModelFlightEventUpdate(evt)
                if code == self.icode.drogueEvent:
                    evt=[float(msgSplit[1])*1E-3, 0, 0, 0, 'D']
                    self.flightEvents.append(evt)
                    for observer in self.observerList:
                        observer.rRocketModelFlightEventUpdate(evt)
                if code == self.icode.parachuteEvent:
                    evt=[float(msgSplit[1])*1E-3, 0, 0, 0, 'P']
                    self.flightEvents.append(evt)
                    for observer in self.observerList:
                        observer.rRocketModelFlightEventUpdate(evt)
                if code == self.icode.landedEvent:
                    evt=[float(msgSplit[1])*1E-3, 0, 0, 0, 'L']
                    self.flightEvents.append(evt)
                    for observer in self.observerList:
                        observer.rRocketModelFlightEventUpdate(evt)
                if code == self.icode.actuatorDischargeTime:
                    self.actuatorDischargeTime = int(msgSplit[1])
                if code == self.icode.capacitorRechargeTime:
                    self.capacitorRechargeTime = int(msgSplit[1])
                if code == self.icode.N:
                    self.N = int(msgSplit[1])
                if code == self.icode.deltaT:
                    self.deltaT = int(msgSplit[1])
                if code == self.icode.speedForLiftoffDetection:
                    for p in self.listOfParameters:
                        if p.name == "speedForLiftoffDetection":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True
                if code == self.icode.speedForFallDetection:
                    for p in self.listOfParameters:
                        if p.name == "speedForFallDetection":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True
                if code == self.icode.speedForApogeeDetection:
                    for p in self.listOfParameters:
                        if p.name == "speedForApogeeDetection":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True
                if code == self.icode.parachuteDeploymentAltitude:
                    for p in self.listOfParameters:
                        if p.name == "parachuteDeploymentAltitude":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True
                if code == self.icode.displacementForLandingDetection:
                    for p in self.listOfParameters:
                        if p.name == "displacementForLandingDetection":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True
                if code == self.icode.maxNumberOfDeploymentAttempts:
                    for p in self.listOfParameters:
                        if p.name == "maxNumberOfDeploymentAttempts":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True
                if code == self.icode.timeStepScaler:
                    for p in self.listOfParameters:
                        if p.name == "timeStepScaler":
                            p.recordedValue = float(msgSplit[1])
                    updatedParameters = True

        if updatedParameters:
            for observer in self.observerList:
                    observer.rRocketModelParameterUpdate()
        if updatedFlight:
            for observer in self.observerList:
                    observer.rRocketModelFlightUpdate()
        if updatedSimulation:
            for observer in self.observerList:
                    observer.rRocketModelSimulationUpdate()

        try:
            if len(data["errors"] ) > 0:
                for observer in self.observerList:
                    observer.rRocketModelErrorsUpdate(data["errors"])

        except:
            pass
