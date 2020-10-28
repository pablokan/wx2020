from wx import*
from wx.dataview import * 
import sqlite3

class MyApp(App):
    def OnInit(self):
        d = Dialog(None, title= "Cargar clientes", size=(200,290))
        s = BoxSizer(VERTICAL)
        stl = StaticText(d, -1, 'Cargar cliente con\nlos siguientes datos: ')
        Nombre = TextCtrl(d, value= 'Nombre ', size=(125,25))
        DNI = TextCtrl(d, value='DNI', size=(125,25))
        Fecha = TextCtrl(d, value='Fecha de Nacimiento', size=(125,25))
        okB = Button(d, ID_OK)
        caB = Button(d, ID_CANCEL)
        flags = ALIGN_CENTER|ALL
        s.Add(stl, 0, flags, 4)
        s.Add(Nombre, 0, flags, 4)
        s.Add(DNI, 0, flags, 4)
        s.Add(Fecha, 0, flags, 4)
        s.Add(okB, 0, flags, 10)
        s.Add(caB, 0, flags, 1)
        d.SetSizer(s)
        if d.ShowModal()==ID_OK:
            print(ID_OK)
            salida = "Nuevo cliente: "+ Nombre.GetValue()+ " ("+ DNI.GetValue()+") Fecha de nacimiento: "+Fecha.GetValue()
            print(salida)
            dni = DNI.GetValue()
            nombre = Nombre.GetValue()
            fnac = Fecha.GetValue()
            con = sqlite3.connect("Clientes01.db")
            cur = con.cursor()
            alta = f"INSERT INTO datos (dni, nombre, fnac) VALUES ('{dni}', '{nombre}', '{fnac}')"
            cur.execute(alta)
            con.commit()
            con.close()
            con = sqlite3.connect("Clientes01.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM datos ORDER BY Nombre")
            tuplas = cur.fetchall()
            print(tuplas)

        else:
            print("Cancelaste")
        d.Destroy()
        return True

app = MyApp()
app.MainLoop()