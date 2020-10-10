from wx import *

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, -1, "Titulo")
        p = Panel(f)
        s = BoxSizer(VERTICAL)      
        self.sNombre = StaticText(p, -1, "Ingrese el nombre") 
        self.tNombre = TextCtrl(p)          
        b = Button(p, -1, "Boton")
        b.Bind(EVT_BUTTON, self.accion)
        s.Add(self.sNombre,0, TOP, 10)          
        s.Add(self.tNombre,0, EXPAND| TOP, 10)            
        s.Add(b, 0, TOP, 10)                          
        p.SetSizer(s)           


        f.Show()
        return True

    def accion(self,event):
        v = self.tNombre.GetValue()
        self.sNombre.SetLabel(v)
        f2 = Frame(None, title="Otra ventana", pos=(2,2))
        f2.Show()
        self.f.Close()




app = MyApp()
app.MainLoop()

#7. INDICAMOS COMO QUEREMOS ORDENAR TOOD (VERTICAL EN ESE CASO)
#8. ES EL TEXTO QUE QUEREMOS QUE APAREZCA DENTRO DE LA CAJA
#9. ES LA CAJA DONDE INGRESAREMOS DATOS.
#11. INDICAMOS QUE VA A HACER EL BOTON ( A LA ACCION DEL BOTON LO PROGRAMAMOS EN EL DEF DE LA LINEA 21)
#12. /TOP/ EL TOP + EL NUMERO, ME SEPARA EL TEXTO DE LA PARTE DE ARRIBA
#13. ALL + EL NUMERO, ME SEPARA EL TEXTO DEL MARGEN LATERAL (Uso el palito para separar)
#13. EL EXPAND ME EXPANDE LA BARRA DE LA LINEA 7 POR TODA LA VENTANA
#15. INSTRUCCION QUE ACOMODA TODO (vertical por la linea 7)
#19. EL EVENTI VA SI O SI.. CORTE SELF
#22. SI PONGO "self.sNombre.GetValue(/aca va el texto nuevo que va a cambiar/)" EL GetValue ME AGREGA TEXTO DE ARRIBA CUANDO APRIETO EL BOTON
#23. SI PONGO "self.sNombre.SetLabel(/aca va el texto nuevo que va a cambiar/)" EL SETLABEL ME CAMBIA EL TEXTO DE ARRIBA (el de la linea 8) CUANDO APRIETO EL BOTON
