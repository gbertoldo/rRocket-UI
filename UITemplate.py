# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"rRocket-UI", pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 900,600 ), wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.basePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1.Add( self.basePanel, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.menuFile = wx.Menu()
        self.menuItemClose = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Fechar", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemClose )

        self.m_menubar1.Append( self.menuFile, u"Arquivo" )

        self.menuHelp = wx.Menu()
        self.menuItemAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"Sobre", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuHelp.Append( self.menuItemAbout )

        self.m_menubar1.Append( self.menuHelp, u"Ajuda" )

        self.SetMenuBar( self.m_menubar1 )

        self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onMenuItemClose, id = self.menuItemClose.GetId() )
        self.Bind( wx.EVT_MENU, self.onMenuItemAbout, id = self.menuItemAbout.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onMenuItemClose( self, event ):
        event.Skip()

    def onMenuItemAbout( self, event ):
        event.Skip()


###########################################################################
## Class PanelConnection
###########################################################################

class PanelConnection ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.bmpRRocketLogo = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.bmpRRocketLogo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText19 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"SISTEMA DE RECUPERAÇÃO DE FOGUETES", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        self.m_staticText19.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer8.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer8.Add( ( 0, 50), 0, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.bmpConnectionStatus = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.bmpConnectionStatus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        choiceSerialPortsChoices = []
        self.choiceSerialPorts = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceSerialPortsChoices, 0 )
        self.choiceSerialPorts.SetSelection( 0 )
        bSizer9.Add( self.choiceSerialPorts, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnReload = wx.BitmapButton( self.m_panel3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
        bSizer9.Add( self.btnReload, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer8.Add( bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.btnConnectDisconnect = wx.Button( self.m_panel3, wx.ID_ANY, u"Conectar", wx.DefaultPosition, wx.Size( 200,60 ), 0 )
        self.btnConnectDisconnect.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer8.Add( self.btnConnectDisconnect, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer8 )
        self.m_panel3.Layout()
        bSizer8.Fit( self.m_panel3 )
        bSizer4.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        # Connect Events
        self.btnReload.Bind( wx.EVT_BUTTON, self.onBtnReload )
        self.btnConnectDisconnect.Bind( wx.EVT_BUTTON, self.onBtnConnectDisconnect )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnReload( self, event ):
        event.Skip()

    def onBtnConnectDisconnect( self, event ):
        event.Skip()


###########################################################################
## Class PanelSetup
###########################################################################

class PanelSetup ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"PARÂMETROS DE VOO", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer16.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txtFirmwareVersion = wx.StaticText( self, wx.ID_ANY, u"Versão de firmware", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtFirmwareVersion.Wrap( -1 )

        bSizer16.Add( self.txtFirmwareVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.panelBase = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer16.Add( self.panelBase, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.btnReadParameters = wx.Button( self, wx.ID_ANY, u"Ler parâmetros", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnReadParameters.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gSizer1.Add( self.btnReadParameters, 0, wx.ALL|wx.EXPAND, 5 )

        self.btnParametersReport = wx.Button( self, wx.ID_ANY, u"Relatório de parâmetros", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
        self.btnParametersReport.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gSizer1.Add( self.btnParametersReport, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.btnRestoreFactoryParameters = wx.Button( self, wx.ID_ANY, u"Restaurar parâmetros originais", wx.DefaultPosition, wx.Size( 300,40 ), 0 )
        self.btnRestoreFactoryParameters.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gSizer1.Add( self.btnRestoreFactoryParameters, 0, wx.ALL|wx.EXPAND, 5 )

        self.btnWriteParameters = wx.Button( self, wx.ID_ANY, u"Gravar parâmetros", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnWriteParameters.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        gSizer1.Add( self.btnWriteParameters, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer16.Add( gSizer1, 0, wx.EXPAND, 5 )


        bSizer13.Add( bSizer16, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer13 )
        self.Layout()

        # Connect Events
        self.btnReadParameters.Bind( wx.EVT_BUTTON, self.onBtnReadParameters )
        self.btnParametersReport.Bind( wx.EVT_BUTTON, self.onBtnParametersReport )
        self.btnRestoreFactoryParameters.Bind( wx.EVT_BUTTON, self.onBtnRestoreFactoryParameters )
        self.btnWriteParameters.Bind( wx.EVT_BUTTON, self.onBtnWriteParameters )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnReadParameters( self, event ):
        event.Skip()

    def onBtnParametersReport( self, event ):
        event.Skip()

    def onBtnRestoreFactoryParameters( self, event ):
        event.Skip()

    def onBtnWriteParameters( self, event ):
        event.Skip()


###########################################################################
## Class PanelMemory
###########################################################################

class PanelMemory ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.panelBase = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15.Add( self.panelBase, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnSetupFlightStatistics = wx.Button( self, wx.ID_ANY, u"Configurar ", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnSetupFlightStatistics.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer16.Add( self.btnSetupFlightStatistics, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnReadMemory = wx.Button( self, wx.ID_ANY, u"Ler memória", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnReadMemory.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer16.Add( self.btnReadMemory, 0, wx.ALL, 5 )

        self.btnFlightReport = wx.Button( self, wx.ID_ANY, u"Relatório de voo", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnFlightReport.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer16.Add( self.btnFlightReport, 0, wx.ALL, 5 )


        bSizer16.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.btnClearMemory = wx.Button( self, wx.ID_ANY, u"Limpar memória", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnClearMemory.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer16.Add( self.btnClearMemory, 0, wx.ALL, 5 )


        bSizer15.Add( bSizer16, 0, wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()

        # Connect Events
        self.btnSetupFlightStatistics.Bind( wx.EVT_BUTTON, self.onBtnSetupFlightStatistics )
        self.btnReadMemory.Bind( wx.EVT_BUTTON, self.onBtnReadMemory )
        self.btnFlightReport.Bind( wx.EVT_BUTTON, self.onBtnFlightReport )
        self.btnClearMemory.Bind( wx.EVT_BUTTON, self.onBtnClearMemory )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnSetupFlightStatistics( self, event ):
        event.Skip()

    def onBtnReadMemory( self, event ):
        event.Skip()

    def onBtnFlightReport( self, event ):
        event.Skip()

    def onBtnClearMemory( self, event ):
        event.Skip()


###########################################################################
## Class PanelSimulation
###########################################################################

class PanelSimulation ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.panelBase = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10.Add( self.panelBase, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer10.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Selecione um arquivo de trajetória", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer12.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer12.Add( self.filePicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnStartStopSimulation = wx.Button( self, wx.ID_ANY, u"Iniciar simulação", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnStartStopSimulation.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer13.Add( self.btnStartStopSimulation, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer13.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.btnReport = wx.Button( self, wx.ID_ANY, u"Gerar relatório", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnReport.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer13.Add( self.btnReport, 0, wx.ALL, 5 )


        bSizer10.Add( bSizer13, 0, wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        # Connect Events
        self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.onFileChanged )
        self.btnStartStopSimulation.Bind( wx.EVT_BUTTON, self.onBtnStartStopSimulation )
        self.btnReport.Bind( wx.EVT_BUTTON, self.onBtnReport )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onFileChanged( self, event ):
        event.Skip()

    def onBtnStartStopSimulation( self, event ):
        event.Skip()

    def onBtnReport( self, event ):
        event.Skip()


###########################################################################
## Class ReportFrame
###########################################################################

class ReportFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.txtCtrlLog = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer15.Add( self.txtCtrlLog, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnCancel = wx.Button( self.m_panel5, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.btnCancel, 0, wx.ALL, 5 )

        self.btnSave = wx.Button( self.m_panel5, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.btnSave, 0, wx.ALL, 5 )


        bSizer15.Add( bSizer16, 0, wx.ALIGN_RIGHT, 5 )


        self.m_panel5.SetSizer( bSizer15 )
        self.m_panel5.Layout()
        bSizer15.Fit( self.m_panel5 )
        bSizer14.Add( self.m_panel5, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnCancel.Bind( wx.EVT_BUTTON, self.onBtnCancel )
        self.btnSave.Bind( wx.EVT_BUTTON, self.onBtnSave )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnCancel( self, event ):
        event.Skip()

    def onBtnSave( self, event ):
        event.Skip()


###########################################################################
## Class FlightStatisticsFrame
###########################################################################

class FlightStatisticsFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configurar parâmetros para cálculo de velocidade e de aceleração ", pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText5 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Parâmetro m", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoublem = wx.SpinCtrlDouble( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 3, 1 )
        self.spinCtrlDoublem.SetDigits( 0 )
        fgSizer1.Add( self.spinCtrlDoublem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText6 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Parâmetro n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoublen = wx.SpinCtrlDouble( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 3, 1 )
        self.spinCtrlDoublen.SetDigits( 0 )
        fgSizer1.Add( self.spinCtrlDoublen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText7 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Partição de tempo (delta t) (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoubledt = wx.SpinCtrlDouble( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.05, 0.25, 0.1, 0.05 )
        self.spinCtrlDoubledt.SetDigits( 3 )
        fgSizer1.Add( self.spinCtrlDoubledt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer19.Add( fgSizer1, 0, wx.EXPAND, 5 )

        self.txtDescription = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer19.Add( self.txtDescription, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer16.Add( bSizer19, 1, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnCancel = wx.Button( self.m_panel7, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.btnCancel, 0, wx.ALL, 5 )

        self.btnConfirm = wx.Button( self.m_panel7, wx.ID_ANY, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.btnConfirm, 0, wx.ALL, 5 )


        bSizer16.Add( bSizer18, 0, wx.ALIGN_RIGHT, 5 )


        self.m_panel7.SetSizer( bSizer16 )
        self.m_panel7.Layout()
        bSizer16.Fit( self.m_panel7 )
        bSizer15.Add( self.m_panel7, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.spinCtrlDoublem.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoublem )
        self.spinCtrlDoublen.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoublen )
        self.spinCtrlDoubledt.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubledt )
        self.btnCancel.Bind( wx.EVT_BUTTON, self.onBtnCancel )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.onBtnConfirm )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onSpinCtrlDoublem( self, event ):
        event.Skip()

    def onSpinCtrlDoublen( self, event ):
        event.Skip()

    def onSpinCtrlDoubledt( self, event ):
        event.Skip()

    def onBtnCancel( self, event ):
        event.Skip()

    def onBtnConfirm( self, event ):
        event.Skip()


###########################################################################
## Class ModelessDialog
###########################################################################

class ModelessDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Notification", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer20 = wx.BoxSizer( wx.VERTICAL )

        self.txtMessage = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Message", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.txtMessage.Wrap( -1 )

        bSizer20.Add( self.txtMessage, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.btnOk = wx.Button( self.m_panel8, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer20.Add( self.btnOk, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.m_panel8.SetSizer( bSizer20 )
        self.m_panel8.Layout()
        bSizer20.Fit( self.m_panel8 )
        bSizer19.Add( self.m_panel8, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer19 )
        self.Layout()
        bSizer19.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.onBtnOk )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnOk( self, event ):
        event.Skip()


