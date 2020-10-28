from wx import *

class MyApp(App):
    def OnInit(self):
         frame = Frame(None, size=(500, 800))
         panel = Panel(frame)
         panel1 = Panel(panel, pos=(0,0), size=(-1, 400))
         panel1.SetBackgroundColour((255,0,0,100))
         button1 = Button(panel1, -1, label="Saludar")
         button1.Bind(EVT_BUTTON, self.mostrar)

         panel2 = Panel(panel, pos=(0,400), size=(-1, 400))
         panel2.SetBackgroundColour('red')
         self.st = StaticText(panel2)
         sizer = BoxSizer(VERTICAL)
         sizer.Add(panel1,0,EXPAND|ALL,border=10)
         sizer.Add(panel2,0,EXPAND|ALL,border=10)
         panel.SetSizer(sizer)
         frame.Show(True)
         return True

    def mostrar(self, event):
        self.st.SetLabel("Hi students!")


app = MyApp()
app.MainLoop()