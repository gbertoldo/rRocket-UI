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

import pandas as pd 
import numpy as np

def importData(filename, cols=[0,1], sep="\s+", engine='c', comment='#', header=None, skip_blank_lines=True):
  df = pd.read_csv(filename, sep=sep, comment=comment, engine=engine, header=header, skip_blank_lines=skip_blank_lines) 
  time     = df[df.columns[cols[0]]].to_numpy()
  altitude = df[df.columns[cols[1]]].to_numpy()
  return([time,altitude])

def replaceStrInFile(ifile, ofile, strFrom, strTo):
  # Read in the file
  with open(ifile, 'r') as file:
    filedata = file.read()

  # Replace the target string
  filedata = filedata.replace(strFrom, strTo)

  # Write the file out again
  with open(ofile, 'w', encoding="utf-8") as file:
    file.write(filedata)

def removeHeaderLinesFromFile(ifile, ofile, numberOfLines):
  lines = []

  # reading file
  with open(ifile, 'r') as fp:
      # read an store all lines into list
      lines = fp.readlines()

  iPos = numberOfLines
  if iPos < 0:
     iPos=0

  # Write file
  with open(ofile, 'w', encoding="utf-8") as fp:
      for line in lines[iPos:]:
        fp.write(line)


class LinearInterpolator:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.sz = len(x)
    self.lastIdx = 1 # used to accelerate the lookup
  
  def f(self, x):
    if x <= self.x[0]:
      return self.y[0]
    elif x >= self.x[-1]:
      return self.y[-1]
    else:
      firstIdx = 1
      if x > self.x[self.lastIdx]:
        firstIdx = self.lastIdx
      for i in range(firstIdx,self.sz):
        if x < self.x[i]:
          self.lastIdx = i
          return self.y[i-1]+(self.y[i]-self.y[i-1])*(x-self.x[i-1])/(self.x[i]-self.x[i-1])
        
def pathLinSpace(time, altitude, deltaT, tmin=10000, tmax=-10000):
  interpolator = LinearInterpolator(time, altitude)
  if tmin == 10000:
    tmin = np.min(time)
  if tmax == -10000:
    tmax = np.max(time)
  sz = int(float(tmax-tmin)/deltaT)+1
  t = np.zeros(sz)
  h = np.zeros(sz)
  for i in range(0, sz):
    t[i] = tmin + deltaT*i
    h[i] = interpolator.f(t[i])
  return [t,h]