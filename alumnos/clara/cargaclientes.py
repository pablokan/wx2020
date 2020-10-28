from wx import *
from wx.dataview import * 
import sqlite3


class MyApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Clientes", size=(700, 500))
        p1 = self.p1 = Panel(f1)
        self.dvlc = dvlc = DataViewListCtrl(p1)
        dvlc.Bind(EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.modif)
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn('DNI', width=130)
        dvlc.AppendTextColumn('Nombre', width=250, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('F. Nac.', width=100)

        for c in self.dvlc.Columns:
            c.Sortable = True
            c.Reorderable = True

        self.search = search = SearchCtrl(p1, size=(150, 33))
        search.Hide()
        search.ShowCancelButton(True)
       
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        sizer.Add(search, 0, EXPAND)
        search.Bind(EVT_TEXT, self.buscar)
        p1.SetSizer(sizer)

#
        f1.CreateStatusBar()
        f1.SetStatusText("...")

        menuBar = MenuBar()

        menu1 = Menu()
        menu1.Append(101, "&Carga", "Carga listado completo de clientes")
        menu1.Append(102, "&Alta", "Insertar un cliente nuevo")
        menu1.AppendSeparator()
        menu1.Append(103, "&Eliminar", "Borrar fila")
        menu1.AppendSeparator()
        menu1.Append(104, "&Buscar", "Buscar cliente por nombre")
        menu1.Append(105, "&Salir", "Cerrar el programa")
        menuBar.Append(menu1, "&Archivo")

        menu2 = Menu()
        menu2.Append(201, "Documentación")
        menu2.Append(202, "Acerca de")
        menuBar.Append(menu2, "a&Yuda")

        f1.SetMenuBar(menuBar)

        idList = [101, 102, 103, 104, 105, 201, 202]
        for e in idList:
            f1.Bind(EVT_MENU, self.accion, id=e)        

        f1.Show()
        return True

    def accion(self, event):
        id = event.GetId()
        if id == 101:
            self.cargaDatos()
        if id == 102:
            self.alta()
        if id == 103:
            self.borrar()
        if id == 104:
            self.search.Show()
            self.p1.Layout()
            self.search.SetFocus()
        if id == 201:
            f2 = Frame(None, size=(600, 100))
            f2.Show()
        if id == 202:
            print("opción 'Acerca de'")
        if id == 105:
            self.f.Close()

    def buscar(self, event):
        print("--------------------------")
        busco = self.search.GetValue()
        num = self.search.GetLastPosition()
        tot = self.dvlc.GetItemCount()
        for i in range(tot):
            self.dvlc.DeleteItem(0)

        for i in range(len(self.busqueda)):
            if busco == self.busqueda[i][2][:num]:
                self.dvlc.AppendItem(self.busqueda[i])
                print("#", self.busqueda[i][2])

    def cargaDatos(self):
        def recupBD():
            con = sqlite3.connect("Clientes01.db")
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
        self.busqueda = lista

    def modif(self, evt):
        def grabaBD(id, dni, nombre, fnac):
            con = sqlite3.connect("Clientes01.db")
            cur = con.cursor()
            actu = f"UPDATE datos SET dni='{dni}', nombre='{nombre}' WHERE id={id}"
            cur.execute(actu)
            con.commit()
            con.close()

        row = self.dvlc.GetSelectedRow()
        id = self.dvlc.GetTextValue(row, 0)
        dni = self.dvlc.GetTextValue(row, 1)
        nombre = self.dvlc.GetTextValue(row, 2)
        fnac = self.dvlc.GetTextValue(row, 4)
        grabaBD(id, dni, nombre, fnac)

    def alta(self):
        self.f2 = f2 = Frame(None, -1, "Alta")
        p2 = Panel(f2)
        col1 = BoxSizer(VERTICAL)
        dni1 = StaticText(p2, label="DNI", size=(-1, 35))
        nombre1 = StaticText(p2, label="Nombre", size=(-1, 35))
        fnac1 = StaticText(p2, label="Fecha de Nacimiento   ", size=(-1, 35))
        col1.Add(dni1,1, TOP, 10)
        col1.Add(nombre1)
        col1.Add(fnac1)

        col2= BoxSizer(VERTICAL)
        self.dni2 = TextCtrl(p2, -1, "DNI", size=(-1, 35))
        self.nombre2 = TextCtrl(p2, -1, "Nombre", size=(-1, 35))
        self.fnac2 = TextCtrl(p2, -1, "Fecha de Nacimiento", size=(-1, 35))
        col2.Add(self.dni2)
        col2.Add(self.nombre2)
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
        fnac = self.fnac2.GetValue()
        self.dvlc.AppendItem(["0", dni, nombre, fnac])
        con = sqlite3.connect("Clientes01.db")
        cur = con.cursor()
        alta = f"INSERT INTO datos (dni, nombre, fnac) VALUES ('{dni}', '{nombre}', '{fnac}')"
        cur.execute(alta)
        con.commit()
        con.close()
        self.f2.Close()

    def borrar(self):
        def borraBD(id):
            con = sqlite3.connect("Clientes01.db")
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