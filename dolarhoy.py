import requests
from wx import *
from datetime import datetime

class MyApp(App):
    def OnInit(self):
        myUrl = 'https://www.dolarhoy.com'
        resp = requests.get(myUrl)
        resp = resp.text 
        blue = resp.find("cotizaciondolarblue")
        blueCompra = "$" + resp[blue+241: blue+244]
        blueVenta = "$" + resp[blue+413: blue+416]
        ahora = 'Cotización dólar blue ' + str(datetime.now())[:16] + "      "
        f = Frame(None, -1, ahora, size=(-1, 120 ))
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        compra = "Compra: " + blueCompra
        venta = " Venta: " + blueVenta
        st1 = StaticText(p, -1, compra)
        s.Add(st1, 0, ALL|ALIGN_CENTER, 10)
        st2 = StaticText(p, -1, venta)
        s.Add(st2, 0, ALL|ALIGN_CENTER, 10)
        p.SetSizer(s)
        f.Show()
        return True


app = MyApp()
app.MainLoop()
