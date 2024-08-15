import math
import numpy as np
import FlightDataImporter

class FlightStatisticsKalmanAlfaFilter:
    """
      Calculates speed and acceleration from the altitude curve based on Kalman-Alpha filter
    """
    def __init__(self, deltaT=0.1, stdExp=2.0, Vc=170.0, stdModSub=32.0, stdModTra=0.1, dadt=32.0):

      self.clear()
      self.setParameters(deltaT, stdExp, Vc, stdModSub, stdModTra, dadt)
      
    def setParameters(self, deltaT, stdExp, Vc, stdModSub, stdModTra, dadt):
      self.deltaT = deltaT
      self.stdExp=stdExp
      self.Vc = Vc
      self.stdModSub = stdModSub
      self.stdModTra = stdModTra
      self.dadt = dadt
      self.N    = 32  # Minimum number of altitude measurements
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
      self.a     = np.array([]) # acceleration

    def calculate(self, time, altitude):
      self.clear()
      self.traw0 = time
      self.hraw0 = altitude
      self.recalculate()

    def recalculate(self):
      if len(self.traw0) < 1:
        return
      self.traw = np.append(self.traw0[0]-self.N*self.deltaT,self.traw0)
      self.traw = np.append(self.traw, self.traw[-1]+self.N*self.deltaT)
      self.hraw = np.append(self.hraw0[0],self.hraw0)
      self.hraw = np.append(self.hraw, self.hraw[-1])

      if len(self.traw) > 1:
        tmin = self.traw[0]
        tmax = self.traw[-1]
        self.t, self.h = FlightDataImporter.pathLinSpace(self.traw, self.hraw, self.deltaT, tmin, tmax)
        if self.isReady():
          T    =                        self.deltaT # Time step
          T2   =                            T*T*0.5 # Auxiliary variable
          Vexp =          self.stdExp * self.stdExp # Variance of the measurements
          VmodSub = self.stdModSub * self.stdModSub # Variance of the physical model for subsonic speed
          VmodTra = self.stdModTra * self.stdModTra # Variance of the physical model for subsonic speed
          dadt_ref = self.dadt
          da_ref_inv = 1.0 / ( dadt_ref * T)
          s=self.h[0]
          v=0.0
          a=0.0
          vs = v
          Vmod = VmodSub
          P00 = Vexp+Vmod*T*T*T*T*T*T/36.0
          P11 = Vexp/T+Vmod*T*T*T*T/4.0
          P22 = Vexp/(T*T)
          P01 = Vmod*T*T*T*T*T/12.0
          P02 = Vmod*T*T*T*T/6.0
          P12 = Vmod*T*T*T/2.0
          K0 = 0.0
          K1 = 0.0
          K2 = 0.0
          self.hf = np.zeros(len(self.t))
          self.v  = np.zeros(len(self.t))
          self.a  = np.zeros(len(self.t))

          self.hf[0] = s
          self.v[0] = v
          self.a[0] = a

          for i in range(1,len(self.h)):

            sMeasured =self.h[i]
            # Prediction step
            s += v*T + a*T2
            v +=       a*T
            #a = a;
            a0 = a

            if ( v > self.Vc ):
              Vmod = VmodTra
            else:
              Vmod = VmodSub
            
            c1 = P22*T2
            c2 = P22*T

            Ph00 = (c1+2.0*P12*T+2.0*P02)*T2+(P11*T+2.0*P01)*T+P00
            Ph11 = (c2+2.0*P12)*T+P11
            Ph22 = P22+Vmod*T*T
            Ph01 = (c2+P12)*T2+(P12*T+P02+P11)*T+P01
            Ph02 = c1+P12*T+P02
            Ph12 = c2+P12
            
            # Update step
            Sinv = 1.0/(Ph00+Vexp)

            # Updating the Kalman gain
            K0=Ph00*Sinv
            K1=Ph01*Sinv
            K2=Ph02*Sinv

            # Calculating the innovation (measured value - predicted value)
            innovation = sMeasured - s

            # Calculating the new estimate state
            s += K0*innovation
            v += K1*innovation
            a += K2*innovation
            
            # Calculating the new estimate covariance
            raux = 1.0-K0; 
            P00 = raux*Ph00
            P01 = raux*Ph01
            P02 = raux*Ph02
            P11 = Ph11-K1*Ph01
            P12 = Ph12-K1*Ph02
            P22 = Ph22-K2*Ph02

            # Alpha filter
            vs = vs + (v-vs)/(1.0+math.fabs(a-a0)*da_ref_inv)

            self.hf[i] = s
            self.v[i] = vs
            self.a[i] = a

    def minNumberOfMeasurements(self):
      return self.N

    def isReady(self):
      return len(self.t) >= self.N

    def getRawAltitudeVector(self):
      return [self.traw0, self.hraw0]

    def getAltitudeVector(self):
      ibeg=self.N
      iend=len(self.t)-self.N
      return [self.t[ibeg:iend], self.h[ibeg:iend]]

    def getFilteredAltitudeVector(self):
      ibeg=self.N
      iend=len(self.t)-self.N
      return [self.t[ibeg:iend],self.hf[ibeg:iend]]
    
    def getVelocityVector(self):
      ibeg=self.N
      iend=len(self.t)-self.N
      return [self.t[ibeg:iend],self.v[ibeg:iend]]
    
    def getAccelerationVector(self):
      ibeg=self.N
      iend=len(self.t)-self.N
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
      log.append("Estatística de voo (Modelo Kalman-Alfa)")
      log.append("")
      log.append("Modelo Kalman-Alfa para cálculo de velocidade v e de aceleração a verticais")
      log.append("a partir da altura h como função do tempo t. Aplica interpolação linear")
      log.append("para obter particionamento uniforme (com partição dt) de h(t), caso os dados")
      log.append("de entrada não estejam uniformemente particionados. Aplica filtro do tipo ")
      log.append("Kalman-Alfa dinâmico sobre a altura.")
      log.append("")
      log.append("Parâmetros do modelo:")
      log.append("stdExp = "+str(self.stdExp)+": incerteza experimental da altura (m)")
      log.append("Vc = "+str(self.Vc)+": velocidade crítica (m/s)")
      log.append("stdModSub = "+str(self.stdModSub)+": incerteza do modelo físico para V<Vc (m/s2)")
      log.append("stdModTra = "+str(self.stdModTra)+": incerteza do modelo físico para V>=Vc (m/s2)")
      log.append("dadt = "+str(self.dadt)+": tol. para derivada da aceleração (filtro alfa) (m/s3)")

      log.append("Intervalo de tempo (dt) para interpolação de altura (s): "+str(self.deltaT))
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