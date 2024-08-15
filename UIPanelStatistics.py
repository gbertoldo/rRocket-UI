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
import UIFlightStatisticsSetup
import FlightStatisticsMovingAverage
import FlightStatisticsKalmanAlfaFilter
from datetime import datetime
import os


def getFlightEvents(filename):
  lines = []
  events = []
  strF=" s: Voo detectado"
  strD=" s: Drogue acionado"
  strP=" s: Paraquedas principal acionado"
  strL=" s: Aterrissagem detectada"
  with open(filename,'r') as  fp:
    lines = fp.readlines()
  
  for line in lines:
    if strF in line:
      line = line.replace(strF,"")
      line = line.replace("#","")
      events.append([float(line),0,0,0,"F"])
    elif strD in line:
      line = line.replace(strD,"")
      line = line.replace("#","")
      events.append([float(line),0,0,0,"D"])
    elif strP in line:
      line = line.replace(strP,"")
      line = line.replace("#","")
      events.append([float(line),0,0,0,"P"])
    elif strL in line:
      line = line.replace(strL,"")
      line = line.replace("#","")
      events.append([float(line),0,0,0,"L"])
  return events

class PanelStatistics(UITemplate.PanelStatistics):
    def __init__(self, parent, appversion):
        UITemplate.PanelStatistics.__init__(self, parent)
        self.parent = parent
        self.appversion = appversion
        # Plot panel
        self.plotPanel = UIPlot.rRocketPlot( self.panelBase, ["-*","-x","-o","-P"], 10,100, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.plotPanel.setXLabel("t (s)")
        self.plotPanel.setYLabel("")
        self.plotPanel.setTitle("")
        self.plotPanel.setLegend(["Altura bruta (m)", "Velocidade (m/s)", "Aceleração (m/s²)", "Altura filtrada (m)"])
        self.plotPanel.setGrid()
        self.plotPanel.addToolbar()

        self.inputFileFormat = UIInputFileFormatFrame.InputFileFormat()
        self.tmpFolder="tmp"
        self.statfilename=self.tmpFolder+"/"+"rRocketStatFile.txt"
        #self.flightStatistics = FlightStatisticsMovingAverage.FlightStatisticsMovingAverage()
        self.flightStatistics = FlightStatisticsKalmanAlfaFilter.FlightStatisticsKalmanAlfaFilter()

    def plot(self, t, h, v, a, hf):
        self.plotPanel.draw([[t,h],[t,v],[t,a],[t,hf]])

    def plotEvent(self, event):
        self.plotPanel.plotEvent(event)

    def onBtnSetTitle( self, event ):
        txt = self.txtCtrlPlotTitle.GetValue()
        self.plotPanel.setTitle(txt)
 
    def onFileChanged( self, event ):
        filename = self.filePicker.GetPath()

    def isFileValid(self, filename):
        if filename == "":
            dlg = ModelessDialog(self, "Erro", "Por favor, selecione um arquivo de trajetória.", delayMS=5000)
            dlg.Show()
            return False
        try:
            ifile=filename
            ofile=self.statfilename

            # Creating tmp directory, if not exist yet
            os.makedirs(self.tmpFolder, exist_ok = True)

            events = getFlightEvents(filename)
            for evt in events:
                self.plotEvent(evt)

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
            
            self.flightStatistics.calculate(data[0],data[1])
            [t,h]=self.flightStatistics.getAltitudeVector()
            [t,v]=self.flightStatistics.getVelocityVector()
            [t,a]=self.flightStatistics.getAccelerationVector()
            [t,hf]=self.flightStatistics.getFilteredAltitudeVector()

            self.plot(t, h, v, a, hf)
            return True
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
            dlg = ModelessDialog(self, "Erro", "Falha ao carregar arquivo.\n", delayMS=5000)
            dlg.Show()
            return False
        
    def onButtonSetupInputFileFormat(self, event):
        frm = UIInputFileFormatFrame.InputFileFormatFrame(self, self.inputFileFormat)
        frm.Show()

    def setInputFileFormat(self, fmt):
        self.inputFileFormat = fmt

    def onBtnSetup( self, event ):
        frm = UIFlightStatisticsSetup.FlightStatisticsSetup(self, self.flightStatistics)
        frm.Show()

    def setupFlightStatistics(self, stat):
        self.flightStatistics = stat

    def onBtnCalculate( self, event ):
        filename = self.filePicker.GetPath()
        if self.isFileValid(filename):
            self.plotPanel.clearEvents()    
        
    def onBtnReport( self, event ):
        if len(self.flightStatistics.t) > 0:
            log = []
            log.append("RELATÓRIO DE ESTATÍSTICA DE VOO   - "+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            log.append("")
            log.append("")
            log.append("rRocket-UI "+self.appversion)
            log.append("")
            log.append("Arquivo de entrada: "+self.filePicker.GetPath())
            log.append("")

            txt=""
            cmt="# "
            eol="\r\n"
            for line in log:
                txt = txt + cmt + line + eol

            txt = txt + self.flightStatistics.report()
            reportFrm = ReportFrame(self)
            reportFrm.setText(txt)
            reportFrm.Show() 
        else:
            dlg = ModelessDialog(self, "Erro", "Sem dados para gerar relatório.", delayMS=5000)
            dlg.Show()
            return False

    def setDisconnectedAppearance(self):
        self.btnCalculate.Enable(True)
        self.btnSetup.Enable(True)
        self.btnReport.Enable(True)

    def setReadyAppearance(self):
        self.btnCalculate.Enable(True)
        self.btnSetup.Enable(True)
        self.btnReport.Enable(True)

    def setInitializingAppearance(self):
        self.btnCalculate.Enable(True)
        self.btnSetup.Enable(True)
        self.btnReport.Enable(True)

    def setSimulatingAppearance(self):
        self.btnCalculate.Enable(True)
        self.btnSetup.Enable(True)
        self.btnReport.Enable(True)

    def setBusyForDataTransferAppearance(self):
        self.btnCalculate.Enable(True)
        self.btnSetup.Enable(True)
        self.btnReport.Enable(True)

