from wx import *

class MyApp(App):
    def OnInit(self):
        #no_resize = DEFAULT_FRAME_STYLE & ~ (RESIZE_BORDER|MAXIMIZE_BOX|MINIMIZE_BOX)
        #no_resize = DEFAULT_FRAME_STYLE ^ RESIZE_BORDER
        #no_resize = MINIMIZE_BOX | CLOSE_BOX
        f = Frame(None)
        p = Panel(f, size=((500, 500)))
        p.SetBackgroundColour("red")
        #f1.SetSizeHints(200, 500, 1200, 500)
        f.SetMinSize((700, 700))
        f.SetMaxSize((700, 700))
        f.Layout()
        f.Show()
        return True


app = MyApp()
app.MainLoop()




        
