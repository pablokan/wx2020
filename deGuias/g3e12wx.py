 #1: Ingresar la lluvia caída en milímetros para cada día de la semana. 
 #2: Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title="Lluvia esta semana", size=(-1, 700))
        dS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        sD = GridBagSizer(20, 10)
        
        listaMM = []
        for i in range(7):
            nD = StaticText(f)
            nD.SetLabel(dS[i])
            sD.Add(nD, pos=(i, 0))
            mm = TextCtrl(f)
            listaMM.append(mm)
            sD.Add(mm, pos=(i, 1))
        b = Button(f)
        sD.Add(b, pos=(10,1))
        
        f.SetSizer(sD)
        f.Show()
        return True


app = MyApp()
app.MainLoop()
