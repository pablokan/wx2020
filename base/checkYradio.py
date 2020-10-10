from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = self.p = Panel(f)
        grilla = GridBagSizer(10, 10)

# CheckBoxes
        cartelCheck = StaticText(p, -1, "Elija todos los que correspondan")
        grilla.Add(cartelCheck, (0,0), (1, 4), TOP|ALIGN_CENTER, 10)
        self.casa = CheckBox(p, -1, "Casa")
        self.auto = CheckBox(p, -1, "Auto")
        grilla.Add(self.casa, (1, 0), (1, 2), TOP|ALIGN_CENTER, 10)
        grilla.Add(self.auto, (1, 2), (1, 2), TOP|ALIGN_CENTER, 10)

# Radio Buttons
        edad = StaticText(p, -1, "Edades")
        grilla.Add(edad, (3,0), (1, 4), TOP|ALIGN_CENTER, 10)
        listaEdades = ["menor", "adulto", "anciano"]
        self.opcion = RadioBox(p, choices=listaEdades)
        grilla.Add(self.opcion, (4, 0), (1, 4), TOP|ALIGN_CENTER, 10)

# Botón
        bMostrar = Button(p, -1, "Resultado")
        grilla.Add(bMostrar, (7, 2), (1, 1), ALL|EXPAND, 10)
        bMostrar.Bind(EVT_BUTTON, self.mostrar)

# Muestra la grilla
        p.SetSizerAndFit(grilla)
        f.Show()
        return True

    def mostrar(self, event):
        bienes = ""
        salida = Frame(None)
        if self.casa.GetValue():
            bienes += "Casa"
        if self.auto.GetValue():
            bienes += " Auto"
        edad = self.opcion.GetString(self.opcion.GetSelection())
        print(self.opcion.GetSelection())
        texto = bienes + "---" + edad
        s = StaticText(salida, label=texto)
        salida.Show()
        

prog = MyApp()
prog.MainLoop()
