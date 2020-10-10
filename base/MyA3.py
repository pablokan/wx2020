from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title="Título de la ventana")
        panel = Panel(f)
        s = BoxSizer(VERTICAL)
        self.cartelito = cartelito = StaticText(panel, -1, "Ingrese nombre")
        self.nombre = nombre = TextCtrl(panel)
        b = Button(panel, label="Botoncito")
        b.Bind(EVT_BUTTON, self.accion)
        s.Add(cartelito, 0, TOP|CENTER, 30)
        s.Add(nombre, 0, SHAPED)
        s.Add(b, 0, ALL|CENTER, 10)
        panel.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        self.cartelito.SetLabel("apretaste el botoncito")
        self.nombre.SetValue("apretaste el botoncito")
        f2 = Frame(None, pos=(2000, 1))
        f2.Show()


app = MyApp()
app.MainLoop()
