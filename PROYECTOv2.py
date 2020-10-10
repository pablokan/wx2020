from wx import *
from wx.dataview import *
from wx.adv import *
import sqlite3
from sqlalchemy import *
from validador import *

class MyApp(App):

    def OnInit (self):
        self.f = Frame (None, title = "Vapor Expreso", size = (600, 500))
        cuaderno = Notebook(self.f)
        panel1 = self.panel1 = Panel(cuaderno)
        panel2 = self.panel2 = Panel(cuaderno)
        panel3 = self.panel3 = Panel(cuaderno)
        cuaderno.AddPage(self.panel1, "e-Liquid")
        cuaderno.AddPage(self.panel2, "Equipos y repuestos")
        cuaderno.AddPage(self.panel3, "Ventas")

        self.liquidos()
        self.Equipos()
        self.ventas()
        self.f.Show()
        return True

    def liquidos (self):
        self.comparadorL = comparadorL = 0
        self.grilla = grilla = DataViewListCtrl(self.panel1)
        self.grilla.AppendTextColumn ("#", width = 20)
        self.encabezado = ["Nombre", "Tipo", "Nacionalidad", "Cantidad", "Nicotina", "SubTipo"]
        j = 0
        for i in self.encabezado :
            if j == 0 or j == 2:
                self.grilla.AppendTextColumn (i, width = 130)
            else:
                self.grilla.AppendTextColumn (i, width = 75)
            j += 1
        boton = Button (self.panel1, -1 , label = "&Agregar producto")
        self.caja = caja = BoxSizer(HORIZONTAL)
        caja.Add(boton, 1)
        self.search = search = SearchCtrl(self.panel1, value="Buscar") #Boton buscar
        search.ShowCancelButton(True)
        boton.Bind(EVT_BUTTON, self.agregarLiquidos)
        caja.Add(search, 1, flag=EXPAND)
        caja2 = BoxSizer(VERTICAL) #Hace falta para que se ponga en HORIZONTAL el botón
        caja2.Add(self.grilla, -1, EXPAND)
        caja2.Add(caja, flag=EXPAND)
        self.panel1.SetSizer(caja2)
        con = sqlite3.connect("VaperOfice.db")
        cur = con.cursor()
        try:
            cur .execute("CREATE TABLE Liquidos (Id INTEGER PRIMARY kEY, Nombre NVARCHAR, Tipo NVARCHAR, Nacionalidad NVARCHAR, Cantidad NVARCHAR, Nicotina NVARCHAR, Subtipo NVARCHAR)")
        except:
            self.cargaDatosLiquidos()
            print(str(self.comparadorL) + " comparador en programa")

        
        self.search.Bind(EVT_TEXT, self.buscar)
        self.grilla.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.editar)
        return True

    def Equipos (self):
        self.comparadorE = comparadorE = 0
        self.grillaE = grillaE = DataViewListCtrl(self.panel2)
        self.encabezado2 = ["Nombre", "Tipo", "Bateria", "Capacidad", "Cantidad"]
        self.grillaE.AppendTextColumn ("#", width = 20)
        for i in self.encabezado2 :
            self.grillaE.AppendTextColumn (i, width = 130)
        boton = Button (self.panel2, -1 , label = "Agregar producto")
        self.caja2 = caja = BoxSizer(HORIZONTAL)
        caja.Add(boton)
        boton.Bind(EVT_BUTTON, self.agregarEquipos)
        relleno = StaticText(self.panel2) #El relleno espara qe el botòn Buscar se ubique en el lado opuesto del botòn Agregar
        self.searchE = search = SearchCtrl(self.panel2) #Boton buscar
        search.ShowCancelButton(True)
        caja.Add(relleno, 4, flag = EXPAND)
        caja.Add(self.searchE, flag = EXPAND)
        caja2 = BoxSizer(VERTICAL) #Hace falta para que se ponga en HORIZONTAL el botón
        caja2.Add(self.grillaE, -1, EXPAND)
        caja2.Add(caja, flag=EXPAND)
        self.panel2.SetSizer(caja2)
        con = sqlite3.connect("VaperOfice.db")
        cur = con.cursor()
        try:
            cur .execute("CREATE TABLE Equipos (Id INTEGER PRIMARY kEY, Nombre NVARCHAR, Tipo NVARCHAR, Bateria NVARCHAR, Capacidad NVARCHAR, Cantidad NVARCHAR)")
        except:
            self.comparadorE+=1
            self.cargaDatosEquipos()

        self.searchE.Bind(EVT_TEXT, self.buscarE)
        self.grillaE.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.editarE)
        return True

    def ventas(self):
        self.comparadoridV = comparadoridV = 0
        self.grillaV = grillaV = DataViewListCtrl(self.panel3)
        self.grillaV.AppendTextColumn ("#", width = 20)
        encabezado = ["Nombre", "Dni", "Telefono", "Monto"]
        for i in encabezado :
            self.grillaV.AppendTextColumn (i, width = 130)
        boton = Button(self.panel3, label="Vender")
        boton.Bind(EVT_BUTTON, self.vender)
        cajaV = BoxSizer(VERTICAL)
        cajaV.Add(self.grillaV, 1, EXPAND)
        cajaV.Add(boton)
        self.panel3.SetSizer(cajaV)


        con = sqlite3.connect("VaperOfice.db")
        cur = con.cursor()
        try:
            cur .execute("CREATE TABLE Ventas (Id INTEGER PRIMARY kEY, Nombre NVARCHAR, Dni NVARCHAR, Telefono NVARCHAR, Monto NVARCHAR)")
        except:
            self.comparadoridV+=1
            self.cargaDatosVentas()
        self.grillaV.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.cliente)
        
    def vender(self, event):
        self.sumaTotal= sumaTotal = 0
        self.listaAux = listaAux = []
        listaLiquidos = self.recupBDLiquidos()
        for l in listaLiquidos:
            listaAux.append(l[1])
        self.fVenta = fVenta = Frame (None, title = "Vender", size = (550, 800))
        self.griPrincipal = griPrincipal = BoxSizer (VERTICAL)
        self. grillaVe = grillaVe = BoxSizer(HORIZONTAL)
        columStatick = BoxSizer (VERTICAL)
        self.columOpcionesVentas = columOpcionesVentas = BoxSizer (VERTICAL)
        self.listaVentas = listaVentas = ["Nombre y Apellido","DNI", "Producto", ["Liquidos", "Equipos"], "Cantidad", "Precio", "Telefono"]
        j = 1
        for i in listaVentas :
            if j == 4 :
                aux = StaticText(self.fVenta, label = "")
                columStatick.Add(aux, 1, ALL, 22)
            else:
                aux = StaticText(self.fVenta, label = i)
                columStatick.Add(aux, 1, ALL, 22)
            j += 1
        self.nombreC = nombreC = TextCtrl(self.fVenta, size = (150, 30))
        columOpcionesVentas.Add(nombreC, 1, ALL, 10)
        self.dniC = dniC = TextCtrl(self.fVenta, size = (100, 30), validator = MyValidator())
        columOpcionesVentas.Add(dniC, 1, ALL, 10)
        self.aux3 = aux3 = RadioBox (self.fVenta, -1 , choices = listaVentas[3], style = NO_BORDER | RA_SPECIFY_COLS)
        columOpcionesVentas.Add(aux3, 1, LEFT, 10)
        aux3.Bind(EVT_RADIOBOX, self.productos)
        self.eleccionP = eleccionP = ComboBox (self.fVenta, -1 , choices = listaAux , size = (150,40))
        columOpcionesVentas.Add(eleccionP, 1 , ALL, 10)
        self.cantP = cantP = TextCtrl (self.fVenta, validator = MyValidator())
        columOpcionesVentas.Add(cantP, 1, ALL, 10)
        self.precioP = precioP = TextCtrl(self.fVenta, validator = MyValidator())
        columOpcionesVentas.Add(precioP, 1, ALL, 10)
        self.tel = tel = TextCtrl(self.fVenta, validator = MyValidator())
        columOpcionesVentas.Add(tel, 1, ALL, 20)
        #agregarAlCarro =  Button (self.fVenta, label = "Agregar al carro")
        #columStatick.Add(agregarAlCarro)
        
        grillaVe.Add(columStatick)
        grillaVe.Add(columOpcionesVentas)
        griPrincipal.Add(grillaVe)
        self.panelVentas = panelVentas = DataViewListCtrl(self.fVenta)
        encaVenta = ["Nombre", "Cantidad", "Monto $"]
        for e in encaVenta :
            panelVentas.AppendTextColumn(e, width = (130))
        griPrincipal.Add(panelVentas, 1, EXPAND)

        self.botonFinVenta = botonFinVenta = Button(self.fVenta, label="Finalizar venta")
        textTotal = StaticText(self.fVenta, label =  "                                   Total: ", size = (400, 25))
        self.precioFinal = precioFinal = TextCtrl(self.fVenta, size = (100,30), value="0")
        agregarAlCarro =  Button (self.fVenta, label = "Agregar al carro")
        griFinal = BoxSizer (HORIZONTAL) 
        griFinal.Add(botonFinVenta)
        griFinal.Add(agregarAlCarro)
        botonFinVenta.Bind(EVT_BUTTON, self.finalizarLaCompra)
        agregarAlCarro.Bind(EVT_BUTTON, self.agregarACarro)
        griFinal.Add(textTotal, 1, ALL, 7)
        griFinal.Add(precioFinal)
        griPrincipal.Add(griFinal)
        self.fVenta.SetSizer(griPrincipal)
        self.fVenta.Show()
    

    def agregarACarro(self, event):
        listaCarro = []
        tipo = self.aux3.GetStringSelection()
        tipo = tipo.lower()
        print("este es el tipo: "+tipo)
        nombreProducto = self.eleccionP.GetStringSelection()
        idp = self.obtenerID(tipo, nombreProducto)
        listaCarro.append(str(nombreProducto))
        cantidad = int(self.cantP.GetValue())
        listaCarro.append(str(cantidad))
        precio = float(self.precioP.GetValue())
        totalProducto = cantidad * precio
        self.sumaTotal += totalProducto
        listaCarro.append("$"+str(totalProducto))
        self.panelVentas.AppendItem(listaCarro)
        self.precioFinal.SetValue(str(self.sumaTotal))
        self.restaStokL(tipo, idp, cantidad)
        print(listaCarro)


    def finalizarLaCompra(self, event):
        nombreCliente = str(self.nombreC.GetValue())
        dni = str(self.dniC.GetValue())
        telefono = str(self.tel.GetValue())
        total = str(self.sumaTotal)
        self.comparadoridV += 1
        self.grillaV.AppendItem([str(self.comparadoridV),nombreCliente, dni, telefono, total])
        self.grabaBDVentas(nombreCliente, dni, telefono, total)
        self.fVenta.Close()

    def cliente (self, e):
        v = Frame(None, title = "Información del cliente")
        dvlc = DataViewListCtrl(v)
        lista = self.recupBDVentas()
        row = self.grillaV.GetSelectedRow()
        nombre = self.grillaV.GetTextValue(row, 0)
        monto = self.grillaV.GetTextValue(row, 1)
        encabezado = ["Nombre", "Compras", "Fecha de compra"]
        for i in encabezado :
            dvlc.AppendTextColumn (i, width = 130)

        v.Show()
    



    def productos (self, event):
        listaLiquidos = self.recupBDLiquidos()
        listaEquipos = self.recupBDEquipos()
        self.listaAux = []
        if self.aux3.GetSelection() == 0 :
            for k in listaLiquidos:
                self.listaAux.append(k[1])
            self.eleccionP.SetItems(self.listaAux)
        if self.aux3.GetSelection() == 1 :
            for l in listaEquipos:
                self.listaAux.append(l[1])
            self.eleccionP.SetItems(self.listaAux)
    
    def cargaDatosEquipos(self):
        lista = self.recupBDEquipos()
        #print(lista)
        for e in lista:
            self.grillaE.AppendItem(e)
    
    def cargaDatosLiquidos(self):
        lista = self.recupBDLiquidos()
        for e in lista:
            self.grilla.AppendItem(e)
            
    def cargaDatosVentas(self):
        lista = self.recupBDVentas()
        for e in lista:
            self.grillaV.AppendItem(e)

    def recupBDLiquidos(self):
        con = sqlite3.connect("VaperOfice.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Liquidos ORDER BY id")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        
        for e in listaA:
            e[0] = str(e[0])
            if int(e[0]) > self.comparadorL:
                self.comparadorL = int(e[0]) + 1
        con.close()
        return listaA


    def recupBDEquipos(self):
        con = sqlite3.connect("VaperOfice.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Equipos ORDER BY id")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            e[0] = str(e[0])
            if int(e[0]) > self.comparadorE:
                self.comparadorE = int(e[0]) + 1
        con.close()
        return listaA
    
    def recupBDVentas(self):
        con = sqlite3.connect("VaperOfice.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Ventas ORDER BY id")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            e[0] = str(e[0])
            if int(e[0]) > self.comparadoridV:
                self.comparadoridV = int(e[0]) + 1
                print(str(self.comparadoridV)+ "este es el comparador de id ventas")
        con.close()
        return listaA

    def GetValueByRow(self, row, col):
        return self.data[row][col]

    def agregarEquipos (self, event):
        self.fEquipos = Frame (None, title = "Agregar producto", size = (300,410))
        grillaE2 = BoxSizer(HORIZONTAL)
        columStatick = columStatick = BoxSizer (VERTICAL)
        columOpciones = columOpciones = BoxSizer (VERTICAL)
        self.List = List = [["RDA", "RTA"], ["1","2"], ["0 ml", "5 ml", "10 ml"]]
        self.listaE = []
        j = 1
        k = 0
        for i in self.encabezado2 :
            aux = StaticText(self.fEquipos, label = i)
            columStatick.Add(aux, 1, ALL, 22)
            if j == 1:
                aux2 = TextCtrl(self.fEquipos, size = (100,5))
                self.listaE.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 9)
            elif j == 5:
                aux2 = TextCtrl(self.fEquipos, size = (100,5),validator = MyValidator())
                self.listaE.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 9)
            else:
                aux3 = RadioBox(self.fEquipos, -1,"",  DefaultPosition, DefaultSize, List[k], 1, NO_BORDER)
                self.listaE.append(aux3)
                columOpciones.Add(aux3, 1, ALL, 9)
                k += 1
            j += 1
        botonAgregar = Button (self.fEquipos, -1, label = "Agregar", size = DefaultSize)
        botonCerrar = Button (self.fEquipos, -1 ,label = "Cerrar", size = DefaultSize)
        botonAgregar.Bind(EVT_BUTTON, self.AgregarE)
        botonCerrar.Bind(EVT_BUTTON, self.CerrarE)
        columOpciones.Add(botonCerrar, 1, RIGHT|LEFT|BOTTOM, 10)
        columStatick.Add(botonAgregar, 1, ALL, 10)
        grillaE2.Add(columStatick)
        grillaE2.Add(columOpciones)
        self.fEquipos.SetSizer(grillaE2)
        self.fEquipos.Show()

    def agregarLiquidos (self, event):
        self.ff = Frame (None, title = "Agregar producto", size = (300,550))
        self.grilla2 = grilla2 = BoxSizer(HORIZONTAL)
        columStatick = BoxSizer (VERTICAL)
        columOpciones = BoxSizer (VERTICAL)
        self.proList = proList = [["Tabaquil", "Frutal"],["Nacional", "Importado"], ["0", "3", "6"], ["Rubio", "Negro"]]
        self.lista = []
        j = 1
        k = 0
        for i in self.encabezado :
            aux = StaticText(self.ff, label = i)
            columStatick.Add(aux, 1, ALL, 22)
            if j == 1:
                aux2 = TextCtrl(self.ff, size = (100,5))
                self.lista.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 9)
            elif j == 4:
                aux2 = TextCtrl(self.ff, size = (100,5) ,validator = MyValidator() )
                self.lista.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 9)
            else:
                aux3 = RadioBox(self.ff, -1,"",  DefaultPosition, DefaultSize, proList[k], 1, NO_BORDER)
                self.lista.append(aux3)
                columOpciones.Add(aux3, 1, ALL, 9)
                k += 1
            j += 1
        botonAgregar = Button (self.ff, -1, label = "Agregar", size = DefaultSize)
        botonCerrar = Button (self.ff, -1 ,label = "Cerrar", size = DefaultSize)
        botonAgregar.Bind(EVT_BUTTON, self.Agregar)
        botonCerrar.Bind(EVT_BUTTON, self.Cerrar)
        columOpciones.Add(botonCerrar, 1, RIGHT|LEFT|BOTTOM, 10)
        columStatick.Add(botonAgregar, 1, ALL, 10)
        self.grilla2.Add(columStatick)
        self.grilla2.Add(columOpciones)
        self.ff.SetSizer(self.grilla2)
        self.ff.Show()
        

    def AgregarE (self, event):
        condi = True
        i = 0
        while condi and i <= len(self.listaE) - 1 :
            if i == 0 and str(self.listaE[i].GetValue()) == "" or i == 4 and str(self.listaE[i].GetValue()) == "" :
                condi = False
            i += 1
        if condi:
            nom = self.listaE[0].GetValue()
            tipo = self.List[0][self.listaE[1].GetSelection()]
            bat = self.List[1][self.listaE[2].GetSelection()]
            capa = self.List[2][self.listaE[3].GetSelection()]
            cant = self.listaE[4].GetValue()
            self.grabarBDEquipos(nom,tipo,bat,capa,cant)
            self.grillaE.AppendItem([str(self.comparadorE),nom,tipo,bat,capa,cant])
            self.comparadorE += 1
            print("aca de nuevo pase")
        else:
            self.cartelError("Falta completar")

    def Agregar (self, event):
        condi = True
        i = 0
        while condi and i <= len(self.lista) - 1 :
            if i == 0 and str(self.lista[i].GetValue()) == "" or i == 3 and str(self.lista[i].GetValue()) == "":
                condi = False
            i += 1
        if condi:
            nom = self.lista[0].GetValue()
            tipo = self.proList[0][self.lista[1].GetSelection()]
            nac = self.proList[1][self.lista[2].GetSelection()]
            cant = self.lista[3].GetValue()
            nicotina = self.proList[2][self.lista[4].GetSelection()]
            subT = self.proList[3][self.lista[5].GetSelection()]
            self.grilla.AppendItem([str(self.comparadorL),nom,tipo,nac,cant,nicotina,subT ])
            self.comparadorL += 1
            self.grabaBDLiquidos(nom, tipo, nac, cant, nicotina, subT)
        else:
            self.cartelError()

    def grabaBDLiquidos(self, pnom, ptipo, pnac, pcant, pnicotina, psubt):
        engine = create_engine('sqlite:///VaperOfice.db')
        conn = engine.connect()
        metadata = MetaData()

        eLiquidos = Table('Liquidos', metadata, 
            Column('id', Integer(), primary_key=True),
            Column('Nombre', String(200)),
            Column('Tipo', String(200)),
            Column('Nacionalidad', String(200)),
            Column('Cantidad', String(200)),
            Column('Nicotina', String(200)),
            Column('Subtipo', String(200)),
            )

        t = conn.begin()
        ins = eLiquidos.insert().values(Nombre = pnom, Tipo = ptipo, Nacionalidad = pnac, Cantidad = pcant, Nicotina = pnicotina, Subtipo = psubt)    
        
        conn.execute(ins)
        #insert_eLiquido = eLiquidos.insert()  
        t.commit()

    
    
    def grabarBDEquipos(self, enom, etipo, ebat, ecapa, ecant ):
        engine = create_engine('sqlite:///VaperOfice.db')
        conn = engine.connect()
        metadata = MetaData()

        eEquipos = Table('Equipos', metadata, 
            Column('id', Integer(), primary_key=True),
            Column('Nombre', String(200)),
            Column('Tipo', String(200)),
            Column('Bateria', String(200)),
            Column('Capacidad', String(200)),
            Column('Cantidad', String(200)),
            )
        
        
        t = conn.begin()
        ins = eEquipos.insert().values(Nombre = enom, Tipo = etipo, Bateria = ebat, Capacidad = ecapa, Cantidad = ecant)    
        
        conn.execute(ins)
        #insert_eLiquido = eLiquidos.insert()  
        t.commit()


    def grabaBDVentas(self, vnom, vdni, vtelefono, vmonto):
        engine = create_engine('sqlite:///VaperOfice.db')
        conn = engine.connect()
        metadata = MetaData()

        lVentas = Table('Ventas', metadata, 
            Column('Id', Integer(), primary_key=True),
            Column('Nombre', String(200)),
            Column('Dni', String(200)),
            Column('Telefono', String(200)),
            Column('Monto', String(200)),
            )

        t = conn.begin()
        ins = lVentas.insert().values(Nombre = vnom, Dni = vdni, Telefono = vtelefono, Monto = vmonto)    
        
        conn.execute(ins)
        #insert_eLiquido = eLiquidos.insert()  
        t.commit()

    
    def cartelError (self, mensaje):
        self.error = Frame (None, title = "ATENCION!", size = (300,150))
        cajaError = BoxSizer(VERTICAL)
        botonCerrar = Button (self.error, -1 ,label = "Cerrar", size = DefaultSize)
        botonCerrar.Bind (EVT_BUTTON, self.CerrarError)
        tituloError = StaticText(self.error, -1 ,label =mensaje, style = ALIGN_CENTER)
        cajaError.Add(tituloError, 1, ALL, 20)
        cajaError.Add(botonCerrar, 1, ALL, 20)
        self.error.SetSizer(cajaError)
        self.error.Show()

    def cartelStock (self, mensaje):
        self.errorStock= Frame (None, title = "ATENCION, CONTROLE SU STOCK!", size = (600,150))
        cajaError = BoxSizer(VERTICAL)
        botonCerrar = Button (self.errorStock, -1 ,label = "Cerrar", size = DefaultSize)
        botonCerrar.Bind (EVT_BUTTON, self.CerrarErrorStock)
        tituloError = StaticText(self.errorStock, -1 ,label =mensaje, style = ALIGN_CENTER)
        cajaError.Add(tituloError, 1, ALL, 20)
        cajaError.Add(botonCerrar, 1, ALL, 20)
        self.errorStock.SetSizer(cajaError)
        self.errorStock.Show()

    def updateBDEquipos(self, id, unombre,utipo,ubateria,ucapa,ucant):
        engine = create_engine('sqlite:///VaperOfice.db')
        conn = engine.connect()
        metadata = MetaData()

        eEquipos = Table('Equipos', metadata, 
            Column('id', Integer(), primary_key=True),
            Column('Nombre', String(200)),
            Column('Tipo', String(200)),
            Column('Bateria', String(200)),
            Column('Capacidad', String(200)),
            Column('Cantidad', String(200)),
            )

        t = conn.begin()

        s = update(eEquipos).where(
            eEquipos.c.id == id
        ).values(
        Nombre = unombre,
        Tipo = utipo,
        Bateria = ubateria,
        Capacidad = ucapa,
        Cantidad = ucant
        )

        conn.execute(s)
        t.commit()

    def updateBDLiquidos(self, id, lnombre, ltipo, lnacio, lcant, lnico, lsubtipo ):
        engine = create_engine('sqlite:///VaperOfice.db')
        conn = engine.connect()
        metadata = MetaData()

        eLiquidos = Table('Liquidos', metadata, 
            Column('id', Integer(), primary_key=True),
            Column('Nombre', String(200)),
            Column('Tipo', String(200)),
            Column('Nacionalidad', String(200)),
            Column('Cantidad', String(200)),
            Column('Nicotina', String(200)),
            Column('Subtipo', String(200)),
            )

        t = conn.begin()

        s = update(eLiquidos).where(
            eLiquidos.c.id == id
        ).values(
        Nombre = lnombre,
        Tipo = ltipo,
        Nacionalidad = lnacio,
        Cantidad = lcant,
        Nicotina = lnico,
        Subtipo = lsubtipo
        )

        conn.execute(s)
        t.commit()



    def editar (self, event):
        lista1 = []
        self.row = row = self.grilla.GetSelectedRow()
        self.id = id = self.grilla.GetTextValue(row, 0)
        nomEditar = self.grilla.GetTextValue(row, 1)
        lista1.append(nomEditar)
        tipoEditar = self.grilla.GetTextValue(row, 2)
        lista1.append(tipoEditar)
        nacionalidadEditar = self.grilla.GetTextValue(row, 3)
        lista1.append(nacionalidadEditar)
        stockEditar = self.grilla.GetTextValue(row, 4)
        lista1.append(stockEditar)
        nicoEditar = self.grilla.GetTextValue(row, 5)
        lista1.append(nicoEditar)
        subTipEditar = self.grilla.GetTextValue(row, 6)
        lista1.append(subTipEditar)

        self.ventana = Frame (None, title = "Editar producto", size = (300,550))
        self.grilla2 = grilla2 = BoxSizer(HORIZONTAL)
        columStatick = BoxSizer (VERTICAL)
        columOpciones = BoxSizer (VERTICAL)
        proList = [["Tabaquil", "Frutal"],["Nacional", "Importado"], ["0", "3", "6"], ["Rubio", "Negro"]]
        self.listaEdicion = []
        j = 1
        k = 0
        for i in range(len(lista1)) :
            aux = StaticText(self.ventana, label = self.encabezado[i])
            columStatick.Add(aux, 1, ALL, 25)
            if j == 1:
                aux2 = TextCtrl(self.ventana, value = lista1[i])
                self.listaEdicion.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 19)
            elif j == 4:
                aux2 = TextCtrl(self.ventana, value = lista1[i], validator = MyValidator())
                self.listaEdicion.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 19)
            else:
                aux3 = ComboBox(self.ventana, 500, lista1[i], (0, 0), (160, -1), proList[k] , CB_DROPDOWN | TE_PROCESS_ENTER, validator = MyValidator() )
                self.listaEdicion.append(aux3)
                columOpciones.Add(aux3, 1, ALL, 19)
                k += 1
            j += 1
        botonAgregar = Button (self.ventana, -1, label = "Guardar", size = DefaultSize)
        botonCerrar = Button (self.ventana, -1 ,label = "Cerrar", size = DefaultSize)
        botonAgregar.Bind(EVT_BUTTON, self.guardarEdicionL)
        botonCerrar.Bind(EVT_BUTTON, self.CerrarEdicion)
        columOpciones.Add(botonCerrar, 1, RIGHT|LEFT|BOTTOM, 10)
        columStatick.Add(botonAgregar, 1, ALL, 10)
        self.grilla2.Add(columStatick)
        self.grilla2.Add(columOpciones)
        self.ventana.SetSizer(self.grilla2)
        self.ventana.Show()


    
    def guardarEdicionL (self, event):
        condi = True
        i = 0
        while condi and i <= len(self.listaEdicion) - 1 :
            if str(self.listaEdicion[i].GetValue()) == "" :
                condi = False
            i += 1
        if condi:
            nom = str(self.listaEdicion[0].GetValue())
            tipo = str(self.listaEdicion[1].GetValue())
            nac = str(self.listaEdicion[2].GetValue())
            cant = str(self.listaEdicion[3].GetValue())
            nicotina = str(self.listaEdicion[4].GetValue())
            subT = str(self.listaEdicion[5].GetValue())
            idl = self.id
            self.comparadorL += 1

            self.grilla.DeleteItem(self.grilla.GetSelectedRow())
            self.grilla.InsertItem(self.row, (self.id,nom,tipo,nac,cant,nicotina,subT))
            self.updateBDLiquidos(idl, nom, tipo, nac, cant, nicotina, subT)
            self.ventana.Close()
        else:
            self.cartelError("Falta Completar")
        
        


    def editarE (self, event):
        lista1 = []
        self.row1 = row = self.grillaE.GetSelectedRow()
        self.id1 = id = self.grillaE.GetTextValue(row, 0)
        nomEditar = self.grillaE.GetTextValue(row, 1)
        lista1.append(nomEditar)
        tipoEditar = self.grillaE.GetTextValue(row, 2)
        lista1.append(tipoEditar)
        bateriaEditar = self.grillaE.GetTextValue(row, 3)
        lista1.append(bateriaEditar)
        capacidadEditar = self.grillaE.GetTextValue(row, 4)
        lista1.append(capacidadEditar)
        cantidadEditar = self.grillaE.GetTextValue(row, 5)
        lista1.append(cantidadEditar)


        self.fEquipos1 = Frame (None, title = "Editar producto", size = (300,410))
        grillaE2 = BoxSizer(HORIZONTAL)
        columStatick = columStatick = BoxSizer (VERTICAL)
        columOpciones = columOpciones = BoxSizer (VERTICAL)
        List = [["RDA", "RTA"], ["1","2"], ["0 ml", "5 ml", "10 ml"]]
        self.listaE1 = []
        j = 1
        k = 0
        for i in range(len(self.encabezado2)) :
            aux = StaticText(self.fEquipos1, label = self.encabezado2[i])
            columStatick.Add(aux, 1, ALL, 25)
            if j == 1:
                aux2 = TextCtrl(self.fEquipos1, value = lista1[i])
                self.listaE1.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 19)
            elif j == 5:
                aux2 = TextCtrl(self.fEquipos1, value = lista1[i], validator = MyValidator())
                self.listaE1.append(aux2)
                columOpciones.Add(aux2, 1, ALL, 19)
            else:
                aux3 = ComboBox(self.fEquipos1, -1, lista1[i], (0, 0), (160, -1), List[k] , CB_DROPDOWN | TE_PROCESS_ENTER, validator = MyValidator() )
                self.listaE1.append(aux3)
                columOpciones.Add(aux3, 1, ALL, 19)
                k += 1
            j += 1

        print(self.listaE1)
        botonAgregar = Button (self.fEquipos1, -1, label = "Guardar", size = DefaultSize)
        botonCerrar = Button (self.fEquipos1, -1 ,label = "Cerrar", size = DefaultSize)
        botonAgregar.Bind(EVT_BUTTON, self.guardarE)
        botonCerrar.Bind(EVT_BUTTON, self.CerrarEdicionE)
        columOpciones.Add(botonCerrar, 1, RIGHT|LEFT|BOTTOM, 10)
        columStatick.Add(botonAgregar, 1, ALL, 10)
        grillaE2.Add(columStatick)
        grillaE2.Add(columOpciones)
        self.fEquipos1.SetSizer(grillaE2)
        self.fEquipos1.Show()

    def guardarE(self, event):
        condi = True
        i = 0
        while condi and i <= len(self.listaE1) - 1 :
            if str(self.listaE1[i].GetValue()) == "" :
                condi = False
            i += 1
        if condi:
            nom = str(self.listaE1[0].GetValue())
            tipo = str(self.listaE1[1].GetValue())
            bat = str(self.listaE1[2].GetValue())
            capa = str(self.listaE1[3].GetValue())
            cant = str(self.listaE1[4].GetValue())
        
            self.grillaE.DeleteItem(self.grillaE.GetSelectedRow())
            self.grillaE.InsertItem(self.row1, (self.id1,nom,tipo,bat,capa,cant))
            self.updateBDEquipos(self.id1, nom, tipo, bat, capa, cant)
            self.comparadorE += 1
            self.fEquipos1.Close()
            print("aca de nuevo pase")
        else:
            self.cartelError("Falta Completar")
        
        

    def restaStokL(self, producto, idl, cantARestar):
        print("Entre")
        print("Resto")
        listaLiquidos = self.recupBDLiquidos()
        listaEquipos = self.recupBDEquipos()
        valorAnterior = 0
        if producto == "liquidos":
            print("Entre liquidos")
            for e in listaLiquidos:
                valorAnterior = int(e[4])
                print ("ValorAnterior :", valorAnterior)
                print(e[0])
                if int(e[0]) == idl :
                    print("Encontre el producto: " + e[1])
                    e[4] = int(e[4]) - cantARestar
                    e[4] = int(e[4])
                    print("Reste de la base de datos", e[4])
                    if e[4] < 0 :
                        e[4] = valorAnterior
                        self.cartelStock("Esta restando mas del producto que posee en Stock o no posee mas stock del producto")
                    elif e[4] <= 20:
                        e[4] = str(e[4])
                        self.cartelStock("Quedan 20 o menos unidades de este producto. contactar provedor")
                        self.grilla.DeleteItem(idl-1)
                        self.grilla.InsertItem(idl-1, (e[0], e[1], e[2], e[3], e[4], e[5], e[6]))
                        self.updateBDLiquidos(e[0], e[1], e[2], e[3], e[4], e[5], e[6])
                    elif e[4] == 0:
                        e[4] = str(e[4])
                        self.cartelStock("Agoto el producto, contactar")
                        self.grilla.DeleteItem(idl-1)
                        self.grilla.InsertItem(idl-1, (e[0], e[1], e[2], e[3], e[4], e[5], e[6]))
                        self.updateBDLiquidos(e[0], e[1], e[2], e[3], e[4], e[5], e[6])
                    else:
                        print("updatie")
                        e[4] = str(e[4])
                        self.grilla.DeleteItem(idl-1)
                        self.grilla.InsertItem(idl-1, (e[0], e[1], e[2], e[3], e[4], e[5], e[6]))
                        self.updateBDLiquidos(e[0], e[1], e[2], e[3], e[4], e[5], e[6])
        elif producto == "equipos":
            for e in listaEquipos:
                valorAnterior = int(e[5])
                print ("ValorAnterior :", valorAnterior)
                print(e[0])
                if int(e[0]) == idl :
                    print("Encontre el producto: " + e[1])
                    e[5] = int(e[5]) - cantARestar
                    e[5] = int(e[5])
                    print("Reste de la base de datos", e[4])
                    if e[5] < 0 :
                        e[5] = valorAnterior
                        self.cartelStock("Esta restando mas del producto que posee en Stock o no posee mas unidades del producto")
                    elif e[5] <= 20 :
                        self.cartelStock("Se encuentra con 20 o menos unidades. Contactar proveedor")
                        e[5] = str(e[5])
                        self.grillaE.DeleteItem(idl-1)
                        self.grillaE.InsertItem(idl-1, (e[0], e[1], e[2], e[3], e[4], e[5]))
                        self.updateBDEquipos(e[0], e[1], e[2], e[3], e[4], e[5])
                    elif e[5] == 0:
                        print("deleteo")
                        self.cartelStock("Agoto el producto. Contacte a su proveedor")
                        e[5] = str(e[5])
                        self.grillaE.DeleteItem(idl-1)
                        self.grillaE.InsertItem(idl-1, (e[0], e[1], e[2], e[3], e[4], e[5]))
                        self.updateBDEquipos(e[0], e[1], e[2], e[3], e[4], e[5])
                    else:
                        print("updatie")
                        e[5] = str(e[5])
                        self.grillaE.DeleteItem(idl-1)
                        self.grillaE.InsertItem(idl-1, (e[0], e[1], e[2], e[3], e[4], e[5]))
                        self.updateBDEquipos(e[0], e[1], e[2], e[3], e[4], e[5])
      
        
    def obtenerID (self, tipo, nombre):
            if tipo == "liquidos":
                lista = self.recupBDLiquidos()
            elif tipo == "equipos":
                lista = self.recupBDEquipos()
            idob = 0
            for liquido in lista:   
                if liquido[1] == nombre:
                    print("Encontre el nombre: "+ liquido[1])
                    idob = int(liquido[0])
                else: 
                    print("No encontre nada")

            return int(idob)

    
## Comienza funcion Buscar Liquidos

    def buscar(self, event):
        lista = self.recupBDLiquidos()
        print("--------------------------")
        busco = self.search.GetValue()
        num = self.search.GetLastPosition()
        tot = self.grilla.GetItemCount()
        for i in range(tot):
            self.grilla.DeleteItem(0)

        for i in range(len(lista)):
            if busco == lista[i][1][:num]:
                self.grilla.AppendItem(lista[i])
                print("#", lista[i][1])

## Termina funcion Buscar Liquidos


## Comienza función Buscar Equipos

    def buscarE (self, e):
        lista = self.recupBDEquipos()
        print("--------------------------")
        busco = self.searchE.GetValue()
        num = self.searchE.GetLastPosition()
        tot = self.grillaE.GetItemCount()
        for i in range(tot):
            self.grillaE.DeleteItem(0)

        for i in range(len(lista)):
            if busco == lista[i][1][:num]:
                self.grillaE.AppendItem(lista[i])
                print("#", lista[i][1])

    def CerrarEdicionE (self, event):
        self.fEquipos1.Close()

    def CerrarEdicion(self, event):
        self.ventana.Close()


    def Cerrar (self, event):
        self.ff.Close()

    def CerrarE (self, event):
        self.fEquipos.Close()

    def CerrarError (self, event):
        self.error.Close()

    def CerrarErrorStock (self, event):
        self.errorStock.Close()
app = MyApp()
app.MainLoop()