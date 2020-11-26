import requests

myUrl = 'https://www.dolarhoy.com'
resp = requests.get(myUrl)
resp = resp.text

blue = resp.find("cotizaciondolarblue")
blueCompra = resp[blue+241: blue+244]
blueVenta = resp[blue+413: blue+416]

cotizacionBlue = (f"Compra: ${blueCompra} - Venta: ${blueVenta}")
