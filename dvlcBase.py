from wx import *
from wx.dataview import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        s = BoxSizer()
        dvlc = DataViewListCtrl(p)
        dvlc.AppendTextColumn('Apellido', width=400)
        dvlc.AppendTextColumn('Nombre')
        dvlc.AppendTextColumn('Edad')
        dvlc.AppendItem(["Pérez", "Juan", "33"])
        dvlc.AppendItem(["Torres", "Etelvina", "56"])
        dvlc.AppendItem(["Sosa", "Jorge", "122"])
        s.Add(dvlc, 1, EXPAND)
        p.SetSizer(s)
        f.Show()
        return True

prog = MyApp()
prog.MainLoop()
