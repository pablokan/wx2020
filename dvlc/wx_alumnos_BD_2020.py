from wx import *
from wx.dataview import * 
import sqlite3


class MyApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Alumnos", size=(700, 500))
        p1 = self.p1 = Panel(f1)

        self.dvlc = dvlc = DataViewListCtrl(p1)
        dvlc.Bind(EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.modif)
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn('DNI', width=130)
        dvlc.AppendTextColumn('Nombre', width=250, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Comisión', width=75)
        dvlc.AppendTextColumn('Sexo', width=75)
        dvlc.AppendTextColumn('F. Nac.', width=100)

        for c in self.dvlc.Columns:
            c.Sortable = True
            c.Reorderable = True

        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Carga de archivo")
        bA = Button(p1, -1, "&Alta")
        bB = Button(p1, -1, "&Borrar")
        hor.Add(b)
        hor.Add(bA)
        hor.Add(bB)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.cargaDatos)
        bA.Bind(EVT_BUTTON, self.alta)
        bB.Bind(EVT_BUTTON, self.borrar)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()
        return True

    def cargaDatos(self, event):
        def recupBD():
            con = sqlite3.connect("alumnos2020.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM datos ORDER BY Nombre")
            tuplas = cur.fetchall()
            print(tuplas)
            listaA = [list(e) for e in tuplas]
            for e in listaA:
                e[0] = str(e[0])
            con.close()
            return listaA

        lista = recupBD()
        print(lista)
        for e in lista:
            self.dvlc.AppendItem(e)

    def modif(self, evt):
        def grabaBD(id, dni, nombre, comision, sexo, fnac):
            con = sqlite3.connect("alumnos2020.db")
            cur = con.cursor()
            actu = f"UPDATE datos SET dni='{dni}', nombre='{nombre}' WHERE id={id}"
            cur.execute(actu)
            con.commit()
            con.close()

        row = self.dvlc.GetSelectedRow()
        id = self.dvlc.GetTextValue(row, 0)
        dni = self.dvlc.GetTextValue(row, 1)
        nombre = self.dvlc.GetTextValue(row, 2)
        comision = self.dvlc.GetTextValue(row, 3)
        sexo = self.dvlc.GetTextValue(row, 4)
        fnac = self.dvlc.GetTextValue(row, 5)
        grabaBD(id, dni, nombre, comision, sexo, fnac)

    def alta(self, event):
        f2 = Frame(None, -1, "Alta")
        p2 = Panel(f2)
        col1 = BoxSizer(VERTICAL)
        dni1 = StaticText(p2, label="DNI", size=(-1, 35))
        nombre1 = StaticText(p2, label="Nombre", size=(-1, 35))
        comision1 = StaticText(p2, label="Comisión", size=(-1, 35))
        sexo1 = StaticText(p2, label="Sexo", size=(-1, 35))
        fnac1 = StaticText(p2, label="Fecha de Nacimiento   ", size=(-1, 35))
        col1.Add(dni1,1, TOP, 10)
        col1.Add(nombre1)
        col1.Add(comision1)
        col1.Add(sexo1)
        col1.Add(fnac1)

        col2= BoxSizer(VERTICAL)
        self.dni2 = TextCtrl(p2, -1, "DNI", size=(-1, 35))
        self.nombre2 = TextCtrl(p2, -1, "Nombre", size=(-1, 35))
        self.comision2 = TextCtrl(p2, -1, "Comisión", size=(-1, 35))
        self.sexo2 = TextCtrl(p2, -1, "Sexo", size=(-1, 35))
        self.fnac2 = TextCtrl(p2, -1, "Fecha de Nacimiento", size=(-1, 35))
        col2.Add(self.dni2)
        col2.Add(self.nombre2)
        col2.Add(self.comision2)
        col2.Add(self.sexo2)
        col2.Add(self.fnac2)

        s = BoxSizer(HORIZONTAL)
        s.Add(col1)
        s.Add(col2)
        b = Button(p2, -1, "&Alta")

        b.Bind(EVT_BUTTON, self.altaBD)
        s.Add(b, 1, ALL|EXPAND, 20)
        p2.SetSizer(s)
        f2.Show()

    def altaBD(self, event):
        dni = self.dni2.GetValue()
        nombre = self.nombre2.GetValue()
        comision = self.comision2.GetValue()
        sexo = self.sexo2.GetValue()
        fnac = self.fnac2.GetValue()
        self.dvlc.AppendItem(["0", dni, nombre, comision, sexo, fnac])
        con = sqlite3.connect("alumnos2020.db")
        cur = con.cursor()
        alta = f"INSERT INTO datos (dni, nombre, comision, sexo, fnac) VALUES ('{dni}', '{nombre}', '{comision}', '{sexo}', '{fnac}')"
        cur.execute(alta)
        con.commit()
        con.close()

    def borrar(self, event):
        def borraBD(id):
            con = sqlite3.connect("alumnos2020.db")
            cur = con.cursor()
            dele = f"DELETE from datos WHERE id={id}"
            cur.execute(dele)
            con.commit()
            con.close()
        row = self.dvlc.GetSelectedRow()
        id = self.dvlc.GetTextValue(row, 0)
        self.dvlc.DeleteItem(row)
        borraBD(id)


prog = MyApp()
prog.MainLoop()
