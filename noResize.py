from wx import *

class MyApp(App):
    def OnInit(self):
        no_resize = DEFAULT_FRAME_STYLE & ~ (RESIZE_BORDER|MAXIMIZE_BOX)
        no_caption = DEFAULT_FRAME_STYLE & ~ (CAPTION|MINIMIZE_BOX|MAXIMIZE_BOX|RESIZE_BORDER|SYSTEM_MENU|CLOSE_BOX|CLIP_CHILDREN)
        f1 = Frame(None, size=(500, 500), style=no_resize)
        self.f2 = Frame(None, size=(300, 300), style=no_caption)
        panel = Panel(self.f2)
        panel.SetBackgroundColour("cyan")
        sizer = BoxSizer()
        cerrar = Button(panel, size=(100, 50), label="Cerrar")
        sizer.Add(cerrar, 0, ALL, 30)
        panel.SetSizer(sizer)
        cerrar.Bind(EVT_BUTTON, self.close)
        f1.Show()
        self.f2.Show()
        return True

    def close(self, event):
        self.f2.Close()

app = MyApp()
app.MainLoop()





        
