from wx import *

class MyApp(App):
    def OnInit(self):
        f = self.f = Frame(None, -1, "")
        p = self.p = Panel(f, -1)
        s = self.s = BoxSizer()
        botonList = self.botonList = [0]
        for x in range(1, 4):
            b = Button(p, x, str(x))
            botonList.append(b)
            s.Add(b, 0, ALL, 5)
            botonList[x].Bind(EVT_BUTTON, self.onClick)
        p.SetSizer(s)
        f.Show()
        return True

    def onClick(self, e):
        ident = e.GetId()
        print(ident)
        self.botonList[ident].SetBackgroundColour("red")

app = MyApp()
app.MainLoop()
