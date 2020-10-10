from wx import *

class Mayor(App):
    def OnInit(self):
        lista=[]
        self.lista = lista
        f = Frame(None)
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        cartelito= StaticText(p, -1, "ingrese nombre y seleccione sexo")
        s.Add(cartelito,0,TOP|CENTER,10)
        self.sexo=[]
        Genero=["Hombre","Mujer"]
        for i in range(8):
            n = TextCtrl(p)
            self.opcion = RadioBox(p, choices=Genero)
            self.opcion.Bind(EVT_RADIOBOX,self.accion)
            s.Add(n,0,TOP|CENTER,10)
            s.Add(self.opcion,0,CENTER,10)
            lista.append(n)
        b = Button(p, -1, "Contar")
        b.Bind(EVT_BUTTON,self.mostrar)
        s.Add(b,0,TOP,10)
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        edad = self.opcion.GetString(self.opcion.GetSelection())
        print(self.opcion.GetSelection(), edad)
        self.sexo.append(edad)
    
    def mostrar(self,event):
        print(self.sexo)
app = Mayor()
app.MainLoop()