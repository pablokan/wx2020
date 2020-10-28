from wx import *

class MyApp(App):
    def OnInit(self):
        d = Dialog(None)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(d, -1, 'Escribí cualquier verdura')
        tc1 = TextCtrl(d)
        okB = Button(d, ID_OK)
        caB = Button(d, ID_CANCEL)
        flags = ALIGN_CENTER|ALL
        s.Add(st1, 0, flags, 10)
        s.Add(tc1, 0, flags, 10)
        s.Add(okB, 0, flags, 10)
        s.Add(caB, 0, flags, 10)
        d.SetSizer(s)
        if d.ShowModal() == ID_OK:
            salida = "Escribiste:" + tc1.GetValue()
            print(salida)
        else:
            print("Cancelaste")
        d.Destroy()
        return True


app = MyApp()
app.MainLoop()
