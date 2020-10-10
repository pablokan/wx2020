from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = BoxSizer()
        listaOpc = ["uno", "dos", "tres"]
        self.combo = ComboBox(p, size=(150, -1), value="Opciones", choices=listaOpc)
        s.Add(self.combo, 0, ALL, 20)
        inp = TextCtrl(p)
        s.Add(inp, 0, ALL, 20)
        self.combo.Bind(EVT_KILL_FOCUS, self.accion)
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print(self.combo.GetValue())
        #event.Skip()

app = MyApp()
app.MainLoop()









