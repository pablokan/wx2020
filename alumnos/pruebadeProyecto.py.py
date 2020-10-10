from sqlite3 import OperationalError,IntegrityError,connect
from wx import *
from wx.dataview import DataViewListCtrl
from wx.adv import *


##########################################
# BASE DE DATOS PARA CREAR, LEER, ACTUALIZAR Y BORRAR (CRUD) DATOS DE LAS RESERVACIONES
##########################################
class DATABASE(object):
    def __init__(self,db_name='.reservations'):
        self.conn=connect(db_name)
        self.cursor=self.conn.cursor()
        self.__create_table()
    
    def __create_table(self):
        q="""CREATE TABLE RESERVATIONS(        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name text(20),
        last_name text(20),
        telephone_number text(10),
        service text(10),  
        date text(10) UNIQUE, 
        time text(10),
        price text(4)
        )"""
        try:
            #PARA EJECUTAR LA CONSULTA (CREAR LA TABLA PARA LAS RESERVACIONES)
            self.cursor.execute(q)           
            #PARA GUARDAR LA TRANSACCION
            self.conn.commit()
        except OperationalError as e:
            pass
            
    def create(self,first_name,last_name,telephone_number,service,date,time,price): 
        q="""INSERT INTO RESERVATIONS VALUES(
        NULL,?,?,?,?,?,?,?
        )"""
        
        to_insert=( (first_name),(last_name),(telephone_number),(service), (date), (time), (price) )
        try:
            self.cursor.execute(q, to_insert ) 
            self.conn.commit()
            return True
        except OperationalError as e:
            print(e)
        except IntegrityError as e:
            return False

    def read(self,telephone_number=None,get_all=False):   
        try:
            if telephone_number is None and get_all:
                q="SELECT last_name,first_name,telephone_number,service,date,time,price FROM RESERVATIONS"
                self.cursor.execute(q)
                data=self.cursor.fetchall()
                if data == []:
                    return 
                else:
                   return data
            elif telephone_number is not None and not get_all:
                q="SELECT * FROM RESERVATIONS WHERE telephone_number = ?"
                self.cursor.execute(q,(telephone_number,))
                data=self.cursor.fetchall()
                if data == []:
                    return 
                else:
                   return data
            else:
                return 
        except OperationalError:
            return
        
    def close(self):
        self.cursor.close()
        self.conn.close()


class MyApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Turnos de Depilacion", size = (770,700))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc= DataViewListCtrl(p1)
        encabezado = [('Apellidos', 125), ('Nombres', 125),('Telefono',50) , ('Servicio', 150), ('Fecha del Turno', 100), ('Horario', 100), ('Precio', 100)]
        for enca in encabezado:
            self.dvlc.AppendTextColumn(enca[0], width=enca[1])
        
        mydb=DATABASE()
        clients_data=mydb.read(get_all=True)
        mydb.close()

        if clients_data:
            if len(clients_data) == 1:
                items=list(clients_data[0])
                print(items)
                self.dvlc.AppendItem(items)

            else:
                for client_data in clients_data:
                    items=list(client_data)
                    print(items)
                    self.dvlc.AppendItem(items)

        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Agregar Clientes")
        hor.Add(b)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(self.dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.abrirAgP)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()
        return True

    def abrirAgP(self, e):
        f2 = Frame(None, title="Agregar Clientes", size=(300, 350))
        p2 = self.p2 = Panel(f2)
        grilla = GridBagSizer(5,5)

# Apellidos - Caja de Texto
        flagsTex = TOP|ALIGN_CENTER
        flagsInp = EXPAND
        l_apellido = StaticText(p2, -1, "Apellidos")
        grilla.Add(l_apellido, pos=(0,0), flag=flagsTex, border=5)
        self.apellido_input = TextCtrl(p2, -1, "Apellidos")
        grilla.Add(self.apellido_input, pos=(0,1), span = (1, 2), flag=flagsInp)

# Nombre - Caja de Texto
        l_nombrem = StaticText(p2, -1, "Nombre")
        grilla.Add(l_nombrem, pos = (1,0), flag=flagsTex, border=5)
        self.nombre_input =TextCtrl(p2, -1, "Nombre")
        grilla.Add(self.nombre_input, pos = (1,1), span = (1, 2), flag=flagsInp)

# Numero de Telefono - Caja de Texto
        l_numero_telefono = StaticText(p2, -1, "Numero Telefono")
        grilla.Add(l_numero_telefono, pos = (2,0), flag=flagsTex, border=5)
        self.numero_telefono_input =TextCtrl(p2, -1, "Numero de telefono")
        grilla.Add(self.numero_telefono_input, pos = (2,1), span = (1, 2), flag=flagsInp)

# servicioo - Combo
        l_servicio = StaticText(p2, -1, "Servicio")
        grilla.Add(l_servicio, pos = (3,0), flag=flagsTex, border=5)
        servicioList = ["Masajes", "Depilacion", "Lprecioieza de cutis"]
        self.servicio_input = ComboBox(p2, 500, "Servicio", (0, 0), (-1, -1), servicioList, CB_DROPDOWN | TE_PROCESS_ENTER )
        self.servicio_input.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.servicio_input, pos = (3,1), span = (1, 2), flag=flagsInp)

# fecha - Caja de Texto fecha  del Turno - Abre datepicker
        l_fecha = StaticText(p2, -1, "Fecha del Turno")
        grilla.Add(l_fecha, pos = (4,0), flag=flagsTex, border=5)
        self.fecha_input = DatePickerCtrl(p2, size=(120,-1), style = DP_DROPDOWN | DP_SHOWCENTURY)
        self.fecha_input.Bind(EVT_DATE_CHANGED, self.OnDateChanged, self.fecha_input)
        grilla.Add(self.fecha_input, pos = (4,1), span = (1, 2), flag=flagsInp)

# Horario - Caja de Texto
        l_horario = StaticText(p2, -1, "Horario")
        grilla.Add(l_horario, pos = (5,0), flag=flagsTex, border=5)
        self.horarios_input = TextCtrl(p2,-1,"Horario")
        grilla.Add(self.horarios_input, pos = (5, 1), span = (1, 1),flag=flagsInp)
    

# Precio - Radio Buttons
        l_precio = StaticText(p2, -1, "Precio")
        grilla.Add(l_precio, pos = (6,0), flag=flagsTex, border=5)
        self.precio_input = TextCtrl(p2,-1,"Precio")
        grilla.Add(self.precio_input, pos = (6, 1), span = (1, 1),flag=flagsInp)

# Botón Guardar
        guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (7, 0), span=(1, 3), flag=EXPAND|ALL|ALIGN_CENTER, border=10)
        guardar.Bind(EVT_BUTTON, self.guardaPart)

# Muestra la grilla
        p2.SetSizer(grilla)
        f2.Show()

#Guarda el participante
    def guardaPart(self, evt):
        apellido = self.apellido_input.GetValue()
        nombre = self.nombre_input.GetValue()
        numero_telefono=self.numero_telefono_input.GetValue()
        fecha = str(self.fecha_input.GetValue())
        servicio = self.servicio_input.GetValue()
        horario= self.horarios_input.GetValue()
        precio = self.precio_input.GetValue()

        items=[apellido, nombre,numero_telefono,servicio, fecha, horario, precio]
        print(items)
        mydb=DATABASE()
        saved_data=mydb.create(nombre,apellido,numero_telefono,servicio, fecha, horario, precio)
        mydb.close()
        if saved_data:
            self.dvlc.AppendItem(items)
        else:
            # AQUI SE TIENE QUE IMPLMENTAR: MOSTRAR MENSAJE DE ERROR AL USUARIO
            print("La fecha ya fue reservada...!!")

# Begin Combo
    def OnKillFocus(self, evt):
        # self.pr = self.pro.GetValue()
        evt.Skip()
# End Combo

# Begin Calendario
    def OnDateChanged(self, evt):
        d = evt.GetDate()
        self.fecha = d.FormatISODate()
# End Calendario

app = MyApp()
app.MainLoop()