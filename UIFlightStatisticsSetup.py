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
import FlightStatisticsKalmanAlfaFilter
import FlightStatisticsMovingAverage
import copy
import wx

class PanelStatKalmanAlfaFilter(UITemplate.PanelStatKalmanAlfaFilter):
    def __init__(self, parent, flightStatistics:FlightStatisticsKalmanAlfaFilter.FlightStatisticsKalmanAlfaFilter):
        UITemplate.PanelStatKalmanAlfaFilter.__init__(self, parent)
        self.parent = parent
        self.flightStatistics = copy.deepcopy(flightStatistics)
        self.fillForm(self.flightStatistics)

    def fillForm(self, stat:FlightStatisticsKalmanAlfaFilter.FlightStatisticsKalmanAlfaFilter):
        self.spinCtrlDoubledt.SetValue(stat.deltaT)
        self.spinCtrlDoubleStdExp.SetValue(stat.stdExp)
        self.spinCtrlDoubleVc.SetValue(stat.Vc)
        self.spinCtrlDoubleStdModSub.SetValue(stat.stdModSub)
        self.spinCtrlDoubleStdModTra.SetValue(stat.stdModTra)
        self.spinCtrlDoubleDaDt.SetValue(stat.dadt)

    def extractForm(self):
        deltaT = self.spinCtrlDoubledt.GetValue()
        stdExp = self.spinCtrlDoubleStdExp.GetValue()
        Vc = self.spinCtrlDoubleVc.GetValue()
        stdModSub = self.spinCtrlDoubleStdModSub.GetValue()
        stdModTra = self.spinCtrlDoubleStdModTra.GetValue()
        dadt = self.spinCtrlDoubleDaDt.GetValue()
        self.flightStatistics.setParameters(deltaT, stdExp, Vc, stdModSub, stdModTra, dadt)
        return self.flightStatistics


class PanelStatMovingAverage(UITemplate.PanelStatMovingAverage):
    def __init__(self, parent, flightStatistics:FlightStatisticsMovingAverage.FlightStatisticsMovingAverage):
        UITemplate.PanelStatMovingAverage.__init__(self, parent)
        self.parent = parent
        self.flightStatistics = copy.deepcopy(flightStatistics)
        self.fillForm(self.flightStatistics)

    def fillForm(self, stat:FlightStatisticsMovingAverage.FlightStatisticsMovingAverage):
        self.spinCtrlDoubledt.SetValue(stat.deltaT)
        self.spinCtrlDoublem.SetValue(stat.m)
        self.spinCtrlDoublen.SetValue(stat.n)

    def extractForm(self):
        dT = self.spinCtrlDoubledt.GetValue()
        m = int(self.spinCtrlDoublem.GetValue())
        n = int(self.spinCtrlDoublen.GetValue())
        self.flightStatistics.setParameters(m, n, dT, FlightStatisticsMovingAverage.FilterCenteredMovingAverage(n))
        return self.flightStatistics

class FlightStatisticsSetup(UITemplate.FlightStatisticsSetup):
    def __init__(self, parent, flightStatistics):
        UITemplate.FlightStatisticsSetup.__init__(self, parent)
        self.parent = parent
        self.flightStatistics = copy.deepcopy(flightStatistics)
        self.choiceModel.Clear()
        self.choiceModel.SetItems([u"Kalman-Alfa",u"Média móvel"])
        self.currentPanel = None
        self.fillForm(self.flightStatistics)

    def fillForm(self, flightStatistics):
        if self.currentPanel is not None:
            self.currentPanel.Destroy()
        if isinstance(flightStatistics, FlightStatisticsMovingAverage.FlightStatisticsMovingAverage):
            self.choiceModel.SetSelection(1)
            self.currentPanel = PanelStatMovingAverage(self.panelBase, self.flightStatistics)
        else:
            self.choiceModel.SetSelection(0)
            self.currentPanel = PanelStatKalmanAlfaFilter(self.panelBase, self.flightStatistics)

        txt = self.flightStatistics.description()
        self.txtDescription.SetLabel(txt)
        bSizer = wx.BoxSizer( wx.VERTICAL )
        bSizer.Add( self.currentPanel, 1, wx.EXPAND|wx.ALL, 5 )
        self.Layout()

    def updateForm(self):
        opt = self.choiceModel.GetSelection()
        if opt == 0:
            self.flightStatistics = FlightStatisticsKalmanAlfaFilter.FlightStatisticsKalmanAlfaFilter()
        elif opt == 1:
            self.flightStatistics = FlightStatisticsMovingAverage.FlightStatisticsMovingAverage()
        self.fillForm(self.flightStatistics)    
 
    def onChoiceModel( self, event ):
        self.updateForm()

    def onBtnCancel( self, event ):
        self.Destroy()

    def onBtnConfirm( self, event ):
        self.flightStatistics = self.currentPanel.extractForm()
        self.parent.setupFlightStatistics(self.flightStatistics)
        self.Destroy()

if __name__ == "__main__":
  import wx
  app = wx.App()
  mainFrame = FlightStatisticsSetup(parent=None, flightStatistics=None)
  mainFrame.Show()
  app.MainLoop()