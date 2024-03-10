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

import wx
import numpy as np
import UITemplate
import UIPlot
from UIFlightStatistics import *
from UIReportFrame import *

class PanelMemory(UITemplate.PanelMemory):
    def __init__(self, parent):
        UITemplate.PanelMemory.__init__(self, parent)

        self.parent = parent
        self.btnClearMemory.SetBackgroundColour(wx.Colour(wx.RED))
        #self.btnClearMemory.SetForegroundColour(wx.Colour(wx.WHITE))
        # Plot panel
        self.plotPanel = UIPlot.rRocketPlot(self.panelBase, ["-*","-x","-o"], 10,100, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.plotPanel.setXLabel("t (s)")
        self.plotPanel.setYLabel("")
        self.plotPanel.setLegend(["Altura (m)", "Velocidade (m/s)", "Aceleração (m/s²)"])
        self.plotPanel.setGrid()
        self.plotPanel.addToolbar()
        #self.plotEmpty()

    def confirmMemoryErase(self):
        dlg = wx.MessageDialog(self, "O procedimento apagará a memória do último voo. Confirma?", "Confirmar limpeza de memória de voo", wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            return True
        else:
            return False

    def plotEmpty(self):
        p = [np.array([0,0]),np.array([[0,0]])]
        self.plotPanel.draw([p,p,p])
    
    def plotHVA(self, data1, data2, data3):
        self.plotPanel.draw([data1, data2, data3])

    def plotEvent(self, evt):
        self.plotPanel.plotEvent(evt, showH=False)

    def clearEvents(self):
        self.plotPanel.clearEvents()

    def setupFlightStatistics(self, flightStatistics):
        self.parent.rRocketModel.flightStatistics = flightStatistics
        self.parent.rRocketModel.readLastFlightData()

    def onBtnSetupFlightStatistics( self, event ):
        flightStatistics = self.parent.rRocketModel.flightStatistics
        frm = FlightStatisticsFrame(self, flightStatistics)
        frm.Show()

    def onBtnReadMemory( self, event ):
        self.parent.rRocketModel.readLastFlightData()

    def onBtnFlightReport( self, event ):
        if len(self.parent.rRocketModel.flightAltitudeLogger.t) > 0:
            log = self.parent.getFlightReport()
            reportFrm = ReportFrame(self)
            reportFrm.setText(log)
            reportFrm.Show() 
            event.Skip()
        else:
            wx.MessageBox("Memória de voo vazia.", "Relatório de voo", wx.OK | wx.ICON_INFORMATION)

    def onBtnClearMemory( self, event ):
        if self.confirmMemoryErase():
            self.parent.rRocketModel.clearLastFlight()
            self.plotEmpty()
            self.clearEvents()

    def setDisconnectedAppearance(self):
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)
        self.btnSetupFlightStatistics.Enable(False)

    def setReadyAppearance(self):
        self.btnClearMemory.Enable(True)
        self.btnFlightReport.Enable(True)
        self.btnReadMemory.Enable(True)
        self.btnSetupFlightStatistics.Enable(True)

    def setInitializingAppearance(self):
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)
        self.btnSetupFlightStatistics.Enable(False)

    def setSimulatingAppearance(self):
        self.clearEvents()
        self.plotEmpty()
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)
        self.btnSetupFlightStatistics.Enable(False)

    def setBusyForDataTransferAppearance(self):
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)
        self.btnSetupFlightStatistics.Enable(False)

