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

from FlightDataImporter import *
import numpy as np
import random


class FilterNone:
  def __init__(self, n):
    self.n = n
  def report(self):
    return "# Filtro: nenhum."
  def filter(self, i, vec):
    return vec[i]

class FilterCenteredMovingAverage:
  def __init__(self, n):
    self.n = n
  def report(self):
    return ["Filtro: média móvel central. Total de pontos: "+str(1+2*self.n)]
  def filter(self, i, vec):
    ibeg = i - self.n
    iend = i + self.n
    sum = 0.0
    for i in range(ibeg, iend+1):
      sum = sum + vec[i]
    return sum/(2.0*self.n+1.0)

class FilterBackwardMovingAverage:
  def __init__(self, n):
    self.n = 2*n
  def report(self):
    return ["Filtro: média móvel para trás (backward). Total de pontos "+str(self.n+1)]
  def filter(self, i, vec):
    ibeg = i - self.n
    iend = i
    sum = 0.0
    for i in range(ibeg, iend+1):
      sum = sum + vec[i]
    return sum/(self.n+1.0)

class FilterCentralIntegralAverage:
  def __init__(self, n):
    self.n = n
  def report(self):
    return ["Filtro: média móvel central por integração. Total de pontos "+str(2*self.n+1)]
  def filter(self, i, vec):
    ibeg = i - self.n
    iend = i + self.n
    sum = 0.0
    for i in range(ibeg+1, iend):
      sum = sum + vec[i]
    sum = sum + 0.5 *(vec[ibeg]+vec[iend])
    return sum/(iend-ibeg)


class FlightStatisticsS01:
    """
      Calculates speed and acceleration from the altitude curve.
      Applies a filter to reduce noise from calculations. 
    """
    def __init__(self, m=8, n=8, deltaT=0.1, filter=FilterCenteredMovingAverage(n=8)):

      self.clear()
      self.setParameters(m, n, deltaT, filter)
      
    def setParameters(self, m, n, deltaT, filter):
      self.m = m 
      self.n = n
      self.deltaT = deltaT
      self.filter = filter
      self.N    = 1 + 2*n + 2*m # Minimum number of altitude measurements
      self.Nbar = self.N-1      # Last index of the vectors
      self.recalculate()

    def clear(self):
      self.traw0 = np.array([]) # raw time (not uniformly distributed) (original)
      self.hraw0 = np.array([]) # raw altitude (original)
      self.traw  = np.array([]) # raw time (not uniformly distributed) (extended)
      self.hraw  = np.array([]) # raw altitude (extended)
      self.t     = np.array([]) # uniformly distributed time (deltaT)
      self.h     = np.array([]) # altitude h(t)
      self.hf    = np.array([]) # filtered altitude
      self.v     = np.array([]) # velocity
      self.ve    = np.array([]) # velocity estimated
      self.a     = np.array([]) # acceleration

    def calculate(self, time, altitude):
      self.traw0 = time
      self.hraw0 = altitude
      self.recalculate()

    def recalculate(self):
      if len(self.traw0) < 1:
        return
      self.traw = np.append(self.traw0[0]-2*(self.m+self.n)*self.deltaT,self.traw0)
      self.traw = np.append(self.traw, self.traw[-1]+2*(self.m+self.n)*self.deltaT)
      self.hraw = np.append(self.hraw0[0],self.hraw0)
      self.hraw = np.append(self.hraw, self.hraw[-1])

      if len(self.traw) > 1:
        tmin = self.traw[0]
        tmax = self.traw[-1]
        self.t, self.h = pathLinSpace(self.traw, self.hraw, self.deltaT, tmin, tmax)
        if self.isReady():
          self.hf = np.zeros(len(self.t))
          self.v  = np.zeros(len(self.t))
          self.ve = np.zeros(len(self.t))
          self.a  = np.zeros(len(self.t))
          imin = self.n
          imax = len(self.t)-self.n
          for i in range(imin,imax):
            self.hf[i] = self.filter.filter(i,self.h)
          imin = self.n+self.m
          imax = len(self.t)-self.n-self.m
          dT = (self.deltaT*self.m)
          for i in range(imin,imax):
            self.v[i] = (self.hf[i+self.m]-self.hf[i-self.m])/(2.0*dT)
            self.a[i] = (self.hf[i+self.m]-2.0*self.hf[i]+self.hf[i-self.m])/(dT*dT)
          self.ve = self.v

    def minNumberOfMeasurements(self):
      return self.N

    def isReady(self):
      return len(self.t) >= self.N

    def getRawAltitudeVector(self):
      return [self.traw0, self.hraw0]

    def getAltitudeVector(self):
      ibeg=self.N-1
      iend=len(self.t)-self.N+2
      return [self.t[ibeg:iend], self.h[ibeg:iend]]

    def getFilteredAltitudeVector(self):
      ibeg=self.N-1
      iend=len(self.t)-self.N+2      
      return [self.t[ibeg:iend],self.hf[ibeg:iend]]
    
    def getVelocityVector(self):
      ibeg=self.N-1
      iend=len(self.t)-self.N+2
      return [self.t[ibeg:iend],self.v[ibeg:iend]]
    
    def getAccelerationVector(self):
      ibeg=self.N-1
      iend=len(self.t)-self.N+2
      return [self.t[ibeg:iend],self.a[ibeg:iend]]
    
    def getMaxAltitude(self):
      t, h = self.getAltitudeVector()
      idx = h.argmax()
      return [t[idx], h[idx]]
    
    def getMaxSpeed(self):
      t, v = self.getVelocityVector()
      idx = v.argmax()
      return [t[idx], v[idx]]
    
    def getMaxAcceleration(self):
      t, a = self.getAccelerationVector()
      idx = a.argmax()
      return [t[idx], a[idx]]

    def description(self, cmt="# ", eol="\r\n"):
      log = []
      log.append("Estatística de voo (Modelo S01)")
      log.append("")
      log.append("Modelo S01 para cálculo de velocidade v e de aceleração a verticais")
      log.append("a partir da altura h como função do tempo t. Aplica interpolação linear")
      log.append("para obter particionamento uniforme (com partição dt) de h(t), caso os dados")
      log.append("de entrada não estejam uniformemente particionados. Aplica filtro do tipo ")
      log.append("média móvel central sobre a altura com n pontos à esquerda e n pontos à direita.")
      log.append("As derivadas para determinação da velocidade e da aceleração são calculadas com")
      log.append("a altura filtrada hf com esquemas de diferenças finitas centrais com partição no")
      log.append(" tempo de dT=m x dt, onde o parâmetro m é definido pelo usuário.")
      log.append("")
      log.append("Parâmetros do modelo:")
      log.append("n = "+str(self.m)+": parâmetro para aplicação do filtro")
      log.append("m = "+str(self.n)+": parâmetro para cálculo de derivadas")
      log.append("Intervalo de tempo (dt) para interpolação de altura (s): "+str(self.deltaT))
      log = log + self.filter.report()
      log.append("")
      log.append("Esquemas numéricos:")
      log.append("v(t) = ( hf(t+dT)-hf(t-dT) ) / ( 2dT ). dT = m*dt = "+str(self.m*self.deltaT)+"s")
      log.append("a(t) = (hf(t+dT)-2hf(t)+hf(t-dT) ) / ( dT² ). dT = m*dt = "+str(self.m*self.deltaT)+"s")
      log.append("")
      txt = ""
      for line in log:
        txt = txt + cmt + line + eol
      return txt

    def report(self, cmt="# ", eol="\r\n"):
      log = []
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
      log.append("hf: altura filtrada (m)")
      log.append(" v: velocidade (m/s)")
      log.append(" a: aceleração (m/s²)")

      log.append("%11s%11s%11s%11s%11s"%("t (s)","h(m)","hf (m)","v (m/s)","a(m/s2)"))
      ibeg=0#2*(self.n+self.m)
      iend=len(self.t)#-2*(self.n+self.m)
      log2 = []
      for i in range(ibeg,iend):
        log2.append("%11.2f%11.2f%11.2f%11.2f%11.2f"%(self.t[i],self.h[i],self.hf[i],self.v[i],self.a[i]))
      txt = self.description()
      for line in log:
        txt = txt + cmt + line + eol
      for line in log2:
        txt = txt + line + eol
      return txt


class FlightStatisticsS02:
    # todo: finish this class
    def __init__(self, m=8, n=8, deltaT=0.1, filter=FilterBackwardMovingAverage(n=8)):
      self.m = m 
      self.n = n
      self.deltaT = deltaT
      self.filter = filter

      self.N    = 1 + 2*n + 2*m # Minimum number of altitude measurements
      self.Nbar = self.N-1      # Last index of the vectors

      self.traw  = np.array([]) # raw time (not uniformly distributed)
      self.hraw  = np.array([]) # raw altitude
      self.t     = np.array([]) # uniformly distributed time (deltaT)
      self.h     = np.array([]) # altitude h(t)
      self.hf    = np.array([]) # filtered altitude
      self.v     = np.array([]) # velocity
      self.ve    = np.array([]) # velocity estimated
      self.a     = np.array([]) # acceleration

    def appendAltitude(self, time, altitude):
      self.traw = np.append(self.traw, time)
      self.hraw = np.append(self.hraw, altitude)

    def calculate(self):
      if len(self.traw) > 1:
        tmin = self.traw[0]
        tmax = self.traw[-1]
        self.t, self.h = pathLinSpace(self.traw, self.hraw, self.deltaT, tmin, tmax)
        if self.isReady():
          self.hf = np.zeros(len(self.t))
          self.v  = np.zeros(len(self.t))
          self.ve = np.zeros(len(self.t))
          self.a  = np.zeros(len(self.t))
          imin = 2*self.n
          imax = len(self.t)
          for i in range(imin,imax):
            self.hf[i] = self.filter.filter(i,self.h)
          
          imin = 2*(self.n+self.m)
          imax = len(self.t)
          dT = (self.deltaT*self.m)
          model = 1
          if model == 1:
            for i in range(imin,imax):
              vp = (self.hf[i]-self.hf[i-2*self.m])/(2.0*dT)
              ap = (self.hf[i]-2.0*self.hf[i-self.m]+self.hf[i-2*self.m])/(dT*dT)
              self.v[i] = vp
              self.a[i] = ap
              self.ve[i] = vp+ap*self.deltaT*(self.m+self.n)
          elif model == 2:
            for i in range(imin,imax):             
              vp = (3.0*self.hf[i]-4.0*self.hf[i-self.m]+self.hf[i-2*self.m])/(2.0*dT)
              ap = (self.hf[i]-2.0*self.hf[i-self.m]+self.hf[i-2*self.m])/(dT*dT)
              self.v[i] = vp
              self.a[i] = ap
              self.ve[i] = vp+ap*self.deltaT*(self.n)
          else:
            for i in range(imin,imax):                         
              v1 = (self.hf[i]-self.hf[i-2*self.m])/(2.0*dT)
              v2 = (3.0*self.hf[i]-4.0*self.hf[i-self.m]+self.hf[i-2*self.m])/(2.0*dT)
              ap = (v2-v1)/dT
              v3 = v2 + ap*self.deltaT*self.n
              self.v[i] = v2
              self.a[i] = ap
              self.ve[i] = v3         

    def minNumberOfMeasurements(self):
      return self.N

    def isReady(self):
      return len(self.t) >= self.N

    def getAltitudeVector(self):
      return [self.t, self.h]
    
    def getFilteredAltitudeVector(self):
      pos=self.n
      return [self.t[pos:-pos],self.hf[pos:-pos]]
    
    def getVelocityVector(self):
      pos=self.n+self.m
      return [self.t[pos:-pos],self.v[pos:-pos]]
    
    def getAccelerationVector(self):
      pos=self.n+self.m
      return [self.t[pos:-pos],self.a[pos:-pos]]
    
    def getApogee(self):
      t, h = self.getAltitudeVector()
      idx = h.argmax()
      return [t[idx], h[idx]]
    
    def getMaxSpeed(self):
      t, v = self.getVelocityVector()
      idx = v.argmax()
      return [t[idx], v[idx]]
    
    def getMaxAcceleration(self):
      t, a = self.getAccelerationVector()
      idx = a.argmax()
      return [t[idx], a[idx]]

if __name__ == "__main__":

  m = 8
  n = 8
  deltaT = 0.1

  flight = FlightStatisticsS01(m, n, deltaT, filter=FilterCenteredMovingAverage(n))

  #traw, hraw = importData("launch-11.txt")
  traw, hraw = importData("sim01.txt")

  flight.calculate(traw, hraw)

  print(flight.report())

  with open("sim01_out.txt","w") as fout:
    for i in range(0,len(flight.t)):
      fout.write("%9.2f %9.2f %9.2f %9.2f %9.2f %9.2f\n"%(flight.t[i], flight.h[i], flight.hf[i], flight.v[i], flight.ve[i], flight.a[i]))
