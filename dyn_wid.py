from wx import *

class MyApp(App):
    def OnInit(self):
        self.frame = frame = Frame(parent=None, title="Add / Remove Buttons")
        self.fSizer = BoxSizer(VERTICAL)
        self.panel = panel = Panel(frame)
        self.fSizer.Add(panel, 1, EXPAND)
        panel.SetSizer(self.fSizer)
        self.number_of_buttons = 0
        self.mainSizer = BoxSizer(VERTICAL)
        controlSizer = BoxSizer(HORIZONTAL)
        self.widgetSizer = BoxSizer(VERTICAL)
        self.addButton = Button(panel, label="Add")
        self.addButton.Bind(EVT_BUTTON, self.onAddWidget)
        controlSizer.Add(self.addButton, 0, CENTER|ALL, 5)
        self.removeButton = Button(panel, label="Remove")
        self.removeButton.Bind(EVT_BUTTON, self.onRemoveWidget)
        controlSizer.Add(self.removeButton, 0, CENTER|ALL, 5)
        self.mainSizer.Add(controlSizer, 0, CENTER)
        self.mainSizer.Add(self.widgetSizer, 0, CENTER|ALL, 10)
        panel.SetSizer(self.mainSizer)
        frame.Fit()
        frame.Show()

        return True

    def onAddWidget(self, event):
        self.number_of_buttons += 1
        label = f"Button {self.number_of_buttons}" 
        name = f"button{self.number_of_buttons}" 
        new_button = Button(self.panel, label=label, name=name)
        self.widgetSizer.Add(new_button, 0, ALL, 5)
        self.fSizer.Layout()
        self.frame.Fit()

    def onRemoveWidget(self, event):
        if self.widgetSizer.GetChildren():
            self.widgetSizer.Hide(self.number_of_buttons-1)
            self.widgetSizer.Remove(self.number_of_buttons-1)
            self.number_of_buttons -= 1
            self.frame.fSizer.Layout()
            self.frame.Fit()


app = MyApp()
app.MainLoop()
