# Base standard
import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Window Title')
        self.Show()

my_app = wx.App()
my_frame = MyFrame()
my_app.MainLoop()
