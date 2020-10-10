from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title="Obtener nombres de las mujeres", size=(-1, 700))
        s = GridBagSizer(20, 10)

        self.listaN = listaN = []
        self.listaS = listaS = []
        titu1 = StaticText(f, label="Nombre")
        titu2 = StaticText(f, label="Sexo", pos=(0,30))
        s.Add(titu1, pos=(0,0), flag=ALIGN_CENTER|TOP, border=15)
        s.Add(titu2, pos=(0,1), flag=ALIGN_CENTER|TOP, border=15)
        sexos = ["Femenino", "Masculino", "Chique"]
        for i in range(8):
            n = TextCtrl(f)
            listaN.append(n)
            s.Add(n, pos=(i+1,0), flag=TOP, border=10)
            sex = self.sex = RadioBox(f,choices=sexos)
            listaS.append(sex)
            s.Add(sex, pos=(i+1,1))
        b = Button(f, label="Chicas")
        b.Bind(EVT_BUTTON, self.getWomen)
        s.Add(b, pos=(9,1))
        f.SetSizer(s)
        f.Show()
        return True

    def getWomen(self, event):
        f = Frame(None, title="Nombres de las chicas", size=(150, -1))
        s = BoxSizer(VERTICAL)
        
        for i in range(8):
            sexo = self.listaS[i].GetString(self.listaS[i].GetSelection())
            if sexo == "Femenino":
                n = self.listaN[i].GetValue()
                t = StaticText(f)
                t.SetLabel(n)
                s.Add(t, 0, ALL, 20)
 
        f.SetSizer(s)
        f.Show()


app = MyApp()
app.MainLoop()
