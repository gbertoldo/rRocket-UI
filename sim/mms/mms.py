import math
import random

class TrajectoryBase:
  def __init__(self, tB, tBurn, aprop, hG, g=9.81):
    self.tB = tB 
    self.tBurn = tBurn
    self.aprop = aprop
    self.hG = hG
    self.g = g
    self.tC = self.tB+self.tBurn
    self.hC = self.aprop * (self.tC-self.tB)*(self.tC-self.tB)/2
    self.vC = self.aprop * (self.tC-self.tB)
    self.tG = self.tC + (self.vC+math.sqrt(self.vC*self.vC+2.0*self.g*(self.hC-self.hG)))/self.g
    self.tD = self.tC + self.vC/self.g

  def h(self,t):
    if t < self.tB:
      return 0
    elif t <= self.tC:
      return self.aprop*(t-self.tB)*(t-self.tB)/2.0
    elif t <= self.tG:
      return self.hC + self.vC * (t - self.tC ) - self.g*(t - self.tC)*(t - self.tC)/2.0 
    else:
      return self.hG
    
class RestartFailure:
  def __init__(self, trajectory, tRestart):
    self.trajectory = trajectory
    self.tRestart = tRestart

  def h(self,t):
      if t < self.tRestart:
        return self.trajectory.h(self.tRestart)
      else:
        return self.trajectory.h(t)
      
class Ramp:
  def __init__(self, t0, h0, dt, dh):
    self.dh = dh
    self.dt = dt
    self.t0 = t0
    self.h0 = h0

  def h(self, t):
    if ( t < self.t0 ):
      return self.h0
    elif (t > self.t0+self.dt):
      return self.h0+self.dh
    else:
      return self.h0+self.dh/self.dt*(t-self.t0)

class Noise:
  def __init__(self, Uh):
    self.Uh = Uh

  def h(self, t):
    return self.Uh*(2.0*random.random()-1.0)
  
class SinusoidalPerturbation:
  def __init__(self, A, T, tBeg, tEnd):
    self.A = A
    self.T = T
    self.tBeg = tBeg
    self.tEnd = tEnd
  
  def h(self, t):
    if t < self.tBeg or t > self.tEnd:
      return 0.0
    else:
      return self.A * math.sin(2.0*math.pi*(t-self.tBeg)/self.T)

class Trajectory:
  def __init__(self, name, tbeg, tend):
    self.name = name
    self.tbeg = tbeg
    self.tend = tend
    self.funcList = []

  def append(self, func):
    self.funcList.append(func)
  
  def h(self, t):
    result = 0.0
    for func in self.funcList:
      result = result + func.h(t)
    return result


def runSimulation(mms):
  with open(mms.name+".txt","w") as file:
    t = mms.tbeg
    while (t < mms.tend):
      file.write("%14.7f%14.7f\n"%(t,mms.h(t)))
      t = t+deltaT


g = 9.81 # m/s2
deltaT = 0.05 # s


base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=2.902*g, hG=50.0, g=g)
mms = Trajectory("mms-01", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=1.932*g, hG=50.0, g=g)
mms = Trajectory("mms-02", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=1.932*g, hG=0.0, g=g)
mms = Trajectory("mms-03", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=1.932*g, hG=-50.0, g=g)
mms = Trajectory("mms-04", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=1.41*g, hG=50.0, g=g)
mms = Trajectory("mms-05", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=1.086*g, hG=50.0, g=g)
mms = Trajectory("mms-06", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=4.285*g, hG=50.0, g=g)
mms = Trajectory("mms-07", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=7.042*g, hG=50.0, g=g)
mms = Trajectory("mms-08", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=10.155*g, hG=50.0, g=g)
mms = Trajectory("mms-09", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=12.544*g, hG=50.0, g=g)
mms = Trajectory("mms-10", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=14.5595*g, hG=50.0, g=g)
mms = Trajectory("mms-11", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=2.902*g, hG=50.0, g=g)
noise = Noise(Uh=1.0)
ramp  = Ramp(t0=0.0, h0=0.0, dt=5.0, dh=10.0)
mountPerturbation  = SinusoidalPerturbation(A=50.0, T=0.6, tBeg=5.0,tEnd=5.6)
launchPerturbation = SinusoidalPerturbation(A=-135.0, T=2.2, tBeg=10.0,tEnd=11.1)
machPerturbation  = SinusoidalPerturbation(A=100.0, T=0.6, tBeg=base.tC,tEnd=base.tC+0.6)
mms = Trajectory("mms-12", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
mms.append(ramp)
mms.append(noise)
mms.append(mountPerturbation)
mms.append(launchPerturbation)
mms.append(machPerturbation)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=2.902*g, hG=50.0, g=g)
noise = Noise(Uh=1.0)
flightPerturbation = SinusoidalPerturbation(A=15.0, T=0.8, tBeg=10.0,tEnd=base.tG)
mms = Trajectory("mms-13", tbeg = 0.0, tend=base.tG+base.tB)
mms.append(base)
mms.append(noise)
mms.append(flightPerturbation)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=2.902*g, hG=50.0, g=g)
tRestart = (base.tB+base.tD)/2.0
traj = RestartFailure(base, tRestart=tRestart)
mms = Trajectory("mms-14", tbeg = tRestart, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)

base = TrajectoryBase(tB=10.0, tBurn=3.0, aprop=2.902*g, hG=50.0, g=g)
tRestart = (base.tG-base.tD)*0.2+base.tD
traj = RestartFailure(base, tRestart=tRestart)
mms = Trajectory("mms-15", tbeg = tRestart, tend=base.tG+base.tB)
mms.append(base)
runSimulation(mms)


