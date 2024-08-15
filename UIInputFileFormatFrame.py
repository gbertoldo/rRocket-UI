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
import UITemplate

FILEFORMATCHOICES={"labels":[ u"Personalizado", u"rRocket",u"MicroPeak", u"Stratologger" ],"values":[0,1,2,3]}
FIELDSEPARATORCHOICES ={"labels": [ u"espaço", u",", u";", u"tabulação" ],"values":['\s+',',',';','\t']}
DECIMALSEPARATORCHOICES = {"labels":[ u".", u"," ],"values":[ u".", u"," ]}
HUNITCHOICES = {"labels":[ u"metro (m)", u"pé (ft)" ],"values":[1.0, 0.3048]}

class InputFileFormat:
  def __init__(self):
    self.type=0
    self.fieldSeparator="\s+"
    self.decimalSeparator="."
    self.comment="#"
    self.headerLines=0
    self.tCol=1
    self.hCol=2
    self.hUnit=1.0

class InputFileFormatFrame(UITemplate.InputFileFormatFrame):
    def __init__(self, parent, inputFileFormat = InputFileFormat()):
        UITemplate.InputFileFormatFrame.__init__(self, parent)

        self.parent = parent
        self.inputFileFormat=inputFileFormat

        self.choiceFileFormat.Clear()
        self.choiceFieldSeparator.Clear()
        self.choiceDecimalSeparator.Clear()
        self.choiceHUnit.Clear()
        self.choiceFileFormat.SetItems(FILEFORMATCHOICES["labels"])
        self.choiceFieldSeparator.SetItems(FIELDSEPARATORCHOICES["labels"])
        self.choiceDecimalSeparator.SetItems(DECIMALSEPARATORCHOICES["labels"])
        self.choiceHUnit.SetItems(HUNITCHOICES["labels"])

        self.rRocketFormat=InputFileFormat()
        self.rRocketFormat.type=1
        self.rRocketFormat.fieldSeparator="\s+"
        self.rRocketFormat.decimalSeparator="."
        self.rRocketFormat.comment="#"
        self.rRocketFormat.headerLines=0
        self.rRocketFormat.tCol=1
        self.rRocketFormat.hCol=2
        self.rRocketFormat.hUnit=1.0

        self.microPeakFormat=InputFileFormat()
        self.microPeakFormat.type=2
        self.microPeakFormat.fieldSeparator=","
        self.microPeakFormat.decimalSeparator=","
        self.microPeakFormat.comment="#"
        self.microPeakFormat.headerLines=1
        self.microPeakFormat.tCol=1
        self.microPeakFormat.hCol=3
        self.microPeakFormat.hUnit=1.0

        self.SLFormat=InputFileFormat()
        self.SLFormat.type=3
        self.SLFormat.fieldSeparator="\s+"
        self.SLFormat.decimalSeparator="."
        self.SLFormat.comment="#"
        self.SLFormat.headerLines=1
        self.SLFormat.tCol=1
        self.SLFormat.hCol=2
        self.SLFormat.hUnit=0.3048
      
        self.fillForm(self.inputFileFormat)

    def fillForm(self, fmt: InputFileFormat):
        self.choiceFileFormat.SetSelection(FILEFORMATCHOICES["values"].index(fmt.type))
        self.choiceFieldSeparator.SetSelection(FIELDSEPARATORCHOICES["values"].index(fmt.fieldSeparator))
        self.choiceDecimalSeparator.SetSelection(DECIMALSEPARATORCHOICES["values"].index(fmt.decimalSeparator))
        self.choiceHUnit.SetSelection(HUNITCHOICES["values"].index(fmt.hUnit))

        self.textCtrlComment.SetLabel(fmt.comment)
        self.spinCtrlLinesHeader.SetValue(fmt.headerLines)
        self.spinCtrlTCol.SetValue(fmt.tCol)
        self.spinCtrlHCol.SetValue(fmt.hCol)

        if fmt.type == 1 :
          self.choiceFieldSeparator.Disable()
          self.choiceFieldSeparator.Disable()
          self.choiceDecimalSeparator.Disable()
          self.choiceHUnit.Disable()
          self.textCtrlComment.Disable()
          self.spinCtrlLinesHeader.Disable()
          self.spinCtrlTCol.Disable()
          self.spinCtrlHCol.Disable()
        elif fmt.type == 2:
          self.choiceFieldSeparator.Disable()
          self.choiceFieldSeparator.Disable()
          self.choiceDecimalSeparator.Disable()
          self.choiceHUnit.Disable()
          self.textCtrlComment.Disable()
          self.spinCtrlLinesHeader.Disable()
          self.spinCtrlTCol.Disable()
          self.spinCtrlHCol.Disable()
        elif fmt.type == 3:
          self.choiceFieldSeparator.Disable()
          self.choiceFieldSeparator.Disable()
          self.choiceDecimalSeparator.Disable()
          self.choiceHUnit.Disable()
          self.textCtrlComment.Disable()
          self.spinCtrlLinesHeader.Disable()
          self.spinCtrlTCol.Disable()
          self.spinCtrlHCol.Disable()
        else:
          self.choiceFieldSeparator.Enable()
          self.choiceFieldSeparator.Enable()
          self.choiceDecimalSeparator.Enable()
          self.choiceHUnit.Enable()
          self.textCtrlComment.Enable()
          self.spinCtrlLinesHeader.Enable()
          self.spinCtrlTCol.Enable()
          self.spinCtrlHCol.Enable()

    def extractForm(self):
        fmt = InputFileFormat()
        fmt.type = self.choiceFileFormat.GetSelection()
        fmt.fieldSeparator = FIELDSEPARATORCHOICES["values"][self.choiceFieldSeparator.GetSelection()]
        fmt.decimalSeparator = DECIMALSEPARATORCHOICES["values"][self.choiceDecimalSeparator.GetSelection()]
        fmt.hUnit = HUNITCHOICES["values"][self.choiceHUnit.GetSelection()]

        fmt.comment = self.textCtrlComment.GetLabel()
        fmt.headerLines = self.spinCtrlLinesHeader.GetValue()
        fmt.tCol = self.spinCtrlTCol.GetValue()
        fmt.hCol = self.spinCtrlHCol.GetValue()
        return fmt

    def GetDefaultFileFormat(self):
        return InputFileFormat()   

    def onChoiceFileFormat( self, event ):
        opt = self.choiceFileFormat.GetSelection()
        if opt == 1:
           self.fillForm(self.rRocketFormat)
        elif opt == 2:
           self.fillForm(self.microPeakFormat)
        elif opt == 3:
           self.fillForm(self.SLFormat)
        else:
           self.fillForm(self.GetDefaultFileFormat())
        
    def onButtonCancel( self, event ):
        self.Destroy()

    def onButtonConfirm( self, event ):
        self.parent.setInputFileFormat(self.extractForm())
        self.Destroy()
