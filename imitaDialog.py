from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'Escribí cualquier verdura')
        self.tc1 = tc1 = TextCtrl(p)
        okB = Button(p, ID_OK)
        okB.Bind(EVT_BUTTON, self.accion)
        caB = Button(p, ID_CANCEL)
        flags = ALIGN_CENTER|ALL
        s.Add(st1, 0, flags, 10)
        s.Add(tc1, 0, flags, 10)
        s.Add(okB, 0, flags, 10)
        s.Add(caB, 0, flags, 10)
        p.SetSizer(s)
        f.Show()
        return True


    def accion(self, event):
        salida = "Escribiste:" + self.tc1.GetValue()
        print(salida)


app = MyApp()
app.MainLoop()
