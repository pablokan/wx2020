# Ejemplo base de ListCtrl
from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'ListCtrl')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'ListCtrl')


        self.lc1 = lc1 = ListCtrl(p,  style = LC_REPORT)
        lc1.InsertColumn(0, "Nombre")
        lc1.InsertColumn(1, "Edad")
        lc1.InsertColumn(2, "Comisión")
        personas = [("Juan", "30", "A"), ("Ana", "40", "B")]
        i = 0
        for e in personas:
            index = lc1.InsertItem(i, e[0])
            lc1.SetItem(index, 1, e[1])
            lc1.SetItem(index, 2, e[2])
            i += 1

        lc1.Bind(EVT_LIST_ITEM_SELECTED, self.seleccion)
        s.Add(st1, 0, ALL|EXPAND, 10)
        s.Add(lc1, 0, ALL|EXPAND, 10)
        p.SetSizer(s)
        f.Show()
        return True


    def seleccion(self, event):
        fila = event.Index
        print(fila, self.lc1.GetItemText(fila))

app = MyApp()
app.MainLoop()

