from wx import *
from wx.dataview import * 
import sqlite3


class MyApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Alumnos", size=(700, 500))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = DataViewListCtrl(p1)
        encabezado = [('#', 30), ('DNI', 130), ('Nombre', 250), ('Comisión', 75), ('Sexo', 75), ('F.Nac', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Carga de archivo")
        bA = Button(p1, -1, "&Alta")
        hor.Add(b)
        hor.Add(bA)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.cargaDatos)
        bA.Bind(EVT_BUTTON, self.alta)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()

        dvlc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.borrarOmodif)
        return True

    def alta(self, event):
        pass

    def borrarOmodif(self, event):
        dlg = Dialog(None, -1, "Borrar o Modificar?")
        box = BoxSizer(VERTICAL)
        optList = ["Modificar", "Borrar"]
        opt = self.opt = RadioBox(dlg, -1, choices=optList)
        box.Add(opt, 0, ALIGN_CENTER | ALL, 30)
        okB = Button(dlg, ID_OK)
        caB = Button(dlg, ID_CANCEL)
        box.Add(okB, 0, ALIGN_CENTER | ALL, 30)
        box.Add(caB, 0, ALIGN_CENTER | ALL, 30)
        dlg.SetSizer(box)
        if dlg.ShowModal() == ID_OK:
            if opt.GetSelection() == 0:
                pass
            else:
                self.dvlc.DeleteItem(self.dvlc.GetSelectedRow())

    def cargaDatos(self, e):
        lista = self.recupBD()
        print(lista)
        for e in lista:
            self.dvlc.AppendItem(e)

    def recupBD(self):
        con = sqlite3.connect("alumnos.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM datos ORDER BY Nombre")
        tuplas = cur.fetchall()
        print(tuplas)
        listaA = [list(e) for e in tuplas]
        #print(listaA)
        for e in listaA:
            e[0] = str(e[0])
        con.close()
        return listaA


prog = MyApp()
prog.MainLoop()
