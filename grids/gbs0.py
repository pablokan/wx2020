from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = GridBagSizer(30, 30)
        tc1 = TextCtrl(p, value="caja1")
        tc2 = TextCtrl(p, value="caja2")
        s.Add(tc1, (1, 1))
        s.Add(tc2, (0, 0))
        p.SetSizer(s)
        f.Show()
        return True


app = MyApp()
app.MainLoop()
