from wx import *
import wx.html2 as webview

#----------------------------------------------------------------------

class Web(Panel):
    def __init__(self, parent, direccionWeb):
        Panel.__init__(self, parent, -1)
        self.current = direccionWeb
        sizer = BoxSizer(VERTICAL)
        btnSizer = BoxSizer(HORIZONTAL)
        self.wv = webview.WebView.New(self)
        sizer.Add(self.wv, 1, EXPAND)
        self.SetSizer(sizer)

        b = Button(self, -1, "Refrescar Página", style=BU_EXACTFIT)
        self.Bind(EVT_BUTTON, self.botonRefrescar, b)
        sizer.Add(btnSizer, 0, EXPAND)
        btnSizer.Add(b, 0, EXPAND|ALL, 2)

        self.wv.LoadURL(self.current)

    def botonRefrescar(self, evt):
        self.wv.Reload()


