from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(1000, 1000))
        gbs = GridBagSizer(0,0)
        for i in range(5):
            t = TextCtrl(f)
            gbs.Add(t, pos=(i,i))
        u = TextCtrl(f)
        gbs.Add(u, pos=(10,2), span=(1,6))
        f.SetSizer(gbs)
        f.Show()
        return True


app = MyApp()
app.MainLoop()
