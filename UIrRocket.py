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
import os
import bitmaptools
import wx.adv
import wxpserial
from datetime import datetime

import UITemplate
from UIReportFrame import *
from UIPanelConnection import *
from UIPanelSetup import *
from UIFlightStatisticsSetup import *
from UIPanelMemory import *
from UIPanelSimulation import *
from UIPanelStatistics import *
from UIModelessDialog import *

from rRocketModel import *

APP_VERSION_STRING="v.1.1.0"

def onLinux() -> bool:
	if os.name == 'posix':
		return True
	return False

class rRocketUIListbook(wx.Listbook):
    """
    Listbook class
    """
    def __init__(self, parent, statusBar):
        """
        Constructor
        """
        wx.Listbook.__init__(self, parent, wx.ID_ANY, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             )
        
        self.statusBar = statusBar

        # make an image list using the LBXX images
        toolsize = 50
        il = wx.ImageList(toolsize, toolsize)
        
        fig1 = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/usb-cable-icon.png"), wx.BITMAP_TYPE_ANY ), toolsize, toolsize)
        fig2 = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/setting-line-icon.png"), wx.BITMAP_TYPE_ANY ), toolsize, toolsize)
        fig3 = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/chip-memory-icon.png"), wx.BITMAP_TYPE_ANY ), toolsize, toolsize)
        fig4 = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/metaverse-virtual-reality-icon.png"), wx.BITMAP_TYPE_ANY ), toolsize, toolsize)
        fig5 = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/chart-arrow-up-icon.png"), wx.BITMAP_TYPE_ANY ), toolsize, toolsize)
        il.Add(fig1)
        il.Add(fig2)
        il.Add(fig3)
        il.Add(fig4)
        il.Add(fig5)
        self.AssignImageList(il)

        self.serialParameters = wxpserial.SerialParameters(port=None
            , baudrate=115200
            , bytesize=8
            , parity=wxpserial.serial.PARITY_NONE
            , stopbits=wxpserial.serial.STOPBITS_ONE
            , timeout=0.05
            , xonxoff=False
            , rtscts=False
            , write_timeout=0.05
            , dsrdtr=False
            , inter_byte_timeout=None
            , exclusive=True)
        
        self.rRocketModel = rRocketModel(self)
        self.panelConnection = PanelConnection(self)
        self.panelSetup = PanelSetup(self)
        self.panelMemory = PanelMemory(self)
        self.panelSimulation = PanelSimulation(self)
        self.panelStatistics = PanelStatistics(self, APP_VERSION_STRING)

        pages = [(self.panelConnection, "Conexão"),
                 (self.panelSetup, "Configuração"),
                 (self.panelMemory, "Memória de voo"),
                 (self.panelSimulation, "Simulação"),
                 (self.panelStatistics, "Estatística")]
        imID = 0
        for page, label in pages:
            self.AddPage(page, label, imageId=imID)
            imID += 1
        self.setDisconnectedAppearance()


    def isFirmwareVersionCompatible(self,version):
        decomposedVersion = version.strip().split(".")
        try:
            if (int(decomposedVersion[0]) == 1) and (int(decomposedVersion[1]) == 6):
                return True
            else:
                return False
        except:
            return False

    def rRocketModelStateUpdate(self):
        state = self.rRocketModel.state
        if state == rRocketState["Disconnected"]:
            self.setDisconnectedAppearance()
        elif state == rRocketState["Ready"]:
            self.setReadyAppearance()   
        elif state == rRocketState["Simulating"]:
            self.setSimulatingAppearance()
        elif state == rRocketState["BusyForDataTransfer"]:
            self.setBusyForDataTransferAppearance()
        elif state == rRocketState["Initializing"]:
            self.setInitializingAppearance()
        else:
            self.rRocketModel.stop()
            wx.MessageBox(self, "Altímetro em estado desconhecido. Conexão fechada.", "Erro", wx.OK | wx.ICON_ERROR)

    def rRocketModelParameterUpdate(self):
        self.panelSetup.setRecordedValuesToForm()

    def rRocketModelFlightUpdate(self):
        t=self.rRocketModel.flightAltitudeLogger.t
        h=self.rRocketModel.flightAltitudeLogger.h
        if len(t) > 0:
            self.panelMemory.plotH([t,h])
        else:
            self.panelMemory.plotEmpty()

    def rRocketModelFlightEventUpdate(self, evt):
        self.panelMemory.plotEvent(evt)

    def rRocketModelMessagesUpdate(self, msgs):
        messages = ""
        for msg in msgs:
            messages = messages + "- " + str(msg) + "\n"
        mbox = ModelessDialog(self, "Mensagem", messages, delayMS=5000)
        mbox.Show()
        
    def rRocketModelErrorsUpdate(self, msgs):
        errors = ""
        for msg in msgs:
            errors = errors + "- "+str(msg)+"\n"
        mbox = ModelessDialog(self, "Erro", errors, delayMS=5000)
        mbox.Show()

    def rRocketModelSimulationUpdate(self):
        t=self.rRocketModel.flightSimulationLogger.t
        h=self.rRocketModel.flightSimulationLogger.h
        v=self.rRocketModel.flightSimulationLogger.v
        a=self.rRocketModel.flightSimulationLogger.a
        self.panelSimulation.plot(t, h, v, a)

    def rRocketModelSimulationFlightEventUpdate(self, event):
        self.panelSimulation.plotEvent(event)

    def rRocketModelFinishedReceivingMemoryReportUpdate(self):
        if len(self.rRocketModel.flightAltitudeLogger.t) < 1:
            self.panelMemory.plotEmpty()
            self.panelMemory.clearEvents()
            mbox = ModelessDialog(self, "Estado da memória de voo", "Memória de voo vazia.", delayMS=5000)
            mbox.Show()
        else:
            self.rRocketModelFlightUpdate()

    def getFlightReport(self,cmt="# ",eol="\r\n"):
        log = []
        log.append("RELATÓRIO DE VOO   - "+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        log.append("")
        log.append("")
        log.append("rRocket-UI "+APP_VERSION_STRING)

        txt = ""
        for line in log:
            txt = txt + cmt + line + eol

        txt = txt + self.rRocketModel.flightReport()        
        return txt

    def getFlightSimulationReport(self,cmt="# ",eol="\r\n"):
        log = []
        log.append("RELATÓRIO DE SIMULAÇÃO DE VOO   - "+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        log.append("")
        log.append("")
        log.append("rRocket-UI "+APP_VERSION_STRING)

        txt = ""
        for line in log:
            txt = txt + cmt + line + eol
        txt = txt + self.rRocketModel.flightSimulationReport()        
        return txt

    def setDisconnectedAppearance(self):
        self.panelConnection.setDisconnectedAppearance()
        self.panelSetup.setDisconnectedAppearance()
        self.panelMemory.setDisconnectedAppearance()
        self.panelSimulation.setDisconnectedAppearance()
        self.statusBar.SetStatusText("Altímetro desconectado")

    def setReadyAppearance(self):
        self.panelConnection.setReadyAppearance()
        self.panelSetup.setReadyAppearance()
        self.panelMemory.setReadyAppearance()
        self.panelSimulation.setReadyAppearance()
        self.statusBar.SetStatusText("")

    def setInitializingAppearance(self):
        self.panelConnection.setInitializingAppearance()
        self.panelSetup.setInitializingAppearance()
        self.panelMemory.setInitializingAppearance()
        self.panelSimulation.setInitializingAppearance()
        self.statusBar.SetStatusText("Altímetro em processo de inicialização... Por favor, aguarde.")

    def setSimulatingAppearance(self):
        self.panelConnection.setSimulatingAppearance()
        self.panelSetup.setSimulatingAppearance()
        self.panelMemory.setSimulatingAppearance()
        self.panelSimulation.setSimulatingAppearance()
        self.statusBar.SetStatusText("Simulando voo...")

    def setBusyForDataTransferAppearance(self):
        self.panelConnection.setBusyForDataTransferAppearance()
        self.panelSetup.setBusyForDataTransferAppearance()
        self.panelMemory.setBusyForDataTransferAppearance()
        self.panelSimulation.setBusyForDataTransferAppearance()
        self.statusBar.SetStatusText("Altímetro ocupado para transferência de dados... Por favor, aguarde.")


class MainFrame(UITemplate.MainFrame):
    def __init__(self, parent):
        UITemplate.MainFrame.__init__(self,parent)

        notebook = rRocketUIListbook(self.basePanel, self.statusBar)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND, 5)
        self.basePanel.SetSizer(sizer)

        self.Layout()
        sizer.Fit(self.basePanel)

    def onMenuItemClose( self, event ):
        self.Close()

    def onMenuItemAbout( self, event ):
        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetName("rRocket-UI")
        aboutInfo.SetIcon(wx.Icon(bitmaptools.resource_path("./fig/rRocket.ico"), desiredWidth=1))
        aboutInfo.SetVersion(APP_VERSION_STRING)
        aboutInfo.SetDescription("Interface Gráfica para altímetros rRocket")
        aboutInfo.SetCopyright("(C) 2024 - Universidade Tecnológica Federal do Paraná")
        #aboutInfo.SetWebSite("http:#myapp.org")
        aboutInfo.AddDeveloper("Guilherme Bertoldo")
        aboutInfo.AddArtist("Guilherme Bertoldo")
        aboutInfo.AddArtist("uxwing.com")

        wx.adv.AboutBox(aboutInfo)