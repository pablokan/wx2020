from wx import *
from wx.dataview import * 
import sqlite3


class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Alumnos", size=(700, 500))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = DataViewListCtrl(p1)
        
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn('DNI', width=130)
        dvlc.AppendTextColumn('Nombre', width=250, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Comisión', width=75, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Sexo', width=75)
        dvlc.AppendTextColumn('F. Nac.', width=100)


        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Carga de archivo")
        bA = Button(p1, 1001, "&Alta")
        hor.Add(b)
        hor.Add(bA)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.cargaDatos)
        bA.Bind(EVT_BUTTON, self.altaOmodi)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()

        dvlc.Bind(EVT_DATAVIEW_SELECTION_CHANGED, self.sele)
        dvlc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.altaOmodi)
        dvlc.Bind(EVT_DATAVIEW_ITEM_EDITING_DONE, self.OnEditingDone)
        dvlc.Bind(EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.OnValueChanged)

        return True

    def sele(self, evt):
        row = self.dvlc.GetSelectedRow()
        print(row)
        print("Nombre", self.dvlc.GetTextValue(row, 2))
        print("Comisión", self.dvlc.GetTextValue(row, 3))

    def OnEditingDone(self, evt):
        print("OnEditingDone")

    def OnValueChanged(self, evt):
        print("OnValueChanged")
        row = self.dvlc.GetSelectedRow()
        print(row)
        dni = self.dvlc.GetTextValue(row, 1)
        nombre = self.dvlc.GetTextValue(row, 2)
        comision = self.dvlc.GetTextValue(row, 3)
        sexo = self.dvlc.GetTextValue(row, 4)
        fnac = self.dvlc.GetTextValue(row, 5)
        id = self.dvlc.GetTextValue(row, 0)
        print(nombre)
        self.grabaBD(id, dni, nombre, comision, sexo, fnac)
       
    def GetValueByRow(self, row, col):
        return self.data[row][col]

    def altaOmodi(self, event):
        if event.GetId() == 1001:
            etiq = ["DNI", "Nombre", "Comisión", "Sexo", "F.Nac."]
        elif event.GetId() == 1001:
            etiq = []
        f = Frame(None)

        pass

    
    def cargaDatos(self, e):
        lista = self.recupBD()
        #print(lista)
        for e in lista:
            self.dvlc.AppendItem(e)

    def recupBD(self):
        con = sqlite3.connect("alumnos.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM datos ORDER BY Nombre")
        tuplas = cur.fetchall()
        #print(tuplas)
        listaA = [list(e) for e in tuplas]
        #print(listaA)
        for e in listaA:
            e[0] = str(e[0])
        con.close()
        return listaA

    def grabaBD(self, id, dni, nombre, comision, sexo, fnac):
        con = sqlite3.connect("alumnos.db")
        cur = con.cursor()
        actu = "UPDATE datos SET dni = '" + dni + "' , nombre = '" + nombre + "' WHERE id = " + str(id)
        print(actu)
        cur.execute(actu)
        con.commit()
        con.close()


prog = MiApp()
prog.MainLoop()
