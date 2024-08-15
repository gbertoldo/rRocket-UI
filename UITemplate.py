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

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.txtPlotTitle = wx.StaticText( self, wx.ID_ANY, u"Título do gráfico:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtPlotTitle.Wrap( -1 )

        bSizer21.Add( self.txtPlotTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txtCtrlPlotTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.txtCtrlPlotTitle, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnSetTitle = wx.Button( self, wx.ID_ANY, u"Alterar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.btnSetTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer15.Add( bSizer21, 0, wx.EXPAND, 5 )

        self.panelBase = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15.Add( self.panelBase, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

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
        self.btnSetTitle.Bind( wx.EVT_BUTTON, self.onBtnSetTitle )
        self.btnReadMemory.Bind( wx.EVT_BUTTON, self.onBtnReadMemory )
        self.btnFlightReport.Bind( wx.EVT_BUTTON, self.onBtnFlightReport )
        self.btnClearMemory.Bind( wx.EVT_BUTTON, self.onBtnClearMemory )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnSetTitle( self, event ):
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

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.txtPlotTitle = wx.StaticText( self, wx.ID_ANY, u"Título do gráfico:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtPlotTitle.Wrap( -1 )

        bSizer21.Add( self.txtPlotTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txtCtrlPlotTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.txtCtrlPlotTitle, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnSetTitle = wx.Button( self, wx.ID_ANY, u"Alterar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.btnSetTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer10.Add( bSizer21, 0, wx.EXPAND, 5 )

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

        self.buttonSetupInputFileFormat = wx.Button( self, wx.ID_ANY, u"Configurar formato", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.buttonSetupInputFileFormat, 0, wx.ALL, 5 )


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
        self.btnSetTitle.Bind( wx.EVT_BUTTON, self.onBtnSetTitle )
        self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.onFileChanged )
        self.buttonSetupInputFileFormat.Bind( wx.EVT_BUTTON, self.onButtonSetupInputFileFormat )
        self.btnStartStopSimulation.Bind( wx.EVT_BUTTON, self.onBtnStartStopSimulation )
        self.btnReport.Bind( wx.EVT_BUTTON, self.onBtnReport )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnSetTitle( self, event ):
        event.Skip()

    def onFileChanged( self, event ):
        event.Skip()

    def onButtonSetupInputFileFormat( self, event ):
        event.Skip()

    def onBtnStartStopSimulation( self, event ):
        event.Skip()

    def onBtnReport( self, event ):
        event.Skip()


###########################################################################
## Class PanelStatistics
###########################################################################

class PanelStatistics ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.txtPlotTitle = wx.StaticText( self, wx.ID_ANY, u"Título do gráfico:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtPlotTitle.Wrap( -1 )

        bSizer21.Add( self.txtPlotTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txtCtrlPlotTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.txtCtrlPlotTitle, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnSetTitle = wx.Button( self, wx.ID_ANY, u"Alterar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.btnSetTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer10.Add( bSizer21, 0, wx.EXPAND, 5 )

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

        self.buttonSetupInputFileFormat = wx.Button( self, wx.ID_ANY, u"Configurar formato", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.buttonSetupInputFileFormat, 0, wx.ALL, 5 )


        bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnSetup = wx.Button( self, wx.ID_ANY, u"Configurar", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnSetup.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer13.Add( self.btnSetup, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnCalculate = wx.Button( self, wx.ID_ANY, u"Calcular", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnCalculate.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer13.Add( self.btnCalculate, 0, wx.ALL, 5 )


        bSizer13.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.btnReport = wx.Button( self, wx.ID_ANY, u"Gerar relatório", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
        self.btnReport.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer13.Add( self.btnReport, 0, wx.ALL, 5 )


        bSizer10.Add( bSizer13, 0, wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        # Connect Events
        self.btnSetTitle.Bind( wx.EVT_BUTTON, self.onBtnSetTitle )
        self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.onFileChanged )
        self.buttonSetupInputFileFormat.Bind( wx.EVT_BUTTON, self.onButtonSetupInputFileFormat )
        self.btnSetup.Bind( wx.EVT_BUTTON, self.onBtnSetup )
        self.btnCalculate.Bind( wx.EVT_BUTTON, self.onBtnCalculate )
        self.btnReport.Bind( wx.EVT_BUTTON, self.onBtnReport )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnSetTitle( self, event ):
        event.Skip()

    def onFileChanged( self, event ):
        event.Skip()

    def onButtonSetupInputFileFormat( self, event ):
        event.Skip()

    def onBtnSetup( self, event ):
        event.Skip()

    def onBtnCalculate( self, event ):
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
## Class FlightStatisticsSetup
###########################################################################

class FlightStatisticsSetup ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configurar modelo de estatística de voo ", pos = wx.DefaultPosition, size = wx.Size( 900,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        choiceModelChoices = []
        self.choiceModel = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceModelChoices, 0 )
        self.choiceModel.SetSelection( 0 )
        self.choiceModel.SetMinSize( wx.Size( 300,-1 ) )

        bSizer29.Add( self.choiceModel, 0, wx.ALL|wx.EXPAND, 5 )

        self.panelBase = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer29.Add( self.panelBase, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer19.Add( bSizer29, 0, wx.EXPAND, 5 )

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
        self.choiceModel.Bind( wx.EVT_CHOICE, self.onChoiceModel )
        self.btnCancel.Bind( wx.EVT_BUTTON, self.onBtnCancel )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.onBtnConfirm )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onChoiceModel( self, event ):
        event.Skip()

    def onBtnCancel( self, event ):
        event.Skip()

    def onBtnConfirm( self, event ):
        event.Skip()


###########################################################################
## Class PanelStatMovingAverage
###########################################################################

class PanelStatMovingAverage ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,220 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer27 = wx.BoxSizer( wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Partição de tempo (delta t) (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoubledt = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.05, 0.25, 0.1, 0.05 )
        self.spinCtrlDoubledt.SetDigits( 3 )
        fgSizer1.Add( self.spinCtrlDoubledt, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Parâmetro m", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoublem = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 3, 1 )
        self.spinCtrlDoublem.SetDigits( 0 )
        fgSizer1.Add( self.spinCtrlDoublem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Parâmetro n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoublen = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 3, 1 )
        self.spinCtrlDoublen.SetDigits( 0 )
        fgSizer1.Add( self.spinCtrlDoublen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


        bSizer27.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer27 )
        self.Layout()

        # Connect Events
        self.spinCtrlDoubledt.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubledt )
        self.spinCtrlDoublem.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoublem )
        self.spinCtrlDoublen.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoublen )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onSpinCtrlDoubledt( self, event ):
        event.Skip()

    def onSpinCtrlDoublem( self, event ):
        event.Skip()

    def onSpinCtrlDoublen( self, event ):
        event.Skip()


###########################################################################
## Class PanelStatKalmanAlfaFilter
###########################################################################

class PanelStatKalmanAlfaFilter ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,220 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Partição de tempo (delta t) (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoubledt = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.05, 0.25, 0.1, 0.05 )
        self.spinCtrlDoubledt.SetDigits( 3 )
        fgSizer1.Add( self.spinCtrlDoubledt, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Incerteza experimental de h (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoubleStdExp = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.1, 100, 2, 0.25 )
        self.spinCtrlDoubleStdExp.SetDigits( 2 )
        fgSizer1.Add( self.spinCtrlDoubleStdExp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Velocidade crítica Vc (m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        fgSizer1.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.spinCtrlDoubleVc = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 100, 340, 170, 1 )
        self.spinCtrlDoubleVc.SetDigits( 0 )
        fgSizer1.Add( self.spinCtrlDoubleVc, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Incerteza do modelo físico para V<Vc (m/s2)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoubleStdModSub = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.01, 10000, 32, 1 )
        self.spinCtrlDoubleStdModSub.SetDigits( 3 )
        fgSizer1.Add( self.spinCtrlDoubleStdModSub, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Incerteza do modelo físico para V>=Vc (m/s2)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        fgSizer1.Add( self.m_staticText28, 0, wx.ALL, 5 )

        self.spinCtrlDoubleStdModTra = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.01, 10000, 0.1, 1 )
        self.spinCtrlDoubleStdModTra.SetDigits( 3 )
        fgSizer1.Add( self.spinCtrlDoubleStdModTra, 0, wx.ALL, 5 )

        self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Tol. derivada da aceleração (filtro alfa) (m/s3)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText40.Wrap( -1 )

        fgSizer1.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlDoubleDaDt = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0.01, 1000, 32, 1 )
        self.spinCtrlDoubleDaDt.SetDigits( 3 )
        fgSizer1.Add( self.spinCtrlDoubleDaDt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


        bSizer29.Add( fgSizer1, 0, wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer29 )
        self.Layout()

        # Connect Events
        self.spinCtrlDoubledt.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubledt )
        self.spinCtrlDoubleStdExp.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubleStdExp )
        self.spinCtrlDoubleVc.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubleVc )
        self.spinCtrlDoubleStdModSub.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubleStdModSub )
        self.spinCtrlDoubleStdModTra.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubleStdModTra )
        self.spinCtrlDoubleDaDt.Bind( wx.EVT_SPINCTRLDOUBLE, self.onSpinCtrlDoubleDaDt )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onSpinCtrlDoubledt( self, event ):
        event.Skip()

    def onSpinCtrlDoubleStdExp( self, event ):
        event.Skip()

    def onSpinCtrlDoubleVc( self, event ):
        event.Skip()

    def onSpinCtrlDoubleStdModSub( self, event ):
        event.Skip()

    def onSpinCtrlDoubleStdModTra( self, event ):
        event.Skip()

    def onSpinCtrlDoubleDaDt( self, event ):
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


###########################################################################
## Class InputFileFormatFrame
###########################################################################

class InputFileFormatFrame ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Formato de arquivo de entrada", pos = wx.DefaultPosition, size = wx.Size( 350,340 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer26 = wx.BoxSizer( wx.VERTICAL )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.txtInputFileType = wx.StaticText( self, wx.ID_ANY, u"Formato de arquivo de entrada", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtInputFileType.Wrap( -1 )

        fgSizer2.Add( self.txtInputFileType, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        choiceFileFormatChoices = [ u"Personalizado", u"Micro Peak", u"Stratologger" ]
        self.choiceFileFormat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceFileFormatChoices, 0 )
        self.choiceFileFormat.SetSelection( 0 )
        fgSizer2.Add( self.choiceFileFormat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Separador de campo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        fgSizer2.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        choiceFieldSeparatorChoices = [ u"espaço", u",", u";", u"tabulação" ]
        self.choiceFieldSeparator = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceFieldSeparatorChoices, 0 )
        self.choiceFieldSeparator.SetSelection( 0 )
        fgSizer2.Add( self.choiceFieldSeparator, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Separador decimal", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        fgSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )

        choiceDecimalSeparatorChoices = [ u".", u"," ]
        self.choiceDecimalSeparator = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDecimalSeparatorChoices, 0 )
        self.choiceDecimalSeparator.SetSelection( 0 )
        fgSizer2.Add( self.choiceDecimalSeparator, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Comentário", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        fgSizer2.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textCtrlComment = wx.TextCtrl( self, wx.ID_ANY, u"#", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.textCtrlComment, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Linhas de cabeçalho a desconsiderar", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        fgSizer2.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlLinesHeader = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        fgSizer2.Add( self.spinCtrlLinesHeader, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        bSizer26.Add( fgSizer2, 0, wx.ALIGN_RIGHT, 5 )

        fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        fgSizer3.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Coluna", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        fgSizer3.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Unidade", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        fgSizer3.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Tempo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        fgSizer3.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlTCol = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 1 )
        fgSizer3.Add( self.spinCtrlTCol, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"segundo (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        fgSizer3.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Altura", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        self.m_staticText23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        fgSizer3.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spinCtrlHCol = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 2 )
        fgSizer3.Add( self.spinCtrlHCol, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        choiceHUnitChoices = [ u"metro (m)", u"pé (ft)" ]
        self.choiceHUnit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceHUnitChoices, 0 )
        self.choiceHUnit.SetSelection( 0 )
        fgSizer3.Add( self.choiceHUnit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


        bSizer26.Add( fgSizer3, 0, wx.ALIGN_RIGHT, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer26.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

        self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.buttonCancel, 0, wx.ALL, 5 )

        self.buttonConfirm = wx.Button( self, wx.ID_ANY, u"Confirmar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.buttonConfirm, 0, wx.ALL, 5 )


        bSizer26.Add( bSizer28, 0, wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer26 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.choiceFileFormat.Bind( wx.EVT_CHOICE, self.onChoiceFileFormat )
        self.buttonCancel.Bind( wx.EVT_BUTTON, self.onButtonCancel )
        self.buttonConfirm.Bind( wx.EVT_BUTTON, self.onButtonConfirm )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onChoiceFileFormat( self, event ):
        event.Skip()

    def onButtonCancel( self, event ):
        event.Skip()

    def onButtonConfirm( self, event ):
        event.Skip()


