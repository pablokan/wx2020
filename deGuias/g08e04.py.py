from wx import *

class MyApp(App):
    def OnInit(self):
        self.lista = []
        f = Frame(None, -1, 'carga')
        self.p = p = Panel(f)
        p.SetBackgroundColour("brown")
        self.s = s = GridBagSizer(5, 5)
        st1 = StaticText(p, -1, 'ingrese número:')
        self.numero = TextCtrl(p)
        boton = Button(p, -1, 'Agregar')
        boton.Bind(EVT_BUTTON, self.accion)
        s.Add(st1, (0, 0), (1, 1), ALL|EXPAND, 10)
        s.Add(self.numero, (0, 1), (1, 1), ALL|EXPAND, 10)
        s.Add(boton, (1, 0), (1, 2), ALL|EXPAND, 10)
        p.SetSizerAndFit(s)
        f.Show()
        return True

    def accion(self, event):
        self.lista.append(int(self.numero.GetValue()))
        self.numero.SetValue("")
        print(self.lista)

app = MyApp()
app.MainLoop()
