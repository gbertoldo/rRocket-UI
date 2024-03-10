import wx
import UITemplate

class ModelessDialog(UITemplate.ModelessDialog):
    def __init__(self, parent, title, message, delayMS=0):
        UITemplate.ModelessDialog.__init__(self, parent)
        self.SetTitle(title)
        self.txtMessage.SetLabel(title)
        szTitle = self.txtMessage.GetSize()
        self.txtMessage.SetLabel(message)
        szMsg = self.txtMessage.GetSize()
        szBtn = self.btnOk.GetSize()
        width = 100
        if szTitle[0] > szMsg[0]:
            width = width + szTitle[0]
        else:
            width = width + szMsg[0]
        height = szMsg[1]+szBtn[1]+80
        self.SetSize(width, height)
        self.Layout()
        if delayMS > 0:
          self.timer = wx.Timer(self)
          self.Bind(wx.EVT_TIMER, self.onBtnOk, self.timer)
          self.timer.Start(delayMS, oneShot=wx.TIMER_ONE_SHOT)
    def onBtnOk( self, event ):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App()

    frm = ModelessDialog(None, "Estado da memória de voo", "Memória de voo vazia", delayMS=2000)
    frm.Show()
    app.MainLoop()