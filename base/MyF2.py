import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)        
        sizer = wx.BoxSizer(wx.VERTICAL)        
        text_ctrl = wx.TextCtrl(panel)
        sizer.Add(text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        btn = wx.Button(panel, label='Botoncito')
        sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(sizer)        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()