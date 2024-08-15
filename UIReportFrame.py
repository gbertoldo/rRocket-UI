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

class ReportFrame(UITemplate.ReportFrame):
    def __init__(self, parent):
        UITemplate.ReportFrame.__init__(self, parent)
        self.clear()
    
    def clear(self):
        self.txtCtrlLog.Clear()

    def setText(self, txt):
        self.txtCtrlLog.AppendText(txt)
        self.txtCtrlLog.SetInsertionPoint(0)

    def onBtnCancel( self, event ):
        self.Destroy()

    def onBtnSave( self, event ):
        with wx.FileDialog(self, "Salvar relatório", wildcard="Arquivos txt (*.txt)|*.txt",
                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w', encoding='utf-8') as file:
                    txt = self.txtCtrlLog.GetValue()
                    file.write(txt)
            except IOError:
                wx.LogError("Erro ao salvar '%s'." % pathname)
