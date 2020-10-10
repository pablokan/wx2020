from wx import *
from wx.adv import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        sizer = BoxSizer(VERTICAL)
        f.SetSizer(sizer)

        dpc = DatePickerCtrl(f, size=(120,-1), style = DP_DROPDOWN | DP_SHOWCENTURY)
        dpc.Bind(EVT_DATE_CHANGED, self.OnDateChanged, dpc)
        sizer.Add(dpc, 0, ALL, 50)
        f.Show()
        return True

    def OnDateChanged(self, evt):
        print("OnDateChanged: %s\n" % evt.GetDate())
        d = evt.GetDate()
        print(d.FormatISODate())
        

app = MyApp()
app.MainLoop()