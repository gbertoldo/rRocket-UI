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

import UITemplate
import FlightStatistics
import copy

class FlightStatisticsFrame(UITemplate.FlightStatisticsFrame):
    def __init__(self, parent, flightStatistics):
        UITemplate.FlightStatisticsFrame.__init__(self, parent)
        self.parent = parent
        self.flightStatistics = copy.deepcopy(flightStatistics)
        self.spinCtrlDoublem.SetValue(flightStatistics.m)
        self.spinCtrlDoublen.SetValue(flightStatistics.n)
        self.spinCtrlDoubledt.SetValue(flightStatistics.deltaT)
        self.txtDescription.Clear()
        self.txtDescription.AppendText(flightStatistics.description())

    def updateParameters(self):
        m = int(self.spinCtrlDoublem.GetValue())
        n = int(self.spinCtrlDoublen.GetValue())
        deltaT = self.spinCtrlDoubledt.GetValue()
        filter = FlightStatistics.FilterCenteredMovingAverage(n)
        self.flightStatistics.setParameters(m, n, deltaT, filter)
        self.txtDescription.Clear()
        self.txtDescription.AppendText(self.flightStatistics.description())

    def onSpinCtrlDoublem( self, event ):
        self.updateParameters()

    def onSpinCtrlDoublen( self, event ):
        self.updateParameters()

    def onSpinCtrlDoubledt( self, event ):
        self.updateParameters()

    def onBtnCancel( self, event ):
        self.Destroy()

    def onBtnConfirm( self, event ):
        self.updateParameters()
        self.parent.setupFlightStatistics(self.flightStatistics)
        self.Destroy()

