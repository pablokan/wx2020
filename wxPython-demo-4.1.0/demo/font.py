from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'label')
        fnt = Font(pointSize = 40, family = FONTFAMILY_SWISS, style = FONTSTYLE_NORMAL, weight = FONTWEIGHT_LIGHT)
        st1.SetFont(fnt)
        tc1 = TextCtrl(p)
        bt1 = Button(p, -1, 'label')
        bt1.Bind(EVT_BUTTON, self.accion)
        s.Add(st1, 0, ALL|EXPAND, 10)
        s.Add(tc1, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print('label')


app = MyApp()
app.MainLoop()
