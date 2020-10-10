from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'Check Boxes')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        cartelCheck = StaticText(p, -1, "Elija todos los que correspondan")
        s.Add(cartelCheck, 0, ALL|EXPAND, 10)
        self.casa = CheckBox(p, -1, "Casa")
        self.auto = CheckBox(p, -1, "Auto")
        s.Add(self.casa, 0, ALL, 3)
        s.Add(self.auto, 0, ALL, 3)
        bt1 = Button(p, -1, 'mostrar')
        bt1.Bind(EVT_BUTTON, self.accion)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        self.sal = StaticText(p)
        s.Add(self.sal, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        salida = "Tiene"
        print(self.casa.GetValue(), self.auto.GetValue())
        if self.casa.GetValue():
            salida += " -casa"
        if self.auto.GetValue():
            salida += " -auto"
        self.sal.SetLabel(salida)


app = MyApp()
app.MainLoop()

