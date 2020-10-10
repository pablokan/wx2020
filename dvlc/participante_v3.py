from wx import *
from wx.dataview import *
from wx.adv import *


class MiApp(App):
    def OnInit(self):
        f1 = Frame(None)
        p1 = self.p1 = Panel(f1)
        self.dvlc = dvlc = DataViewListCtrl(p1)
        dvlc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.editar)
        encabezado = [('Apellido', 150), ('Nombre', 150)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Agregar participante")
        bf = Button(p1, -1, "Nada")
        hor.Add(b)
        hor.Add(bf)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.editar)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()
        return True

    def editar(self, e):
        print(e.GetEventType())
        f2 = Frame(None, -1, "Agregar participante", size = (350, 300))
        p2 = self.p2 = Panel(f2)
        grilla = GridBagSizer(5,5)
# Apellido - Caja de Texto
        l_ape = StaticText(p2, -1, "Apellido")
        grilla.Add(l_ape, pos=(0,0))
        ape = self.ape = TextCtrl(p2, -1, "Acá va el Apellido")
        grilla.Add(ape, pos=(0,1))
# Nombre - Caja de Texto
        l_nom = StaticText(p2, -1, "Nombre")
        grilla.Add(l_nom, pos = (1,0))
        nom = self.nom =TextCtrl(p2, -1, "Acá va el Nombre")
        grilla.Add(nom, pos = (1,1))
# Botón Guardar
        guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (3, 1))
        guardar.Bind(EVT_BUTTON, self.guardaPart)

# Muestra la grilla
        p2.SetSizerAndFit(grilla)
        f2.Show()
#Guarda el participante
    def guardaPart(self, evt):
        ap = self.ape.GetValue()
        no = self.nom.GetValue()
        self.dvlc.AppendItem([ap, no])


prog = MiApp()
prog.MainLoop()
