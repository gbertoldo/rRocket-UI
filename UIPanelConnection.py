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
import wxpserial
import bitmaptools
from UIModelessDialog import *

class PanelConnection(UITemplate.PanelConnection):
    def __init__(self, parent):
        UITemplate.PanelConnection.__init__(self,parent)
        self.parent = parent
        self.figLogo =bitmaptools.scale_bitmap(wx.Bitmap(  bitmaptools.resource_path(u"fig/rRocket.png"), wx.BITMAP_TYPE_ANY ), 200, 200)
        self.figDisconnected = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/disconnected.png"), wx.BITMAP_TYPE_ANY ), 25, 25)
        self.figConnected = bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/connected.png"), wx.BITMAP_TYPE_ANY ), 25, 25)
        self.figReload =bitmaptools.scale_bitmap(wx.Bitmap( bitmaptools.resource_path(u"fig/reload.png"), wx.BITMAP_TYPE_ANY ), 20, 20)
        self.bmpRRocketLogo.SetBitmap(self.figLogo)
        self.btnReload.SetBitmap(self.figReload)
        self.updateSerialPortList()

    def onBtnReload( self, event ):
        self.updateSerialPortList()

    def onBtnConnectDisconnect( self, event ):
        if self.parent.rRocketModel is None:
            self.connect()
        else:
            if self.parent.rRocketModel.isOpen():
                self.disconnect()
            else:
                self.connect()
    
    def connect(self):
        port = self.choiceSerialPorts.GetStringSelection()
        self.parent.serialParameters.port = port
        self.parent.rRocketModel.start(serialParameters = self.parent.serialParameters)
        dialog = wxpserial.wxPSerialConnectionProgressDialog(self, "Conectando...", self.parent.rRocketModel, maxMillis=10000)
        dialog.ShowModal()

        if self.parent.rRocketModel.isOpen():
            self.parent.rRocketModelStateUpdate()
        else:
            self.parent.setDisconnectedAppearance()
            wx.MessageBox("Falha na conexão.", "Estado da conexão", wx.OK | wx.ICON_ERROR)
            
    def disconnect(self):
        if self.parent.rRocketModel.isOpen():
            self.parent.rRocketModel.stop()  

    def updateSerialPortList(self):
        ports = wxpserial.availableSerialPorts()
        self.choiceSerialPorts.Clear()
        for p in ports:
            self.choiceSerialPorts.Append(p)

    def setDisconnectedAppearance(self):
        self.bmpConnectionStatus.SetBitmap(self.figDisconnected)
        self.btnConnectDisconnect.SetLabel("Conectar")
        self.choiceSerialPorts.Enable(True)
        self.btnReload.Enable(True)
        self.bmpConnectionStatus.SetBitmap(self.figDisconnected)

    def setReadyAppearance(self):
        self.bmpConnectionStatus.SetBitmap(self.figConnected)
        self.btnConnectDisconnect.SetLabel("Desconectar")
        self.choiceSerialPorts.Enable(False)
        self.btnReload.Enable(False)
        self.bmpConnectionStatus.SetBitmap(self.figConnected)

    def setInitializingAppearance(self):
        self.setReadyAppearance()

    def setSimulatingAppearance(self):
        self.setReadyAppearance()

    def setBusyForDataTransferAppearance(self):
        self.setReadyAppearance()

