from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'Radio Buttons')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'Seleccione una opción')
        listaEdades = ["menor", "adulto", "anciano"]
        self.opcion = RadioBox(p, choices=listaEdades)
        self.opcion.Bind(EVT_RADIOBOX, self.clickeo)
        bt1 = Button(p, -1, 'Choice')
        bt1.Bind(EVT_BUTTON, self.accion)
        s.Add(st1, 0, ALL|EXPAND, 10)
        s.Add(self.opcion, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def clickeo(self, event):
        print(self.opcion.GetSelection())

    def accion(self, event):
        edad = self.opcion.GetString(self.opcion.GetSelection())
        print(self.opcion.GetSelection(), edad)


app = MyApp()
app.MainLoop()
