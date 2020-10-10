from wx import *

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, -1, 'Menú de Opciones')
        f.CreateStatusBar()
        f.SetStatusText("This is the statusbar")
        self.tc = tc = TextCtrl(f, style=TE_MULTILINE)
        menuBar = MenuBar()
        menu1 = Menu()
        menu1.Append(101, "&Nuevo", "Crear un archivo de texto")
        menu1.Append(102, "&Abrir", "Abrir un archivo de texto")
        menu1.AppendSeparator()
        menu1.Append(103, "&Salir", "Cerrar el programa")
        menuBar.Append(menu1, "&Archivo")

        menu2 = Menu()
        menu2.Append(201, "Documentación")
        menu2.Append(202, "Acerca de")
        menuBar.Append(menu2, "a&Yuda")

        f.SetMenuBar(menuBar)
        idList = [101, 102, 103, 201, 202]
        for e in idList:
            f.Bind(EVT_MENU, self.accion, id=e)

        f.Show()
        return True

    def accion(self, event):
        id = event.GetId()
        print(id)
        
        switch = {
            101: self.nuevo,
            102: self.abrir,
            103: self.salir,
            201: self.nada,
            202: self.nada
        }
        switch.get(id)()

    def nuevo(self):
        print("opción nuevo")

    def abrir(self):
        contenido = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Nullam eros arcu, eleifend non ipsum et, 
        accumsan vehicula tortor. Pellentesque habitant morbi
        tristique senectus et netus et malesuada fames ac turpis.
        """
        self.tc.SetValue(contenido)

    def salir(self):
        self.f.Close()

    def nada(self):
        pass

app = MyApp()
app.MainLoop()
