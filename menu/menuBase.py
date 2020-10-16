from wx import *

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, -1, 'Menú de Opciones')
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.st = st = StaticText(p, label="static text")
        self.tc = tc = TextCtrl(p, value="valor por defecto", style=TE_READONLY)
        s.Add(st, 0, ALL|ALIGN_CENTER, 20)
        s.Add(tc, 0, ALL|EXPAND, 20)
        p.SetSizer(s)

        # menu 
        f.CreateStatusBar()
        f.SetStatusText("Esto va en la barra de estado")

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
        if id == 101:
            print("opción 'Nuevo'")
            self.st.SetLabel("hiciste click en 'Nuevo'")
        if id == 102:
            self.tc.SetValue("metiste la opción Archivo --> Abrir")
        if id == 201:
            f2 = Frame(None, size=(600, 100))
            f2.Show()

        if id == 202:
            print("opción 'Acerca de'")
        if id == 103:
            self.f.Close()


app = MyApp()
app.MainLoop()
