##https://drive.google.com/drive/folders/1VPxvRZatGDDr7GYYOQXMUlWKwI2SioMf?usp=sharing

from wx import * 
import random

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, 1, 'Casino')
        self.p = Panel(f)
        f.SetDimensions(0, 0, 1920, 1080)
        self.bmp = Bitmap("H:/Mi Carpeta/Universidad/Programacion/EFI/Menú/Botones/CNP/atras.jpg", BITMAP_TYPE_ANY)
        self.button = BitmapButton(self.p, id = 1, bitmap = self.bmp, size =(self.bmp.GetWidth(), self.bmp.GetHeight())) 
        self.button.Bind(EVT_BUTTON, self.atras)
        self.button.SetPosition((70, 870))
        bmpJ = Bitmap('H:/Mi Carpeta/Universidad/Programacion/EFI/Menú/Botones/CNP/jugar.jpg',BITMAP_TYPE_ANY) 
        buttonJ = BitmapButton(self.p, id = 2, bitmap = bmpJ, size =(bmpJ.GetWidth(), bmpJ.GetHeight())) 
        buttonJ.Bind(EVT_BUTTON, self.jugar) 
        buttonJ.SetPosition((1000, 465)) 
        fondo = StaticBitmap(self.p, -1, Bitmap("H:/Mi Carpeta/Universidad/Programacion/EFI/Menú/1 - Menu - Game.jpg", BITMAP_TYPE_ANY), pos = Point(0, 0), size = (1920, 1080))
        f.Show()
        f.ShowFullScreen(True)
        return True
    
    def jugar (self,event):
        print('Jugar')
        self.f2 = Frame (None, 2)
        p2 = Panel(self.f2)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p2, -1, 'Cantidad de Monedas iniciales')
        self.tc1 = TextCtrl(p2, -1, '0')
        bt1 = Button(p2, 1, 'set')
        bt1.Bind(EVT_BUTTON, self.setCoins)
        s.Add(st1,0, ALL|EXPAND, 10)
        s.Add(self.tc1, 0, ALL|EXPAND, 10)
        s.Add(bt1, 0 , ALL|EXPAND, 10)
        p2.SetSizer(s)
        self.f2.Show()
        return True
  
    def setCoins(self,event):
        self.coinsInicio = int(self.tc1.GetValue())
        print(self.coinsInicio)
        self.f2.Destroy()
        self.coinflip()
    
    def coinflip(self):
        self.f3 = Frame(None, -1)
        p3 = Panel(self.f3)
        self.f3.SetDimensions(0, 0, 1920, 1080)
        s = BoxSizer(VERTICAL)
        self.bmp = Bitmap("H:/Mi Carpeta/Universidad/Programacion/EFI/Menú/Botones/CNP/atrasc.jpg", BITMAP_TYPE_ANY)
        self.button = BitmapButton(p3, id = 3, bitmap = self.bmp, size =(self.bmp.GetWidth(), self.bmp.GetHeight())) 
        self.button.Bind(EVT_BUTTON, self.atras)
        self.button.SetPosition((70, 875))
        coinsActuales = str(self.coinsInicio)
        st1 = StaticText(p3, -1, label = coinsActuales, size = Size(350, 50))
        s.Add(st1,ALL|CENTER, 100)
        st1.SetPosition((1250, 80))
        fondoCoinflip = StaticBitmap(p3, -1, Bitmap("H:/Mi Carpeta/Universidad/Programacion/EFI/Coinflip/Plantilla Fondo.jpg", BITMAP_TYPE_ANY), pos = Point(0, 0), size = (1920, 1080))
        p3.SetSizer(s)
        self.f3.Show()
        self.f3.ShowFullScreen(True)
        
        return True
    
    def coc (self, event):
        self.coc = int
        id = event.GetId()
        if id == 11:
            self.coc = 1
            print('cara')
        if id == 12:
            self.coc = 2
            print('Cruz')
        return self.coc
        
    def start (self,event):
        self.x = random.randint(1,2)
        print(self.x)
        self.apuesta = int(self.bet.GetValue())
        if self.x == self.coc:
            self.coinsInicio = self.coinsInicio + self.apuesta
            print(f'Ganaste {self.apuesta}')
            self.flip()
        else:
            self.coinsInicio = self.coinsInicio - self.apuesta
            print(f'Perdiste {self.apuesta}')
            self.flip()
        
    def flip(self):
        self.resultado = Frame(None, 14, 'Resultado')
        p4 = Panel(self.resultado)
        s = BoxSizer(VERTICAL)
        if self.coc == self.x:
            st1 = StaticText(p4, -1, (f'Ganaste {self.apuesta},ahora tienes un total de {self.coinsInicio}'))
            s.Add(st1,0,ALL|CENTER,10)
        else:
            st2 = StaticText(p4, -1, (f'Perdiste {self.apuesta}, ahora tienes un total de {self.coinsInicio}'))
            s.Add(st2, 0,ALL|CENTER,10)
        self.bt1Close = Button(p4, -1, 'Atras')
        self.bt1Close.Bind(EVT_BUTTON, self.atras)
        s.Add(self.bt1Close, 0,ALL|CENTER,10)
        p4.SetSizer(s)
        self.resultado.Show()
        return True

    def atras(self,event):
        id = event.GetId()
        if id == 1:
            self.f.Destroy()
            print("Salir")
        elif id == 3:
            self.f3.Destroy()
            print("Atras")
        elif id == 14:
            self.resultado.Destroy()
            print("Atras")


app = MyApp()
app.MainLoop()
