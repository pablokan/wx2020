from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(770, 516))
        p = Panel(f)
        jpg = Image('peyton.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        bitmap = StaticBitmap(p, -1, jpg)
        s = BoxSizer(VERTICAL)
        ib1 = Image("em01.jpg", BITMAP_TYPE_ANY).ConvertToBitmap()
        ib2 = Image("em02.jpg", BITMAP_TYPE_ANY).ConvertToBitmap()
        b1 = BitmapButton(p, -1, ib1)
        b2 = BitmapButton(p, -1, ib2)
        s.Add(b1, 0, ALL|ALIGN_RIGHT, 30)
        s.Add(b2, 0, ALL|ALIGN_RIGHT, 30)
        p.SetSizer(s)
        f.Show()
        return True

app = MyApp()
app.MainLoop()
