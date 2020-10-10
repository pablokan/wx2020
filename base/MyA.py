from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'ventna')
        f.Show()
        return True

    def accion(self, event):
        print('botoncito')


app = MyApp()
app.MainLoop()
