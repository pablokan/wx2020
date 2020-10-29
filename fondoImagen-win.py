from wx import *

class MyApp(App):

    def OnInit(self):
        f = Frame(None,-1, size=(770, 516))
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        imageFile = 'peyton.jpg'
        bmp1 = Image(imageFile ,BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = StaticBitmap(p, -1, bmp1,(0, 0))
        str1 = '%s %dx%d' % (imageFile, bmp1.GetWidth(), bmp1.GetHeight())
        botonFondo = 'em01.jpg'
        bmp2 = Image(botonFondo,BITMAP_TYPE_ANY).ConvertToBitmap()
        boton = BitmapButton(self.bitmap1, -1, bmp2)
        botonFondo2 = 'em02.jpg'
        bmp3 = Image(botonFondo2,BITMAP_TYPE_ANY).ConvertToBitmap()
        boton2 = BitmapButton(self.bitmap1, -1, bmp3)
        s.Add(boton,0, ALL|CENTER,30)
        s.Add(boton2,0, ALL|CENTER,30)
        p.SetSizer(s)
        f.Show()
        return True
    
app = MyApp()
app.MainLoop()