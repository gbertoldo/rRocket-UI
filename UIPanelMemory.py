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
from UIReportFrame import *
from UIModelessDialog import *
import UIInputFileFormatFrame

class PanelMemory(UITemplate.PanelMemory):
    def __init__(self, parent):
        UITemplate.PanelMemory.__init__(self, parent)

        self.parent = parent
        self.btnClearMemory.SetBackgroundColour(wx.Colour(wx.RED))
        #self.btnClearMemory.SetForegroundColour(wx.Colour(wx.WHITE))
        # Plot panel
        self.plotPanel = UIPlot.rRocketPlot(self.panelBase, ["-*"], 10,100, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.plotPanel.setXLabel("t (s)")
        self.plotPanel.setYLabel("h (m)")
        #self.plotPanel.setLegend(["Altura (m)"])
        self.plotPanel.setGrid()
        self.plotPanel.addToolbar()
        #self.plotEmpty()

        self.inputFileFormat = UIInputFileFormatFrame.InputFileFormat()

    def confirmMemoryErase(self):
        dlg = wx.MessageDialog(self, "O procedimento apagará a memória do último voo. Confirma?", "Confirmar limpeza de memória de voo", wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            return True
        else:
            return False

    def plotEmpty(self):
        p = [np.array([0,0])]
        self.plotPanel.draw(p)
    
    def plotH(self, data):
        self.plotPanel.draw([data])

    def plotEvent(self, evt):
        self.plotPanel.plotEvent(evt, showH=False)

    def clearEvents(self):
        self.plotPanel.clearEvents()

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
            mbox = ModelessDialog(self, "Relatório de voo", "Memória de voo vazia.", delayMS=5000)
            mbox.Show()

    def onBtnClearMemory( self, event ):
        if self.confirmMemoryErase():
            self.parent.rRocketModel.clearLastFlight()
            self.plotEmpty()
            self.clearEvents()
            
    def onBtnSetTitle( self, event ):
        txt = self.txtCtrlPlotTitle.GetValue()
        self.plotPanel.setTitle(txt)

    def setDisconnectedAppearance(self):
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)

    def setReadyAppearance(self):
        self.btnClearMemory.Enable(True)
        self.btnFlightReport.Enable(True)
        self.btnReadMemory.Enable(True)

    def setInitializingAppearance(self):
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)

    def setSimulatingAppearance(self):
        self.clearEvents()
        self.plotEmpty()
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)

    def setBusyForDataTransferAppearance(self):
        self.btnClearMemory.Enable(False)
        self.btnFlightReport.Enable(False)
        self.btnReadMemory.Enable(False)

