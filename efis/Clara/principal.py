from wx import *
from wx.dataview import * 
import sqlite3
from random import randint
from wx.lib.ogl import lines
import wx
from wx.adv import AnimationCtrl

class MyApp(App):
    def OnInit(self):
        f = Frame(None,-1,"   SORTEO",size=(400, 400))
        p = self.p = Panel(f)
        p.SetBackgroundColour((100,149,237))
        #se podria agregar en la barra del titulo del frame un menu para agregar sorteo nuevo creando una nueva base de datos 
        #preguntando la cantidad de numeros para sortear y el nombre del sorteo 
        A = Button(p, -1, "AGREGAR PARTICIPANTES", (90,50),(200,90),)
        V = Button(p, -1, "VER LISTA PARTICIPANTES", (90,150),(200,90))
        S = Button(p, -1, "SORTEAR", (90,250),(200,90))
        A.Bind(EVT_BUTTON, self.Agregar)
        V.Bind(EVT_BUTTON, self.Mostrar)
        S.Bind(EVT_BUTTON, self.Sortear)
        A.SetBackgroundColour((176,224,230))
        V.SetBackgroundColour((176,224,230))
        S.SetBackgroundColour((176,224,230))
        #con = sqlite3.connect("DatosSorteo00.db")
        #cur = con.cursor()
        #cur.execute("CREATE TABLE concursantes00 (id integer PRIMARY KEY, numero real, nombre text, apellido text, direccion text, telefono real)")
        #con.commit()


        f.Show()
        return True

    def Agregar(self, e):
        self.f2 = f2 = Frame(None, -1, "AGREGAR PARTICIPANTES")
        p2 = Panel(f2)
        grilla = GridBagSizer(3,3)
        flagsTex = TOP|ALIGN_CENTER
        flagsInp = EXPAND
        snumero = StaticText(p2, -1, "NUMERO DE SORTEO")
        grilla.Add(snumero, pos = (1,1), flag=flagsTex, border=5)
#Numero        
        a = open("lista.txt", "r")
        listaaa = a.read()
        a.close()
        nLista = listaaa.split("\n")
        self.numero = numero = ComboBox(p2, -1, "NUMERO", (2, 2), (1, 1), nLista, CB_DROPDOWN | TE_PROCESS_ENTER )
        grilla.Add(numero, pos = (1,4), span = (2, 2), flag=flagsInp) #falta que busque mientras se va escribiendo el nombre
        numero.Bind(EVT_TEXT, self.EvtText)
        numero.Bind(EVT_CHAR, self.EvtChar)
        numero.Bind(EVT_COMBOBOX, self.EvtCombobox)
        #self.ignoreEvtText = False

#Nombre
        snombre = StaticText(p2, -1, "Nombre")
        grilla.Add(snombre, pos = (3,1), flag=flagsTex, border=5)
        nombre = self.nombre =TextCtrl(p2, -1, "Nombre")
        grilla.Add(nombre, pos = (3,4), span = (2, 2), flag=flagsInp)
#Apellido
        sapellido = StaticText(p2, -1, "Apellido")
        grilla.Add(sapellido, pos=(5,1), flag=flagsTex, border=5)
        apellido = self.apellido = TextCtrl(p2, -1, "Apellido")
        grilla.Add(apellido, pos=(5,4), span = (1, 2), flag=flagsInp)
#Telefono
        stelefono = StaticText(p2, -1, "TELEFONO")
        grilla.Add(stelefono, pos = (6,1), flag=flagsTex, border=5)
        telefono =self.telefono = TextCtrl(p2, -1, "TELEFONO")
        grilla.Add(telefono, pos = (6,4), span = (2, 2), flag=flagsInp, border=10)
#Direccion
        l_adi = StaticText(p2, -1, "DIRECCION")
        grilla.Add(l_adi, pos = (8,1), flag=flagsTex, border=5)
        direccion = self.direccion =TextCtrl(p2, -1, "DIRECCION")
        grilla.Add(direccion, pos = (8,4), span = (2, 2), flag=flagsInp)

#Guardar
        guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (10, 4), span=(2, 3), flag=EXPAND|ALL|ALIGN_CENTER, border=10)
        guardar.Bind(EVT_BUTTON, self.guardar)
        
        
        p2.SetSizer(grilla)
        f2.Show()

        
    def EvtCombobox(self, event):
        self.ignoreEvtText = True
        event.Skip()
    
    def EvtChar(self, event):
        if event.GetKeyCode() == 8:
            self.ignoreEvtText = True
            event.Skip()
    
    def EvtText(self, event):
        if self.ignoreEvtText:
            self.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.numero :
            if choice.startswith(currentText):
                self.ignoreEvtText = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetMark(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()

    def guardar(self, evt):
        self.ap = apellido= self.apellido.GetValue()
        self.no = nombre= self.nombre.GetValue()
        self.tl = telefono= self.telefono.GetValue()
        self.di = direccion= self.direccion.GetValue()
        self.nu = numero= self.numero.GetValue()
        con = sqlite3.connect("DatosSorteo00.db")
        cur = con.cursor()
        datos = f"INSERT INTO concursantes00 (numero, nombre, apellido, direccion, telefono) VALUES ('{numero}', '{nombre}', '{apellido}', '{direccion}', '{telefono}')"
        cur.execute(datos)
        con.commit()
        con.close()
        print("si")
        f = open("lista.txt","r")
        lines = f.readlines()
        f.close()
        f = open("lista.txt","w")
        for line in lines:
            if line != str(numero)+"\n":
                lines = f.write(line)
        f.close()
        self.f2.Close(True)

    def Mostrar(self, e):
        f1 = Frame(None, -1, "Listado de participantes", size =(510, 500))
        p1 = self.p1 = Panel(f1,)

        self.dvlc = dvlc = DataViewListCtrl(p1)
        dvlc.Bind(EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.modif)
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn("Numero", width=60) #no se ven los numeros del comboBox
        dvlc.AppendTextColumn('Nombre', width=100)
        dvlc.AppendTextColumn('Apellido', width=100, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Domicilio', width=100)
        dvlc.AppendTextColumn('Telefono', width=100)
        
        def recupBD(): 
            con = sqlite3.connect("DatosSorteo00.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM concursantes00 ORDER BY Nombre")
            tuplas = cur.fetchall()
            #print(tuplas)
            listaA = [list(e) for e in tuplas] 
            for e in listaA:
                e[0] = str(e[0])
            con.close()
            return listaA
        lista = recupBD()
        #print(lista)

        for e in lista:
            self.dvlc.AppendItem(e)
        self.busqueda = lista

        for c in self.dvlc.Columns:
            c.Sortable = True
            c.Reorderable = True
       

        self.search = search = SearchCtrl(p1, size=(150, 33))
        search.Hide()
        search.ShowCancelButton(True)
       
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        sizer.Add(search, 0, EXPAND)
        p1.SetSizer(sizer)

        f1.Show()
        return True
    

    def modif(self, evt):  #revisar 
        def grabaBD(id, numero, nombre, apellido, domicilio, telefono):
            con = sqlite3.connect("DatosSorteo00.db")
            cur = con.cursor()
            actu = f"UPDATE concursantes00 SET numero='{numero}', nombre='{nombre}', apellido='{apellido}', domicilio='{domicilio}', telefono'{telefono}' WHERE id={id}"
            cur.execute(actu)
            con.commit()
            con.close()

        row = self.dvlc.GetSelectedRow()
        id = self.dvlc.GetTextValue(row, 0)
        self.numerosusados = numero = self.dvlc.GetTextValue(row,1)
        nombre = self.dvlc.GetTextValue(row, 2)
        apellido = self.dvlc.GetTextValue(row, 3)
        domicilio = self.dvlc.GetTextValue(row, 4)
        telefono= self.dvlc.GetTextValue(row, 5)
        grabaBD(id, numero, nombre, apellido, domicilio, telefono)

    
    def Sortear(self, e): #se podria agregar la cantidad de ganadores
        
        con = sqlite3.connect("DatosSorteo00.db")
        cur = con.cursor()
        listanumerosusados = []
        for row in cur.execute('SELECT * FROM concursantes00;'):
            print(row)
            listanumerosusados.append(row)

        con.close()


        b = randint(0, len(listanumerosusados)-1)
        G = ("Ganador/a: \n"+str(listanumerosusados[b]))
        styles = DEFAULT_FRAME_STYLE & ~ (CAPTION)
        f4 = Frame(None,-1,"       GANADOR/A     ",size=(500, 510))
        p4 = self.p4 = Panel(f4)
        p4.SetBackgroundColour((100,149,237))
        imagen = AnimationCtrl(p4)
        imagen.LoadFile('tenor.gif')
        imagen.Play()
        ganadora = StaticText(p4, -1, G, size= (60,20),pos=(5,400))
        font = wx.Font(10, MODERN, SLANT, BOLD)
        ganadora.SetFont(font)

        f4.Show()
        return True


    


app = MyApp()
app.MainLoop()
