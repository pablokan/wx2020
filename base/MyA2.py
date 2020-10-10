from wx import *

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, title="Título de la ventana")
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.sNombre = sNombre = StaticText(p, -1, "Ingrese número:")
        self.tNombre = tNombre = TextCtrl(p)
        self.b = b = Button(p, -1, "el doble")
        self.resultado = StaticText(p, -1, "Resultado")
        b.Bind(EVT_BUTTON, self.accion)
        b.Bind(EVT_SET_FOCUS, self.cambiaColor)
        s.Add(sNombre, 0, ALL, 10)
        s.Add(tNombre, 0, ALL|EXPAND, 10)
        s.Add(b, 0, TOP|CENTER, 20)
        s.Add(self.resultado, 0, ALL|CENTER, 20)
        p.SetSizer(s)
        f.Show()
        return True

    def cambiaColor(self, event):
        self.b.SetForegroundColour((255,0,0))

    def accion(self, event):
        v = int(self.tNombre.GetValue())
        salida = self.resultado.GetLabel() + " = " + str(v*2)
        self.resultado.SetLabel(salida)


app = MyApp()
app.MainLoop()
