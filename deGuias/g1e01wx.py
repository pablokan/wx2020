from wx import *
from validador import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(500, 100))
        p = Panel(f)
        s = BoxSizer()
        self.n1 = n1 = TextCtrl(p, validator=MyValidator())
        self.n2 = n2 = TextCtrl(p, validator=MyValidator())
        self.b = b = Button(p, label="Sumar")
        b.Bind(EVT_SET_FOCUS, self.bONf)
        b.Bind(EVT_BUTTON, self.suma)
        self.t = t = StaticText(p, label="Resultado", size=(100, 100))
        s.Add(n1, 1, EXPAND|ALL, 10)
        s.Add(n2, 1, EXPAND|ALL, 10)
        s.Add(b, 3, EXPAND|ALL, 10)
        s.Add(t, 1, EXPAND|ALL, 25)
        p.SetSizer(s)
        f.Show()
        return True


    def bONf(self, event):
        self.b.SetBackgroundColour((255,0,0)) 
        
    def suma(self, event):
        s = str(int(self.n1.GetValue()) + int(self.n2.GetValue()))
        s = "Resultado = " + s
        self.t.SetLabel(s)
        self.t.SetForegroundColour("green")
        

app = MyApp()
app.MainLoop()
