from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(1000, 1000))
        gbs = GridBagSizer(0,0)
        s = StaticText(f, -1, "fdjsfjkldsfj")
        t = TextCtrl(f)
        b = Button(f)
        gbs.Add(s, pos=(1,1))
        gbs.Add(t, pos=(2,1))
        gbs.Add(b, pos=(2,2))
        f.SetSizer(gbs)
        f.Show()
        return True


app = MyApp()
app.MainLoop()
