from wx import *
from wx.lib.pubsub import pub 

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        pub.subscribe(self.myListener, "myListener")
        btn = Button(p, label="Open Frame")
        btn.Bind(EVT_BUTTON, self.onOpenFrame)
        f.Show()
        return True

    def myListener(self, message, arg2=None):
        print("Received the following message: " + message)
        if arg2:
            print("Received another arguments: " + str(arg2))

    def onOpenFrame(self, event):
        self.f2 = f2 = Frame(None)
        p2 = Panel(f2)
        msg = "Enter a Message to send to the main frame"
        instructions = StaticText(p2, label=msg)
        self.msgTxt = TextCtrl(p2, value="")
        closeBtn = Button(p2, label="Send and Close")
        closeBtn.Bind(EVT_BUTTON, self.onSendAndClose)
        sizer = BoxSizer(VERTICAL)
        flags = ALL|CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(self.msgTxt, 0, flags, 5)
        sizer.Add(closeBtn, 0, flags, 5)
        p2.SetSizer(sizer)
        f2.Show()

    def onSendAndClose(self, event):
        msg = self.msgTxt.GetValue()
        pub.sendMessage("myListener", message=msg)
        pub.sendMessage("myListener", message="test2", arg2="2nd argument!")
        self.f2.Close()


app = MyApp()
app.MainLoop()
