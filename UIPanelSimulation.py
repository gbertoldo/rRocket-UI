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
from UIModelessDialog import *
import UIInputFileFormatFrame
import os

class PanelSimulation(UITemplate.PanelSimulation):
    def __init__(self, parent):
        UITemplate.PanelSimulation.__init__(self, parent)
        self.parent = parent
        # Plot panel
        self.plotPanel = UIPlot.rRocketPlot( self.panelBase, ["-*","-x","-o"], 10,100, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.plotPanel.setXLabel("t (s)")
        self.plotPanel.setYLabel("")
        self.plotPanel.setTitle("")
        self.plotPanel.setLegend(["Altura (m)", "Velocidade (m/s)", "Aceleração (m/s²)"])
        self.plotPanel.setGrid()
        self.plotPanel.addToolbar()

        self.inputFileFormat = UIInputFileFormatFrame.InputFileFormat()
        self.tmpFolder="tmp"
        self.simfilename=self.tmpFolder+"/"+"rRocketSimFile.txt"

    def plot(self, t, h, v, a):
        self.plotPanel.draw([[t,h],[t,v],[t,a]])

    def plotEvent(self, event):
        self.plotPanel.plotEvent(event)

    def onBtnSetTitle( self, event ):
        txt = self.txtCtrlPlotTitle.GetValue()
        self.plotPanel.setTitle(txt)
 
    def onFileChanged( self, event ):
        filename = self.filePicker.GetPath()
        #self.isFileValid(filename)

    def isFileValid(self, filename):
        if filename == "":
            dlg = ModelessDialog(self, "Erro", "Por favor, selecione um arquivo de trajetória.", delayMS=5000)
            dlg.Show()
            return False
        try:
            ifile=filename
            ofile=self.simfilename
            # Creating tmp directory, if not exist yet
            os.makedirs(self.tmpFolder, exist_ok = True)

            FlightDataImporter.removeHeaderLinesFromFile(ifile,ofile,self.inputFileFormat.headerLines)
            if self.inputFileFormat.fieldSeparator == "," and self.inputFileFormat.decimalSeparator==",":
                FS = ";"
                FlightDataImporter.replaceStrInFile(ofile,ofile,", ",FS)
            else:
                FS = self.inputFileFormat.fieldSeparator
                      
            if self.inputFileFormat.decimalSeparator == ",":
                FlightDataImporter.replaceStrInFile(ofile,ofile,",",".")

            tCol = self.inputFileFormat.tCol-1
            hCol = self.inputFileFormat.hCol-1
            data = FlightDataImporter.importData(ofile,cols=[tCol,hCol],sep=FS, engine="python",comment=self.inputFileFormat.comment)
            
            # Converts the altitude unit to meter
            data[1] = data[1] * self.inputFileFormat.hUnit
            
            with open(ofile, 'w') as fp:
                for i in range(0,len(data[0])):
                    fp.write(("%14.7f %14.7f\n")%(data[0][i],data[1][i]))
            return True
        except:
            dlg = ModelessDialog(self, "Erro", "Falha ao carregar arquivo.", delayMS=5000)
            dlg.Show()
            return False
        
    def onButtonSetupInputFileFormat(self, event):
        frm = UIInputFileFormatFrame.InputFileFormatFrame(self, self.inputFileFormat)
        frm.Show()

    def setInputFileFormat(self, fmt):
        self.inputFileFormat = fmt

    def onBtnStartStopSimulation( self, event ):
        if self.parent.rRocketModel.state == rRocketState["Ready"]:
            filename = self.filePicker.GetPath()
            if self.isFileValid(filename):
                self.parent.rRocketModel.startSimulationMode(filename, self.simfilename)    
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

