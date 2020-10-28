from wx import *


class MyApp(App):
    def OnInit(self):
        cA = self.cuantosSon()
        liAsis = self.carga(cA)
        self.liGuita = liGuita = []

        for i in range(len(liAsis)):
            boxMain = BoxSizer(VERTICAL)
            self.d = d = Dialog(None, size=(1000, 100))
            p = Panel(d)
            nombre = StaticText(p, -1, str(liAsis[i]))
            self.compraA = compraA = CheckBox(p, 1001, "Asado")
            self.compraV = compraV = CheckBox(p, 1002, "Vino")
            self.compraP = compraP = CheckBox(p, 1003, "Pan")
            compraA.Bind(EVT_CHECKBOX, self.habCarga)
            compraV.Bind(EVT_CHECKBOX, self.habCarga)
            compraP.Bind(EVT_CHECKBOX, self.habCarga)
            self.costoA = costoA = TextCtrl(p, -1)
            self.costoV = costoV = TextCtrl(p, -1)
            self.costoP = costoP = TextCtrl(p, -1)
            costoA.Disable()
            costoV.Disable()
            costoP.Disable()
            boxFila = BoxSizer(HORIZONTAL)
            boxFila.Add(nombre, 0, ALIGN_CENTER | ALL, 20)
            boxFila.Add(compraA, 0, ALIGN_CENTER | ALL, 20)
            boxFila.Add(costoA, 0, ALIGN_CENTER | ALL, 20)
            boxFila.Add(compraV, 0, ALIGN_CENTER | ALL, 20)
            boxFila.Add(costoV, 0, ALIGN_CENTER | ALL, 20)
            boxFila.Add(compraP, 0, ALIGN_CENTER | ALL, 20)
            boxFila.Add(costoP, 0, ALIGN_CENTER | ALL, 20)
            cCosto = Button(p, -1, "Carga gastos")
            boxFila.Add(cCosto, 0, ALIGN_CENTER | ALL, 20)
            cCosto.Bind(EVT_BUTTON, self.cargaCosto)
            boxMain.Add(boxFila)
            p.SetSizer(boxMain)
            d.ShowModal()
        print(liGuita)
        total = 0
        for z in range(len(liAsis)):
            total += liGuita[z]
        pCabeza = total / cA
        for z in range(len(liAsis)):
            print(liAsis[z], liGuita[z]-pCabeza)
        self.mostrar(liAsis, liGuita, pCabeza)
        return True

    def mostrar(self, liAsis, liGuita, pCabeza):
        f = Frame(None)
        p = Panel(f)
        boxV = BoxSizer(VERTICAL)
        for z in range(len(liAsis)):
            boxH = BoxSizer(HORIZONTAL)
            liA = StaticText(p, -1, liAsis[z])
            saldo = liGuita[z]-pCabeza
            poner = StaticText(p, -1, str(saldo))
            colorete = (0,0, 255)
            if saldo < 0:
                colorete = (255,0,0)
            else:
                colorete = (0, 255, 0)
            poner.SetForegroundColour(colorete)
            boxH.Add(liA, 0, ALIGN_CENTER | ALL, 10)
            boxH.Add(poner, 0, ALIGN_CENTER | ALL, 10)
            boxV.Add(boxH)
        p.SetSizer(boxV)
        f.Show()

    def habCarga(self, event):
        if event.GetId() == 1001:
            self.costoA.Enable()
        if event.GetId() == 1002:
            self.costoV.Enable()
        if event.GetId() == 1003:
            self.costoP.Enable()

    def cargaCosto(self, event):
        suma = 0
        if self.compraA.GetValue():
            suma +=  int(self.costoA.GetValue())
        if self.compraV.GetValue():
            suma +=  int(self.costoV.GetValue())
        if self.compraP.GetValue():
            suma +=  int(self.costoP.GetValue())
        print(suma)
        self.d.Destroy()
        self.liGuita.append(suma)

    def cuantosSon(self):
        dlgCant = TextEntryDialog(None, 'Cuantos asistentes?', "Asado")
        cA = 0
        if dlgCant.ShowModal() == ID_OK:
            cA = int(dlgCant.GetValue())
            dlgCant.Destroy()
        return cA

    def carga(self, cA):
        dlgCargaBD = Dialog(None, -1, "Asistentes al asado")
        box = BoxSizer(VERTICAL)
        listaA = []
        for i in range(cA):
            asis = TextCtrl(dlgCargaBD)
            listaA.append(asis)
            box.Add(asis, 0, ALIGN_CENTER | ALL, 10)
        okB = Button(dlgCargaBD, ID_OK)
        caB = Button(dlgCargaBD, ID_CANCEL)
        box.Add(okB, 0, ALIGN_CENTER | ALL, 10)
        box.Add(caB, 0, ALIGN_CENTER | ALL, 10)
        dlgCargaBD.SetSizer(box)
        lista = []
        if dlgCargaBD.ShowModal() == ID_OK:
            for e in listaA:
                lista.append(e.GetValue())
        return lista


prog = MyApp()
prog.MainLoop()
