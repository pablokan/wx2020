from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'label')
        tc1 = TextCtrl(p)
        bt1 = Button(p, -1, 'label')
        bt1.Bind(EVT_BUTTON, self.accion)
        flags = ALL|EXPAND
        s.Add(st1, flag=flags, border=10)
        s.Add(tc1, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print('label')


app = MyApp()
app.MainLoop()
