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
import UITemplate
import UIPlot
import FlightDataImporter
from UIReportFrame import *
from rRocketModel import *

class PanelSimulation(UITemplate.PanelSimulation):
    def __init__(self, parent):
        UITemplate.PanelSimulation.__init__(self, parent)
        self.parent = parent
        # Plot panel
        self.plotPanel = UIPlot.rRocketPlot( self.panelBase, ["-*","-x","-o"], 10,100, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.plotPanel.setXLabel("t (s)")
        self.plotPanel.setYLabel("")
        self.plotPanel.setLegend(["Altura (m)", "Velocidade (m/s)", "Aceleração (m/s²)"])
        self.plotPanel.setGrid()
        self.plotPanel.addToolbar()

    def plot(self, t, h, v, a):
        self.plotPanel.draw([[t,h],[t,v],[t,a]])

    def plotEvent(self, event):
        self.plotPanel.plotEvent(event)

    def onFileChanged( self, event ):
        filename = self.filePicker.GetPath()
        #self.isFileValid(filename)

    def isFileValid(self, filename):
        if filename == "":
            dlg = wx.MessageDialog(self, "Por favor, selecione um arquivo de trajetória.", "Erro", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            return False
        try:
            data = FlightDataImporter.importData(filename)
            return True
        except:
            dlg = wx.MessageDialog(self, "Falha ao carregar arquivo.", "Erro", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            return False

    def onBtnStartStopSimulation( self, event ):
        if self.parent.rRocketModel.state == rRocketState["Ready"]:
            filename = self.filePicker.GetPath()
            if self.isFileValid(filename):
                self.parent.rRocketModel.startSimulationMode(filename)    
                self.plotPanel.clearEvents()    
        else:
            self.parent.rRocketModel.stopSimulationMode()

    def onBtnReport( self, event ):
        log = self.parent.getFlightSimulationReport()
        reportFrm = ReportFrame(self)
        reportFrm.setText(log)
        reportFrm.Show() 

    def setDisconnectedAppearance(self):
        self.btnStartStopSimulation.SetLabel("Iniciar simulação")
        self.btnStartStopSimulation.Enable(False)
        self.btnReport.Enable(False)

    def setReadyAppearance(self):
        self.btnStartStopSimulation.SetLabel("Iniciar simulação")
        self.btnStartStopSimulation.Enable(True)
        self.btnReport.Enable(True)

    def setInitializingAppearance(self):
        self.btnStartStopSimulation.SetLabel("Iniciar simulação")
        self.btnStartStopSimulation.Enable(False)
        self.btnReport.Enable(True)

    def setSimulatingAppearance(self):
        self.btnStartStopSimulation.SetLabel("Parar simulação")
        self.btnStartStopSimulation.Enable(True)
        self.btnReport.Enable(False)

    def setBusyForDataTransferAppearance(self):
        self.btnStartStopSimulation.SetLabel("Iniciar simulação")
        self.btnStartStopSimulation.Enable(False)
        self.btnReport.Enable(False)

