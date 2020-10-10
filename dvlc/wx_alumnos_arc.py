from wx import *
from wx.dataview import * 


class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Alumnos", size=(670, 500))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = DataViewListCtrl(p1)
        encabezado = [('DNI', 130), ('Nombre', 250), ('Comisión', 75), ('Sexo', 75), ('F.Nac', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Carga de archivo")
        bA = Button(p1, -1, "&Alta")
        hor.Add(b)
        hor.Add(bA)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.cargaArchivo)
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

    def cargaArchivo(self, e):
        lista = []
        with open("alumnos-python.csv", "r") as archivo:
            first = True
            for line in archivo:
                if first:
                    first = False
                else:
                    print(line,)
                    line = line[:-1]
                    lista.append(line)

        for e in lista:
            e = e.split(",")
            print(e)
            e.pop(0)
            print(e)

            self.dvlc.AppendItem(e)


prog = MiApp()
prog.MainLoop()
