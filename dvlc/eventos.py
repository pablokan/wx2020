from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.tc1 = tc1 = TextCtrl(p)
        self.tc2 = tc2 = TextCtrl(p, style = TE_PROCESS_ENTER)
        tc1.Bind(EVT_TEXT, self.cadaLetra)
        tc2.Bind(EVT_TEXT_ENTER, self.onEnter)
        s.Add(tc1, 0, ALL|EXPAND, 10)
        s.Add(tc2, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def cadaLetra(self, event):
        print(self.tc1.GetValue())

    def onEnter(self, event):
        print(self.tc2.GetValue())


app = MyApp()
app.MainLoop()
