from wx import *
from datetime import *
from wx.adv import *


class MyApp(App):
    def OnInit(self):
        frame = Frame(None)
        panel = Panel(frame)
        sizer = BoxSizer(VERTICAL)
        panel.SetSizer(sizer)

        dpc1 = DatePickerCtrl(panel)
        dpc1.Bind(EVT_DATE_CHANGED, self.OnDateChanged, dpc1)
        sizer.Add(dpc1, 0, ALL, 50)
        print(date(date.today.Format("%d-%m-%Y")))
        #self.sel_date = date(date.today())
        diaInicial = date(1989,1,1)
        diaFinal = date(2002,6,30)
        dpc2 = DatePickerCtrl(panel, style = DP_DEFAULT|DP_SHOWCENTURY)
        #dpc2.SetRange(self.sel_date, diaFinal)
        dpc2.Bind(EVT_DATE_CHANGED, self.OnDateChanged, dpc2)
        sizer.Add(dpc2, 0, LEFT, 50)
        frame.Show()
        return True
        
    def OnDateChanged(self, e):
        self.sel_date = e.GetDate()
        print (self.sel_date.Format("%d-%m-%Y"))


app = MyApp()
app.MainLoop()
