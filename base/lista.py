from wx import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(-1, 700))
        s = BoxSizer(VERTICAL)
        self.lis = lis = []
        for i in range(5):
            t = TextCtrl(f)
            lis.append(t)
            s.Add(t, 0, ALL, 10)
        b = Button(f, label="Botón")
        b.Bind(EVT_BUTTON, self.mostrar)
        s.Add(b, 0, ALL, 10)
        f.SetSizer(s)
        f.Show()
        return True

    def mostrar(self, event):
        for i in range(5):
            print(self.lis[i].GetValue())


app = MyApp()
app.MainLoop()
