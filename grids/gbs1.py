from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = GridBagSizer(10, 10)
        st1 = StaticText(p, -1, 'Nombre')
        tc1 = TextCtrl(p)
        
        flags = TOP|ALIGN_CENTER
        s.Add(st1, (0,0), (1, 1), ALL|EXPAND, 10)
        s.Add(tc1, (0,1), (1, 2), ALL|EXPAND, 10)

        l_adi = StaticText(p, -1, "Adicionales")
        s.Add(l_adi, (1,0), (1, 1), flag=flags, border=5)

        adi1 = self.adi1 = CheckBox(p, -1, "&Cena")
        adi2 = self.adi2 = CheckBox(p, -1, "Sala VIP")
        s.Add(adi1, pos = (1, 1), span = (1, 1))
        s.Add(adi2, pos = (1, 2), span = (1, 1))




        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print('label')


app = MyApp()
app.MainLoop()
