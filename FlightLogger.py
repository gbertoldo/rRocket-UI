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

import numpy as np

class FlightAltitudeLogger:
  def __init__(self):
    self.clear()

  def clear(self):
    self.t = np.array([])
    self.h = np.array([])
    
  def appendData(self, t, h):
    self.t = np.append( self.t, t )
    self.h = np.append( self.h, h )


class FlightSimulationLogger:
  def __init__(self, filename):
    self.clear()
    self.filename = filename
    self.observers = []

  def clear(self):
    self.t = np.array([])
    self.h = np.array([])
    self.v = np.array([])
    self.a = np.array([])
    self.status = []

  def addObserver(self, observer):
    self.observers.append(observer)

  def notify(self, event):
    try:
      for observer in self.observers:
        observer.updateSimulationFlightEvent(event)
    except:
      pass

  def appendData(self, t, h, v, a, status):
    self.t = np.append( self.t, t )
    self.h = np.append( self.h, h )
    self.v = np.append( self.v, v )
    self.a = np.append( self.a, a )
    self.status.append(status)
    if len(self.t)>1:
      idx = len(self.t)-1
      if self.status[idx] != self.status[idx-1]:
          self.notify([self.t[idx],self.h[idx],self.v[idx],self.a[idx],self.status[idx]])
    
  def getFlightEvents(self):
    events = []
    if len(self.t) > 0:
      i = 0
      events.append([self.t[i], self.h[i], self.v[i], self.a[i], self.status[i] ])
      for i in range(1,len(self.t)):
        if self.status[i] != self.status[i-1]:
          events.append([self.t[i],self.h[i],self.v[i],self.a[i],self.status[i]])
    return events
 
  def getMaxAltitude(self):
    idx = self.h.argmax()
    return [self.t[idx], self.h[idx]]
  
  def getMaxSpeed(self):
    idx = self.v.argmax()
    return [self.t[idx], self.v[idx]]
  
  def getMaxAcceleration(self):
    idx = self.a.argmax()
    return [self.t[idx], self.a[idx]]

  def report(self, cmt="# ", eol="\r\n"):
    log = []
    log.append("DADOS DA SIMULAÇÃO REALIZADA NO ALTÍMETRO")
    log.append("")
    log.append("Arquivo de entrada para trajetória: ")
    log.append(self.filename)
    log.append("")
    log.append("Eventos de voo")    
    log.append("R=ready: pronto para voo")
    log.append("F=flying: em voo ascendente")
    log.append("D=drogue: paraquedas auxiliar ativado")
    log.append("P=parachute: paraquedas principal ativado")
    log.append("L=landed: aterrissado")
    events = self.getFlightEvents()
    log.append("     t (s)      h(m)    v(m/s)   a(m/s²) Estado")
    for evt in events:
      log.append("%10.3f%10.1f%10.1f%10.1f%5s"%(evt[0],evt[1],evt[2],evt[3],evt[4]))
    log.append("")
    log.append("Valores extremos: ")
    log.append("    t (s)     valor  descrição")
    thmax = self.getMaxAltitude()
    tvmax = self.getMaxSpeed()
    tamax = self.getMaxAcceleration()
    log.append("%9.2f %9.2f %s"%(tamax[0],tamax[1]," aceleração máxima (m/s²)"))
    log.append("%9.2f %9.2f %s"%(tvmax[0],tvmax[1]," velocidade máxima (m/s)"))
    log.append("%9.2f %9.2f %s"%(thmax[0],thmax[1]," altura máxima (m)"))
    log.append("")
    log.append("Legenda:")
    log.append(" t: tempo (s)")
    log.append(" h: altura (m)")
    log.append(" v: velocidade (m/s)")
    log.append(" a: aceleração (m/s²)")
    log.append(" s: estado")

    log.append("")
    log.append("     t(s)       h(m)     v(m/s)    a(m/s²) Estado")
    ibeg=0
    iend=len(self.t)
    log2 = []
    for i in range(ibeg,iend):
      log2.append("%11.2f%11.2f%11.1f%11.1f%7s"%(self.t[i],self.h[i],self.v[i],self.a[i],self.status[i]))
    txt = ""
    for line in log:
      txt = txt + cmt + line + eol
    for line in log2:
      txt = txt + line + eol
    return txt



if __name__ == "__main__":
  data=[]
  data.append([1.301,44.3, 9.9,17.1 ,"R"])
  data.append([1.401,51.9,11.8,19.2 ,"R"])
  data.append([1.501,58.9,13.9,21.8 ,"R"])
  data.append([1.601,65.9,16.4,24.7 ,"F"])
  data.append([1.701,72.9,18.5,26.3 ,"F"])
  data.append([8.201,283.8,15.3,-8.5 ,"F"])
  data.append([8.301,283.8,14.3,-8.7 ,"F"])
  data.append([8.401,283.8,13.3,-8.8 ,"D"])
  data.append([8.501,283.8,12.3,-9.0 ,"D"])
  data.append([13.801,203.9,-19.5,-5.3 ,"D"])
  data.append([13.901,202.0,-19.6,-5.2 ,"D"])
  data.append([14.001,199.0,-19.7,-4.4 ,"D"])
  data.append([14.101,198.1,-19.7,-4.2 ,"P"])
  data.append([14.201,194.7,-19.9,-3.7 ,"P"])
  data.append([26.501,-7.6,-1.0, 2.5 ,"P"])
  data.append([26.601,-7.3,-0.5, 1.1 ,"P"])
  data.append([26.701,-7.3, 0.0,-0.3 ,"L"])
  data.append([26.801,-6.7, 0.0,-0.2 ,"L"])

  flightLogger = FlightSimulationLogger()
  for item in data:
    flightLogger.appendData(item[0],item[1],item[2],item[3],item[4])

  events = flightLogger.getFlightEvents()
  for evt in events:
    print(evt)