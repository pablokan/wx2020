import wx


musicdata = {0: (1, 'aaa', 'aaaaaa', 'aaaaaaaaa'), 1: (1, 'bbb', 'bbbbbb', 'bbbbbbbbb'), 2: (1, 'ccc', 'cccccc', 'ccccccccc') }
#----------------------------------------------------------------------

class CheckListCtrl(wx.ListCtrl):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)


    def OnItemActivated(self, evt):
        self.ToggleItem(evt.Index)


    # this is called by the base class when an item is checked/unchecked
    def OnCheckItem(self, index, flag):
        data = self.GetItemData(index)
        title = musicdata[data][1]
        if flag:
            what = "checked"
        else:
            what = "unchecked"
        print (f'item {title}, at index {index} was {what}\n')



class TestPanel(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1)

        self.list = CheckListCtrl(self)
        sizer = wx.BoxSizer()
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.list.InsertColumn(0, "Id")
        self.list.InsertColumn(1, "Artist")
        self.list.InsertColumn(2, "Title", wx.LIST_FORMAT_RIGHT)
        self.list.InsertColumn(3, "Genre")

        for key, data in musicdata.items():
            index = self.list.InsertItem(self.list.GetItemCount(), data[0])
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2, data[2])
            self.list.SetItem(index, 3, data[3])
            self.list.SetItemData(index, key)

        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, 100)

        ### self.list.CheckItem(1)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected, self.list)


    def OnItemSelected(self, evt):
        print ('item selected: %s\n' % evt.Index)

    def OnItemDeselected(self, evt):
        print ('item deselected: %s\n' % evt.Index)


#----------------------------------------------------------------------

    
class MyApp(wx.App):
    def OnInit(self):
        self.diag = TestPanel()
        self.SetTopWindow(self.diag)
        self.diag.Layout()
        self.diag.Show()
        self.diag.CenterOnScreen()
        return True
    
app = MyApp()
app.MainLoop()
