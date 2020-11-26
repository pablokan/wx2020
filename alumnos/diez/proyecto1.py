import sqlite3
from wx import *
from wx.dataview import DataViewListCtrl
from wx.adv import *

class MyApp(App):
    def OnInit(self):#Metodo constructor de la clase app
        try:
            cmd="""CREATE TABLE datos ( 
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                apellido TEXT(50), 
                nombre TEXT(50), 
                numero TEXT(8), 
                fecha DATETIME, 
                servicio TEXT(7),
                horario DATETIME,
                precio FLOAT
            )"""
            conn=sqlite3.connect("clientes1.db")#Cree una tabla para poder guardar los datos con la base de datos 
            cursor= conn.cursor()
            cursor.execute(cmd)
            cursor.close()
            conn.close() 
        except sqlite3.OperationalError:
            pass

        frame1 = Frame(None, -1, "Turnos de Depilacion", size = (770,700)) #Creo que cuadro del interfaz 
        panel1 = self.panel1 = Panel(frame1, -1 )
        frame1.SetBackgroundColour("#dda0dd")
        self.dvlc = dvlc = DataViewListCtrl(panel1)
        encabezado = [('Apellidos', 150), ('Nombres', 150),('Numero de telefono',100), ('Fecha del Turno', 100), ('Servicio', 150), ('Horario', 100), ('Precio', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])

        hor=BoxSizer(HORIZONTAL)
        botoncarga = Button(panel1, -1, "&Cargar clientes")
        botonagregarclientes = Button(panel1, -1, "&Agregar clientes")
        botonborrarclientes = Button(panel1, -1, "&Borrar clientes")
        botonverclientesHoy = Button(panel1, -1, "&Clientes de Hoy")
        hor.Add(botoncarga)
        hor.Add(botonagregarclientes)
        hor.Add(botonborrarclientes)
        hor.Add(botonverclientesHoy)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        botonagregarclientes.Bind(EVT_BUTTON, self.agregarClientes)
        botoncarga.Bind(EVT_BUTTON, self.cargarClientes)
        botonborrarclientes.Bind(EVT_BUTTON, self.borrarClientes)
       # botonverclientesHoy.Bind(EVT_BUTTON, self.botonverclientesHoy)
        sizer.Add(hor)
        panel1.SetSizer(sizer)
        frame1.Show()
        return True


#Cargar clientes
    
    def cargarClientes(self,event):
        def recupBD():
            con = sqlite3.connect("clientes1.db")
            cur = con.cursor()
            cur.execute("SELECT apellido, nombre, numero, fecha, servicio, horario, precio FROM datos ORDER BY fecha")
            tuplas = cur.fetchall()
            # print(tuplas)
            # listaA = [list(e) for e in tuplas]
            # for e in listaA:
            #     e[0] = str(e[0])
            # con.close()
            return tuplas

        tuplas = recupBD()
        for e in range(0,tuplas.__len__()):
            element=list(tuplas[e])
            print(element)
            self.dvlc.AppendItem(element)


#Agregar clientes

    def agregarClientes(self,e):
        frame1 = Frame(None, title="Agregar Clientes", size=(300, 350))
        panel2 = self.panel2 = Panel(frame1)
        rojo=wx.Colour(255,5,0)
        panel2.SetBackgroundColour(rojo)
        grilla = GridBagSizer(5,5)

# Apellidos
        flagsTex = TOP|ALIGN_CENTER
        flagsInp = EXPAND
        l_apellido = StaticText(panel2, -1, "Apellidos")
        grilla.Add(l_apellido, pos=(0,0), flag=flagsTex, border=5)
        self.apellido_input = TextCtrl(panel2, -1, "Apellidos")
        grilla.Add(self.apellido_input, pos=(0,1), span = (1, 2), flag=flagsInp)

# Nombre
        l_num_telefono = StaticText(panel2, -1, "Nombre")
        grilla.Add(l_num_telefono, pos = (1,0), flag=flagsTex, border=5)
        self.nombre_input =TextCtrl(panel2, -1, "Nombre")
        grilla.Add(self.nombre_input, pos = (1,1), span = (1, 2), flag=flagsInp)



#Numero de telefono
        l_num_telefono = StaticText(panel2, -1, "Numero de telefono")
        grilla.Add(l_num_telefono, pos = (2,0), flag=flagsTex, border=5)
        self.numero_input =TextCtrl(panel2, -1, "Numero de telefono")
        grilla.Add(self.numero_input, pos = (2,1), span = (1, 2), flag=flagsInp)


# fecha
        l_fecha = StaticText(panel2, -1, "Fecha del Turno")
        grilla.Add(l_fecha, pos = (4,0), flag=flagsTex, border=5)
        self.fecha_input = DatePickerCtrl(panel2, size=(120,-1), style = DP_DROPDOWN | DP_SHOWCENTURY)
        self.fecha_input.Bind(EVT_DATE_CHANGED, self.OnDateChanged, self.fecha_input)
        grilla.Add(self.fecha_input, pos = (4,1), span = (1, 2), flag=flagsInp)
# servicios
        l_servicio = StaticText(panel2, -1, "Servicio")
        grilla.Add(l_servicio, pos = (3,0), flag=flagsTex, border=5)
        servicioList = ["Masajes", "Depilacion", "Limpieza de cutis"]
        self.servicio_input = ComboBox(panel2, 500, "Servicio", (0, 0), (-1, -1), servicioList, CB_DROPDOWN | TE_PROCESS_ENTER )
        self.servicio_input.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.servicio_input, pos = (3,1), span = (1, 2), flag=flagsInp)

# Horario
        l_horario = StaticText(panel2, -1, "Horario")
        grilla.Add(l_horario, pos = (5,0), flag=flagsTex, border=5)
        self.horarios_input = TextCtrl(panel2,-1,"Horario")
        grilla.Add(self.horarios_input, pos = (5, 1), span = (1, 1),flag=flagsInp)


# Precio
        l_precio = StaticText(panel2, -1, "Precio")
        grilla.Add(l_precio, pos = (6,0), flag=flagsTex, border=5)
        self.precio_input = TextCtrl(panel2,-1,"Precio")
        grilla.Add(self.precio_input, pos = (6, 1), span = (1, 1),flag=flagsInp)

# Para Guardar
        guardar = Button(panel2, -1, "Guardar")
        grilla.Add(guardar, pos = (7, 0), span=(1, 3), flag=EXPAND|ALL|ALIGN_CENTER, border=10)
        guardar.Bind(EVT_BUTTON, self.guardaPart)


        panel2.SetSizer(grilla)
        frame1.Show()

        #Guarda los clientes
    def guardaPart(self, evt):
        apellido = self.apellido_input.GetValue()
        nombre = self.nombre_input.GetValue()
        fecha = str(self.fecha_input.GetValue())
        servicio = self.servicio_input.GetValue()
        horario= self.horarios_input.GetValue()
        precio = self.precio_input.GetValue()
        numero = self.numero_input.GetValue()

        self.dvlc.AppendItem([apellido, nombre, numero, fecha, servicio, horario , precio])
        con = sqlite3.connect("clientes1.db")
        cur = con.cursor()
        alta = f"INSERT INTO datos VALUES (NULL, '{apellido}', '{nombre}', '{numero}', '{fecha}', '{servicio}','{horario}','{precio}')"
        print(alta)
        cur.execute(alta)
        con.commit()
        con.close()
       

    def OnKillFocus(self, evt):
        self.servicio.GetValue()
        evt.Skip()


# Calendario
    def OnDateChanged(self, evt):
        print(evt.GetDate())
        d = evt.GetDate()
        print(d.FormatISODate())
        self.fecha = d.FormatISODate()
    
#Borrar cliente
    def borrarClientes(self, event):
            def borraBD(nombre):
                con = sqlite3.connect("clientes1.db")
                cur = con.cursor()
                dele = f"DELETE from datos WHERE nombre={nombre}"
                cur.execute(dele)
                con.commit()
                con.close()
            row = self.dvlc.GetSelectedRow()
            nombre = self.dvlc.GetTextValue(row, 0)
            self.dvlc.DeleteItem(row)
            borraBD(nombre)











































app = MyApp()
app.MainLoop()























app = MyApp()
app.MainLoop()