from wx import *

class MyApp(App):
    def OnInit(self):
        f = self.f = Frame(None, -1, "")
        p = self.p = Panel(f, -1)
        gbs = self.gbs = GridBagSizer(50, 50)
        botonList = self.botonList = []
        constrList = self.constrList = ["casa", "hospital", "policia"]
        imagenList = self.imagenList = ["casa.jpg", "hospital.jpg", "policia.jpg"]
        for self.x in range(3):
            botonLabel = constrList[self.x]
            b = Button(p, 1000+self.x, botonLabel)
            botonList.append(b)
            gbs.Add(b, (0, self.x))
            botonList[self.x].Bind(EVT_BUTTON, self.onClick)
        box = BoxSizer()
        box.Add(gbs, 1, ALL|EXPAND, 10)
        p.SetSizer(box)
        f.Show()
        return True

    def onClick(self, e):
        ident = e.GetId() - 1000
        if self.gbs.CheckForIntersectionPos( (1, ident), (1, 1)):
            wx.MessageBox("Ya ta este!!!", "Naaaaaaaaaaaaa", OK)
        else:
            imagen = Image(self.imagenList[ident]).ConvertToBitmap()
            sbm = StaticBitmap(self.p, -1, imagen, (10, 10))
            self.gbs.Add(sbm, (1,ident))
            self.gbs.Layout()

app = MyApp()
app.MainLoop()
