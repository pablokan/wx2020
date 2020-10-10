# Base kan
from wx import *

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, -1, "Título de la ventana", size=(700, 400))
        self.p = p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.sNombre = sNombre = StaticText(p, -1, "Ingrese nombre:")
        self.tNombre = tNombre = TextCtrl(p, size=(200, -1))
        self.b = b = Button(p, -1, "Botoncito")
        self.saludo = StaticText(p)
        b.Bind(EVT_BUTTON, self.algo)
        b.Bind(EVT_SET_FOCUS, self.cambiaColor)
        s.Add(sNombre, 0, ALL, 30)
        s.Add(tNombre, 0, ALL|CENTER, 30)
        s.Add(b, 0, EXPAND|ALL, 30)
        s.Add(self.saludo, 0, ALL, 30)
        p.SetSizer(s)
        f.Show()
        return True

    def cambiaColor(self, event):
        self.b.SetForegroundColour((255,0,0))

    def algo(self, event):
        nombre = self.tNombre.GetValue()
        salida = "Hola " + nombre
        self.saludo.SetLabel(salida)
        self.p.Destroy()




app = MyApp()
app.MainLoop()
