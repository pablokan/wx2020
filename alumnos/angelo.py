
from wx import *

class MyApp(App):
    def OnInit(self):
        self.cont = 0
        self.total = 0
        self.f = f = Frame(None, -1 , title = "Guia 9 Ejercicio 2")
        self.p = p = Panel(self.f)
        self.gbs = GridBagSizer(1,1)
        self.st1 = StaticText(p, -1, "Ingrese un numero: ")
        self.st2 = StaticText(p, -1, "")
        self.tc1 = TextCtrl(p, -1)
        self.bt1 = Button(p, -1, "Agregar")
        self.bt1.Bind(EVT_BUTTON, self.accion)
        self.gbs.Add(self.st1, (1,1), (1,1))
        self.gbs.Add(self.tc1, (1,2), (1,1))
        self.gbs.Add(self.bt1, (3,2), (1,1))
        self.gbs.Add(self.st2, (4,1), (1,2))
        self.p.SetSizer(self.gbs)
        self.f.Show()
        return True

    def accion(self, event):
        self.total +=1
        num = self.tc1.GetValue()
        self.tc1.SetValue("")
        if int(num) > 23:
            self.cont +=1  
        if self.total ==2:
            self.st2.SetLabel("La cantidad de numeros mayores a 23 son: " + str(self.cont))
            self.st1.Destroy()
            self.tc1.Destroy()
            self.bt1.Destroy()
            


app = MyApp()
app.MainLoop()