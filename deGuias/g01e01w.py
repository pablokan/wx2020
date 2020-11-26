from wx import *
from validador import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)

# fila 2 - las cajas de texto        
        self.n1 = n1 = TextCtrl(p, validator=MyValidator())
        self.n2 = n2 = TextCtrl(p, validator=MyValidator())
        fila2 = BoxSizer(HORIZONTAL)
        fila2.Add(n1, 0, ALL, 10)
        fila2.Add(n2, 0, ALL, 10)

# main sizer
        s = BoxSizer(VERTICAL)
        flags = ALL|CENTER
        solicitud = StaticText(p, -1, "Ingrese dos números")
        s.Add(solicitud, 0, flags, 10)
        
        s.Add(fila2, 0, flags, 10)
        
        self.b = b = Button(p, label="Sumar")
        b.Bind(EVT_BUTTON, self.suma)
        s.Add(b, 0, flags, 10)

        self.t = t = StaticText(p, label="Resultado")
        s.Add(t, 0, flags, 25)

        p.SetSizer(s)
        f.Show()
        return True

    def suma(self, event):
        s = str(float(self.n1.GetValue()) + float(self.n2.GetValue()))
        s = self.t.GetLabel() + " = " + s
        self.t.SetLabel(s)
        

app = MyApp()
app.MainLoop()
