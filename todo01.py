import wx

PADDING = 10

class App(wx.App):
    def OnInit(self):
        self.data = [
            {'title':'1st', 'content':'First'},
            {'title':'2nd', 'content':'Second'},
            {'title':'3rd', 'content':'Third'},
        ]
        frame = ListFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

class ListFrame(wx.Frame):
    def __init__(self, title="List", size=(250, 500)):
        wx.Frame.__init__(self, None, -1, title=title, size=size)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label='List Title'), flag=wx.EXPAND|wx.ALL, border=PADDING)
        sizer.Add(wx.StaticLine(panel, style=wx.LI_HORIZONTAL), flag=wx.EXPAND)
        sizer.Add(ListPanel(panel), proportion=1, flag=wx.EXPAND)
        panel.SetSizer(sizer)

class ListPanel(wx.ScrolledWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.data = wx.GetApp().data
        self.SetScrollRate(0,5)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        for item in self.data:
            item_panel = ItemPanel(self, item)
            self.sizer.Add(item_panel, flag=wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=PADDING)
        self.SetSizer(self.sizer)

class ItemPanel(wx.Control):
    def __init__(self, parent, item):
        self.parent = parent
        super().__init__(self.parent)
        self.collapsed = True
        self.item = item

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        #self.panel_collapsed = wx.StaticText(self, label='> '+item['title'])
        #self.panel_expanded = wx.StaticText(self, label='v '+item['title']+'\n\t'+item['content'])
        self.panel_collapsed = ItemPanelCollapsed(self)
        self.panel_expanded = ItemPanelExpanded(self)

        self.panel_collapsed.Bind(wx.EVT_LEFT_UP, self.OnToggleView)
        self.panel_expanded.Bind(wx.EVT_LEFT_UP, self.OnToggleView)
        #self.Bind(wx.EVT_LEFT_UP, self.OnToggleView)

        self.sizer.Add(self.panel_collapsed, proportion=1, flag=wx.EXPAND)
        self.sizer.Add(self.panel_expanded, proportion=1, flag=wx.EXPAND)
        self.sizer.Hide(self.panel_expanded)
        self.SetSizer(self.sizer)

    def OnToggleView(self, event):
        if self.collapsed:
            self.sizer.Hide(self.panel_collapsed)
            self.sizer.Show(self.panel_expanded)
        else:
            self.sizer.Hide(self.panel_expanded)
            self.sizer.Show(self.panel_collapsed)
        self.collapsed = not self.collapsed
        self.sizer.Layout()
        self.parent.sizer.Layout()

class ItemPanelCollapsed(wx.Control):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_NONE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(wx.CheckBox(self, label=parent.item['title']), proportion=1, flag=wx.EXPAND)
        sizer.Add(wx.StaticText(self, label='> '+parent.item['title']), proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)

class ItemPanelExpanded(wx.Control):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_NONE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(wx.CheckBox(self, label=parent.item['title']), proportion=1, flag=wx.EXPAND)
        sizer.Add(wx.StaticText(self, label='v '+parent.item['title']), proportion=1, flag=wx.EXPAND)
        sizer.Add(wx.StaticText(self, label=parent.item['content']), proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)

if __name__ == '__main__':
    app = App(False)
    app.MainLoop()