from wx import *
from wx.adv import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'label')
        dp =self.fna = DatePickerCtrl(p, size=(120,-1), style = DP_DROPDOWN | DP_SHOWCENTURY)
        dp.Bind(EVT_DATE_CHANGED, self.OnDateChanged, dp)
        tc1 = TextCtrl(p)
        bt1 = Button(p, -1, 'label')
        bt1.Bind(EVT_BUTTON, self.accion)
        s.Add(st1, 0, ALL|EXPAND, 10)
        s.Add(dp, 0, ALL, 10)
        s.Add(tc1, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def OnDateChanged(self, evt):
        print(evt.GetDate())
        d = evt.GetDate()
        print(d.FormatISODate())

    def accion(self, event):
        print('label')


app = MyApp()
app.MainLoop()
