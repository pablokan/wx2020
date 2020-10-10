from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'Uso de setters y getters')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.st1 = StaticText(p, -1, 'StaticText')
        self.tc1 = TextCtrl(p, -1, "TextCtrl")
        bt1 = Button(p, -1, 'mostrar')
        bt1.Bind(EVT_BUTTON, self.accion)
        s.Add(self.st1, 0, ALL|EXPAND, 10)
        s.Add(self.tc1, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print("self.tc1.GetValue():", self.tc1.GetValue())
        self.tc1.SetValue("nuevo valor asignado con SetValue")
        print("self.st1.GetLabel():", self.st1.GetLabel())
        self.st1.SetLabel("nuevo valor asignado con SetLabel")
        

app = MyApp()
app.MainLoop()
