from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'title')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'label')
        sampleList = ["1", "2", "3"]
        self.lb1 = ListBox(p)
        list2 = ["4", "5"]
        self.lb1.SetItems(list2)
        bt1 = Button(p, -1, 'label')
        bt1.Bind(EVT_BUTTON, self.accion)
        s.Add(st1, 0, ALL|EXPAND, 10)
        s.Add(self.lb1, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0, ALL|EXPAND, 10)
        
        p.SetSizer(s)
        f.Show()
        return True

    def accion(self, event):
        print('label')


app = MyApp()
app.MainLoop()




