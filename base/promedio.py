from wx import *

class MyApp(App):
    def OnInit(self):
        self.lista = lista = []
        f = Frame(None)
        p = Panel(f)
        s = BoxSizer(HORIZONTAL)
        for i in range(3):
            n = TextCtrl(p)
            s.Add(n)
            lista.append(n)
        b = Button(p, -1, "Promedio")
        s.Add(b)
        b.Bind(EVT_BUTTON, self.prom)
        self.pr = StaticText(p)
        s.Add(self.pr)
        p.SetSizer(s)
        f.Show()
        return True

    def prom(self, event):
        tot = 0
        for i in range(3):
            v = int(self.lista[i].GetValue())
            tot += v
        self.pr.SetLabel(str(tot/3))
        

app = MyApp()
app.MainLoop()
        
