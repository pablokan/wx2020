from wx import *

class MyApp(App):
    def OnInit(self):
        d = Dialog(None, size=(-1, 700))
        s = BoxSizer(VERTICAL)
        st1 = StaticText(d, -1, 'Escribí cualquier verdura')
        tc1 = TextCtrl(d)
        okB = Button(d, ID_OK)
        okB.SetLabel("otro label")
        caB = Button(d, ID_CANCEL)
        otroB = Button(d, ID_HELP)
        #d.SetOKCancelLabels("OK Button String", "Cancel Button string")
        flags = ALIGN_CENTER|ALL
        s.Add(st1, 0, flags, 10)
        s.Add(tc1, 0, flags, 10)
        s.Add(okB, 0, flags, 10)
        s.Add(caB, 0, flags, 10)
        s.Add(otroB, 0, flags, 10)
        d.SetSizer(s)
        if d.ShowModal() == ID_OK:
            salida = "Escribiste:" + tc1.GetValue()
            print(salida)
        #elif d.ShowModal() == ID_HELP:
        #    print("help")
        else:
            print("Cancelaste")
        d.Destroy()
        return True


app = MyApp()
app.MainLoop()
