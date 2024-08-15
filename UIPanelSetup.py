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
from UIReportFrame import *

class PanelSetup(UITemplate.PanelSetup):
 
    def __init__(self, parent):
        UITemplate.PanelSetup.__init__(self,parent)
        self.parent = parent
        self.listOfParameters = self.parent.rRocketModel.listOfParameters
        self.createPanelParameters()
        self.btnRestoreFactoryParameters.SetBackgroundColour(wx.Colour(wx.RED))
      
    def createPanelParameters(self):
        self.listOfWidgets = []
        bSizer17 = wx.BoxSizer( wx.VERTICAL )
        self.panelParameters = wx.Panel( self.panelBase, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.m_staticText20 = wx.StaticText( self.panelParameters, wx.ID_ANY, u"Parâmetro", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        fgSizer2.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        self.m_staticText21 = wx.StaticText( self.panelParameters, wx.ID_ANY, u"Valor gravado", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        fgSizer2.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_staticText22 = wx.StaticText( self.panelParameters, wx.ID_ANY, u"Valor desejado", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        self.m_staticText22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        fgSizer2.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        for par in self.listOfParameters:
            txtDescription = wx.StaticText( self.panelParameters, wx.ID_ANY, par.description, wx.DefaultPosition, wx.DefaultSize, 0 )
            txtDescription.Wrap( -1 )
            fgSizer2.Add( txtDescription, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
            fmt = "%7."+str(par.digits)+"f"
            txtRecordedValue = wx.StaticText( self.panelParameters, wx.ID_ANY, fmt%(par.recordedValue), wx.DefaultPosition, wx.DefaultSize, 0 )
            txtRecordedValue.Wrap( -1 )
            fgSizer2.Add( txtRecordedValue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
            spinCtrlDoubleDesiredValue = wx.SpinCtrlDouble( self.panelParameters, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, par.minValue, par.maxValue, par.initialValue, par.increment )
            spinCtrlDoubleDesiredValue.SetDigits( par.digits )
            fgSizer2.Add( spinCtrlDoubleDesiredValue, 0, wx.ALL|wx.EXPAND, 5 )
            self.listOfWidgets.append({"name":par.name, "recordedValue":txtRecordedValue, "desiredValue":spinCtrlDoubleDesiredValue})
        self.panelParameters.SetSizer( fgSizer2 )
        self.panelParameters.Layout()
        fgSizer2.Fit( self.panelParameters )
        bSizer17.Add( self.panelParameters, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        self.panelBase.SetSizer( bSizer17 )
        self.panelBase.Layout()
        bSizer17.Fit( self.panelBase )
        self.Layout()

    def confirmMemoryErase(self):
        dlg = wx.MessageDialog(self, "O procedimento apagará a memória do último voo. Confirma?", "Confirmar limpeza de memória de voo", wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            return True
        else:
            return False
        
    def getDesiredValuesFromForm(self):
        for par in self.listOfParameters:
            widget = None
            for w in self.listOfWidgets:
                if w["name"] == par.name:
                    widget = w
                    break
            par.desiredValue = widget["desiredValue"].GetValue()
        pass

    def setRecordedValuesToForm(self):
        for par in self.listOfParameters:
            widget = None
            for w in self.listOfWidgets:
                if w["name"] == par.name:
                    widget = w
                    break
            fmt = "%7."+str(par.digits)+"f"
            widget["recordedValue"].SetLabel(fmt%(par.recordedValue))
            par.desiredValue = par.recordedValue
            widget["desiredValue"].SetValue(par.desiredValue)

    def onBtnRestoreFactoryParameters( self, event ):
        if self.confirmMemoryErase():
            self.parent.rRocketModel.resetToFactoryParameters()

    def onBtnReadParameters( self, event ):
        self.parent.rRocketModel.readStaticParameters()
        self.parent.rRocketModel.readDynamicParameters()

    def onBtnParametersReport(self, event):
        log = self.parent.rRocketModel.parametersReport()
        reportFrm = ReportFrame(self)
        reportFrm.setText(log)
        reportFrm.Show() 
    
    def onBtnWriteParameters( self, event ):
        if self.confirmMemoryErase():
            self.getDesiredValuesFromForm()
            self.parent.rRocketModel.writeDynamicParameters()

    def setDisconnectedAppearance(self):
        self.txtFirmwareVersion.SetLabel("Versão de firmware: --- ")
        self.btnRestoreFactoryParameters.Enable(False)
        self.btnReadParameters.Enable(False)
        self.btnWriteParameters.Enable(False)
        self.btnParametersReport.Enable(False)

    def setReadyAppearance(self):
        self.txtFirmwareVersion.SetLabel("Versão de firmware: "+self.parent.rRocketModel.firmwareVersion)
        self.btnRestoreFactoryParameters.Enable(True)
        self.btnReadParameters.Enable(True)
        self.btnWriteParameters.Enable(True)
        self.btnParametersReport.Enable(True)

    def setInitializingAppearance(self):
        self.txtFirmwareVersion.SetLabel("Versão de firmware: ---")
        self.btnRestoreFactoryParameters.Enable(True)
        self.btnReadParameters.Enable(False)
        self.btnWriteParameters.Enable(False)
        self.btnParametersReport.Enable(False)

    def setSimulatingAppearance(self):
        self.txtFirmwareVersion.SetLabel("Versão de firmware: "+self.parent.rRocketModel.firmwareVersion)
        self.btnRestoreFactoryParameters.Enable(False)
        self.btnReadParameters.Enable(False)
        self.btnWriteParameters.Enable(False)
        self.btnParametersReport.Enable(False)

    def setBusyForDataTransferAppearance(self):
        self.txtFirmwareVersion.SetLabel("Versão de firmware: "+self.parent.rRocketModel.firmwareVersion)
        self.btnRestoreFactoryParameters.Enable(True)
        self.btnReadParameters.Enable(False)
        self.btnWriteParameters.Enable(False)
        self.btnParametersReport.Enable(False)

