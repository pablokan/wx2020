from wx import *
from wx.dataview import DataViewListCtrl
from wx.adv import *


class MyApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Participantes", size = (770,700))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = DataViewListCtrl(p1)
        encabezado = [('Apellido', 150), ('Nombre', 150), ('Registración', 100), ('Especialidad', 150), ('Adicionales', 100), ('Importe', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Agregar participante")
        bf = Button(p1, -1, "Nada")
        hor.Add(b)
        hor.Add(bf)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.abrirAgP)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()
        return True

    def abrirAgP(self, e):
        f2 = Frame(None, title="Agregar participante", size=(300, 350))
        p2 = self.p2 = Panel(f2)
        grilla = GridBagSizer(5,5)
# Apellido - Caja de Texto
        flagsTex = TOP|ALIGN_CENTER
        flagsInp = EXPAND
        l_ape = StaticText(p2, -1, "Apellido")
        grilla.Add(l_ape, pos=(0,0), flag=flagsTex, border=5)
        ape = self.ape = TextCtrl(p2, -1, "Apellido")
        grilla.Add(ape, pos=(0,1), span = (1, 2), flag=flagsInp)
# Nombre - Caja de Texto
        l_nom = StaticText(p2, -1, "Nombre")
        grilla.Add(l_nom, pos = (1,0), flag=flagsTex, border=5)
        nom = self.nom =TextCtrl(p2, -1, "Nombre")
        grilla.Add(nom, pos = (1,1), span = (1, 2), flag=flagsInp)
# Fecha - Caja de Texto fecha de registración - Abre datepicker
        self.fe = ""
        l_fna = StaticText(p2, -1, "Registración")
        grilla.Add(l_fna, pos = (2,0), flag=flagsTex, border=5)
        fna =self.fna = DatePickerCtrl(p2, size=(120,-1), style = DP_DROPDOWN | DP_SHOWCENTURY)
        fna.Bind(EVT_DATE_CHANGED, self.OnDateChanged, fna)
        grilla.Add(self.fna, pos = (2,1), span = (1, 2), flag=flagsInp)
# Profesión - Combo
        l_pro = StaticText(p2, -1, "Especialidad")
        grilla.Add(l_pro, pos = (3,0), flag=flagsTex, border=5)
        proList = ["Arquitecto", "Analista", "Soft Dev"]
        self.pro = cb = ComboBox(p2, 500, "Especialidad", (0, 0), (-1, -1), proList, CB_DROPDOWN | TE_PROCESS_ENTER )
        cb.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.pro, pos = (3,1), span = (1, 2), flag=flagsInp)
# Adicionales - CheckBoxes
        l_adi = StaticText(p2, -1, "Adicionales")
        grilla.Add(l_adi, pos = (4,0), flag=flagsTex, border=5)
        adi1 = self.adi1 = CheckBox(p2, -1, "&Cena")
        adi2 = self.adi2 = CheckBox(p2, -1, "Sala VIP")
        grilla.Add(adi1, pos = (4, 1), span = (1, 1))
        grilla.Add(adi2, pos = (4, 2), span = (1, 1))
# Importe - Radio Buttons
        l_imp = StaticText(p2, -1, "Importe")
        grilla.Add(l_imp, pos = (5,0), flag=flagsTex, border=5)
        impList = ["$80", "$150", "$200"]
        imp = self.imp = RadioBox(p2, -1, "", DefaultPosition, DefaultSize, impList, 0, NO_BORDER)
        grilla.Add(imp, pos = (5, 1), span = (1, 1))
# Botón Guardar
        guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (6, 0), span=(1, 3), flag=EXPAND|ALL|ALIGN_CENTER, border=10)
        guardar.Bind(EVT_BUTTON, self.guardaPart)

# Muestra la grilla
        
        p2.SetSizer(grilla)
        f2.Show()
#Guarda el participante
    def guardaPart(self, evt):
        ap = self.ape.GetValue()
        no = self.nom.GetValue()
        fn = self.fe
        pr = self.pr = self.pro.GetValue()
        ad = ""
        if self.adi1.GetValue():
            ad += "Cena"
        if self.adi2.GetValue():
            ad += " VIP"
        im = self.imp.GetString(self.imp.GetSelection())
        self.dvlc.AppendItem([ap, no, fn, pr, ad, im])

# Begin Combo
    def OnKillFocus(self, evt):
        self.pr = self.pro.GetValue()
        evt.Skip()
# End Combo

# Begin Calendario
    def OnDateChanged(self, evt):
        print(evt.GetDate())
        d = evt.GetDate()
        print(d.FormatISODate())
        self.fe = d.FormatISODate()
# End Calendario

prog = MyApp()
prog.MainLoop()
