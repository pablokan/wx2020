from wx import *
import sqlite3
from datetime import *
from wx.adv import *
from wx.dataview import *
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
from validador import *

class MyApp(App):
    def OnInit(self):
        self.f = f = Frame(None, -1, 'Inversiones Personales', size =(800,550), pos = (200,70))
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        font = Font(16, DECORATIVE, ITALIC, BOLD, underline = True) #formato para el titulo
        self.st = st = StaticText(p, label="Cartera de Inversiones Financieras")
        self.image = image = StaticBitmap(p, -1, Bitmap("C:\itec\prog1\EFI\imagen.png", BITMAP_TYPE_ANY))
        st.SetFont(font) # le asigno el formato a st
        s.Add(st, 0, ALL|ALIGN_CENTER, 20)
        s.Add(image, 0, ALL|EXPAND, 20)
        p.SetSizer(s)

        f.CreateStatusBar() #menu
        f.SetStatusText("Menu de Inicio")
        menuBar = MenuBar()

        menu1 = Menu() # creo el menu 1
        menu1.Append(101, "Cartera", "Ver la cartera actual")
        menu1.Append(102, "Resultados", "Obtener resultados de operaciones cerradas")
        menu1.Append(103, "Movimientos", "Ver todos los movimientos")
        menu1.AppendSeparator()
        menu1.Append(104, "Salir", "Cerrar el programa")
        menuBar.Append(menu1, "Cuenta")

        menu2 = Menu()
        menu2.Append(201, "Acciones")
        menu2.Append(202, "Cedears")
        menu2.Append(203, "Dolares")
        menu2.Append(204, "Plazos Fijos")
        menuBar.Append(menu2, "Operar")

        menu3 = Menu()
        menu3.Append(301, "Cotizaciones")
        menu3.Append(302, "Configuracion inicial")
        menuBar.Append(menu3, "Informacion")

        menu4 = Menu()
        menu4.Append(401, "Instrucciones")
        menu4.Append(402, "Acerca de")
        menuBar.Append(menu4, "Ayuda")

        f.SetMenuBar(menuBar)

        idList = [101,102,103,104,201,202,203,204,301,302,304,305,401,402]
        for e in idList:
            f.Bind(EVT_MENU, self.barraMenu, id=e)
        
        f.Show()
        return True
        
    def barraMenu(self, event):
        id = event.GetId()
        if id == 201:
            self.acciones(self)
            self.esp = "Acciones"
        if id == 202:
            self.cedears(self)
            self.esp = "Cedears"
        if id == 203:
            self.dolares(self)    
        if id == 204:
            self.plazoFijo(self)
        if id == 101:
            self.cartera(self)
        if id == 102:
            self.resultadoglobal(self)    
        if id == 103:
            self.movimientos(self)
        if id == 104:
            self.f.Close()    
        if id == 301:
            self.cotizaciones(self)    
        if id == 302:
            self.configInicial(self)
        if id == 401:
            self.instrucciones(self)    
        if id == 402:
            self.acercaDe(self)

    def acciones(self, event): 
        f2 = Frame(None, size=(250, 680), pos = (500,30), title = "Acciones")
        p2 = Panel(f2)
        s2 = BoxSizer(VERTICAL)

        listaOpciones = ["Compra", "Venta"] #boton de compra o venta
        self.opcion = RadioBox(p2, choices = listaOpciones)
        s2.Add(self.opcion,0,CENTER)

        st0 = StaticText(p2,-1,"Seleccione fecha:") #seleccionar fecha
        dpc1 = DatePickerCtrl(p2, style = DP_DROPDOWN|DP_SHOWCENTURY|DP_ALLOWNONE|TAB_TRAVERSAL)
        dpc1.Bind(EVT_DATE_CHANGED, self.fechaInicial, dpc1)
        s2.Add(st0,0,ALL,10)
        s2.Add(dpc1,0,EXPAND|ALL,10)

        st1 = StaticText(p2,-1,"Seleccione especie:") #listado para seleccionar la especie (accion)
        listaTickers = ["alua.ba",'bbar.ba','bma.ba', 'byma.ba', 'cepu.ba', "come.ba",'cres.ba',"cvh.ba","edn.ba",'ggal.ba',
                'mirg.ba', 'pamp.ba', 'supv.ba','teco2.ba', 'tgno4.ba', 'tgsu2.ba', 'tran.ba', 'txar.ba', 'valo.ba','ypfd.ba']
        self.lb1 = ListBox(p2, -1, (100, 50), (90, 120), listaTickers)
        s2.Add(st1,0,ALL,5)
        s2.Add(self.lb1,0,EXPAND|ALL,10)
   
        st2 = StaticText(p2,-1,"Cantidad:")
        self.t2 = TextCtrl(p2,-1,validator=MyValidator())
        s2.Add(st2,0,ALL,5)
        s2.Add(self.t2,0,ALL|EXPAND,10)

        st3 = StaticText(p2,-1,"Precio:")
        self.t3 = TextCtrl(p2,-1,validator=MyValidator())
        s2.Add(st3,0,ALL,5)
        s2.Add(self.t3,0,ALL|EXPAND,10)

        c = Button(p2, -1, "Conocer última cotización")#Boton de la ultima cotización
        s2.Add(c, flag = CENTER)
        c.Bind(EVT_BUTTON, self.obtenerCotizacion)
        self.busquedaCot = StaticText(p2)
        s2.Add(self.busquedaCot, flag = CENTER)
        p2.SetSizer(s2)
        
        st4 = StaticText(p2,-1, "Importe Bruto: ")
        self.st4 = StaticText(p2,-1)#para setear el importe bruto
        s2.Add(st4,0,EXPAND|ALL,5)
        s2.Add(self.st4,0,EXPAND|ALL,10)

        st5 = StaticText(p2,-1, "Importe Neto: ")
        self.st5 = StaticText(p2,-1) #para setear importe neto
        font2 = Font(11, DECORATIVE, ITALIC, BOLD, underline = False)
        self.st5.SetFont(font2)
        s2.Add(st5,0,EXPAND|ALL,5)
        s2.Add(self.st5,0,EXPAND|ALL,10)
        p2.SetSizer(s2)

        b = Button(p2, -1, "Grabar Operacion")
        s2.Add(b, flag = CENTER)
        b.Bind(EVT_BUTTON, self.grabaOp)
        self.resultadoBruto = StaticText(p2)
        s2.Add(self.resultadoBruto, flag = CENTER)
        self.resultadoNeto = StaticText(p2)
        s2.Add(self.resultadoNeto, flag = CENTER)
        p2.SetSizer(s2)
        f2.Show()
        return True

    def cedears(self, event): 
        f2 = Frame(None, size=(250, 680), pos = (500,30), title = "Cedears")
        p2 = Panel(f2)
        s2 = BoxSizer(VERTICAL)

        listaOpciones = ["Compra", "Venta"] #boton de compra o venta
        self.opcion = RadioBox(p2, choices = listaOpciones)
        s2.Add(self.opcion,0,CENTER)

        st0 = StaticText(p2,-1,"Seleccione fecha:") #seleccionar fecha
        dpc1 = DatePickerCtrl(p2, style = DP_DROPDOWN|DP_SHOWCENTURY|DP_ALLOWNONE|TAB_TRAVERSAL)
        dpc1.Bind(EVT_DATE_CHANGED, self.fechaInicial, dpc1)
        s2.Add(st0,0,ALL,10)
        s2.Add(dpc1,0,EXPAND|ALL,10)

        st1 = StaticText(p2,-1,"Seleccione especie:") #listado para seleccionar la especie (accion)
        listaTickers = ["aapl.ba",'amd.ba','bac.ba', 'baba.ba', 'bbd.ba', "desp.ba",'disn.ba',"fb.ba","ge.ba",'googl.ba',
                'ibm.ba', 'intc.ba', 'ko.ba','mcd.ba', 'meli.ba', 'msft.ba', 'nflx.ba', 'noka.ba', 'nvda.ba','pbr.ba','pg.ba',
                'qcom.ba','ten.ba','tsla.ba','twtr.ba','vale.ba','vist.ba']
        self.lb1 = ListBox(p2, -1, (100, 50), (90, 120), listaTickers)
        s2.Add(st1,0,ALL,5)
        s2.Add(self.lb1,0,EXPAND|ALL,10)
   
        st2 = StaticText(p2,-1,"Cantidad:")
        self.t2 = TextCtrl(p2,-1,validator=MyValidator())
        s2.Add(st2,0,ALL,5)
        s2.Add(self.t2,0,ALL|EXPAND,10)

        st3 = StaticText(p2,-1,"Precio:")
        self.t3 = TextCtrl(p2,-1,validator=MyValidator())
        s2.Add(st3,0,ALL,5)
        s2.Add(self.t3,0,ALL|EXPAND,10)

        c = Button(p2, -1, "Conocer última cotización")#Boton de la ultima cotización
        s2.Add(c, flag = CENTER)
        c.Bind(EVT_BUTTON, self.obtenerCotizacion)
        self.busquedaCot = StaticText(p2)
        s2.Add(self.busquedaCot, flag = CENTER)
        p2.SetSizer(s2)
        
        st4 = StaticText(p2,-1, "Importe Bruto: ")
        self.st4 = StaticText(p2,-1)#para setear el importe bruto
        s2.Add(st4,0,EXPAND|ALL,5)
        s2.Add(self.st4,0,EXPAND|ALL,10)

        st5 = StaticText(p2,-1, "Importe Neto: ")
        self.st5 = StaticText(p2,-1) #para setear importe neto
        font2 = Font(11, DECORATIVE, ITALIC, BOLD, underline = False)
        self.st5.SetFont(font2)
        s2.Add(st5,0,EXPAND|ALL,5)
        s2.Add(self.st5,0,EXPAND|ALL,10)
        p2.SetSizer(s2)

        b = Button(p2, -1, "Grabar Operacion")
        s2.Add(b, flag = CENTER)
        b.Bind(EVT_BUTTON, self.grabaOp)
        self.resultadoBruto = StaticText(p2)
        s2.Add(self.resultadoBruto, flag = CENTER)
        self.resultadoNeto = StaticText(p2)
        s2.Add(self.resultadoNeto, flag = CENTER)
        p2.SetSizer(s2)
        f2.Show()
        return True
      
    def cotizaciones(self,event):
        import accederPaginaExterna #llamamos al archivo con la clase para mostrar la pagina
        f2 = Frame(None, title = "Cotizaciones", size = (1200,600), pos = (110,30))
        cotiz = accederPaginaExterna.Web(f2,"http://www.rava.com/precios/panel.php?m=LID")
        f2.Show()

    def obtenerCotizacion(self, event): #hace la consulta a la API
        self.busquedaCot = last_price = si.get_quote_table(self.lb1.GetStringSelection())["Quote Price"]
        cartel = MessageBox("Ultima cotizacion de " + self.lb1.GetStringSelection() + " en el mercado: $" + str(round(self.busquedaCot,2)))
        
    def grabaOp(self, event):
        try:
            self.conectarCostos() #llamamos a la funcion para poder obtener el costo total y asi calcular el rtdo neto
            numero1 = int(self.t2.GetValue())
            numero2 = float(self.t3.GetValue())
            resultadoBruto = str(round((numero1 *  numero2),2))
            self.st4.SetLabel(resultadoBruto)
            if self.opcion.GetString(self.opcion.GetSelection()) == "Compra": #compra
                resultadoNeto = round((numero1 *  numero2) + ((numero1 *  numero2)* (self.costoTotal/100)),2)
            else: #venta
                resultadoNeto = round((numero1 *  numero2) - ((numero1 *  numero2)* (self.costoTotal/100)),2)
            resultadoNeto = str(resultadoNeto)
            self.st5.SetLabel(resultadoNeto)     
            tipo = self.opcion.GetString(self.opcion.GetSelection()) #resultado de la eleccion del radiobotton
            if tipo == "Compra":
                tipo = "Entrada"
                cantNegativa = int(self.t2.GetValue()) * - 1
                cant = str(cantNegativa)
                montoNegativo = float(resultadoNeto) * - 1
                monto = str(montoNegativo)           
            else:
                tipo = "Salida"
                cant = self.t2.GetValue()
                monto = resultadoNeto
            subesp = self.lb1.GetStringSelection() #resultado de la eleccion del activo (del listado)
            fecha = self.fi.Format("%d-%m-%Y")
            tna = "-"
            con = sqlite3.connect("inversiones.db")
            cur = con.cursor()
            alta = f"INSERT INTO datos (Tipo, Especie, Subespecie, Fecha, Cantidad, Monto, TNA) VALUES ('{tipo}','{self.esp}','{subesp}','{fecha}','{cant}','{monto}','{tna}')"
            cur.execute(alta)
            con.commit()
            con.close()
            cartel = MessageBox("La operacion ha sido registrada con exito.")
        except:
            cartel2 = MessageBox("Error: verifique fecha")        

    def dolares(self, event):
        import valorDolarHoy
        f2 = Frame(None, size=(250, 550), pos = (500,140),title = "Dolares")
        p2 = Panel(f2)
        s2 = BoxSizer(VERTICAL)

        st10 = StaticText(p2,-1,"Seleccione fecha:")
        dpc1 = DatePickerCtrl(p2, style = DP_DROPDOWN|DP_SHOWCENTURY|DP_ALLOWNONE|TAB_TRAVERSAL)
        dpc1.Bind(EVT_DATE_CHANGED, self.fechaInicial, dpc1)
        s2.Add(st10,0,EXPAND|ALL,10)
        s2.Add(dpc1,0,EXPAND|ALL,10)
        
        listaOperacion = ["Comprar", "Vender"]
        self.opcion = RadioBox(p2, choices=listaOperacion)
        st1 = StaticText(p2,-1,"Dolar Blue - Tipo de cambio actual:")
        self.tipoDeCambio = valorDolarHoy.cotizacionBlue
        stblanco = StaticText(p2,-1,"")
        self.t1 = StaticText(p2,-1, label=str(self.tipoDeCambio)) #cotizacion del dolar asignada para que lo muestre
        s2.Add(self.opcion,0,EXPAND|ALL,10)
        s2.Add(st1,0,EXPAND|ALL,10)
        s2.Add(self.t1,0,CENTER,10)
        s2.Add(stblanco)

        stUsd = StaticText(p2,-1,"Tipo de Cambio de la Operación:")
        self.cotUsd = TextCtrl(p2,-1,validator=MyValidator())
        s2.Add(stUsd,0,EXPAND|ALL,10)
        s2.Add(self.cotUsd,0,ALIGN_CENTRE|ALL,5)

        m1 = StaticText(p2,-1,"Cantidad de Dolares:")
        self.m2 = TextCtrl(p2,-1,validator=MyValidator())
        s2.Add(m1,0,EXPAND|ALL,10)
        s2.Add(self.m2,0,ALIGN_CENTRE|ALL,5)

        b = Button(p2, -1, "Grabar Operacion") 
        s2.Add(b, 0,ALIGN_CENTRE|ALL,20)
        b.Bind(EVT_BUTTON, self.grabaDolares)

        p2.SetSizer(s2)

        st4 = StaticText(p2,-1, "Importe total en pesos: ")
        self.resultado = StaticText(p2,-1)
        font2 = Font(11, DECORATIVE, ITALIC, BOLD, underline = False)
        self.resultado.SetFont(font2)
        s2.Add(st4,0,EXPAND|ALL,5)
        s2.Add(self.resultado,CENTER,5)

        f2.Show()
        return True

    def grabaDolares(self, event):
        try:
            numero1 = float(self.cotUsd.GetValue())
            numero2 = float(self.m2.GetValue())
            resultado = str(round(numero1 * numero2,2))
            self.resultado.SetLabel(resultado)  
            tipo = self.opcion.GetString(self.opcion.GetSelection()) #resultado de la eleccion del radiobotton
            if tipo == "Comprar":
                tipo = "Entrada"
                numero2 = float(self.m2.GetValue()) *-1
                resultado = str(round(numero1 * numero2,2))
            else:
                tipo = "Salida"  
            esp = "Dolares"
            subesp = "Dolares"
            fechaI = self.fi.Format("%d-%m-%Y")
            tna = "-"
            con = sqlite3.connect("inversiones.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM datos")
            alta = f"INSERT INTO datos (Tipo, Especie, Subespecie, Fecha, Cantidad, Monto, TNA) VALUES ('{tipo}','{esp}','{subesp}','{fechaI}','{numero2}','{resultado}','{tna}')"
            cur.execute(alta)
            con.commit()
            con.close()
            cartel = MessageBox("La operacion ha sido registrada con exito.")
        except:
            cartel2 = MessageBox("Error: verifique fecha")    
       
    def plazoFijo(self, event): # abre la ventana para generar un plazo fijo
        f2 = Frame(None, size=(300, 550), pos = (500,140), title = "Plazo Fijo")
        p2 = Panel(f2)
        s2 = BoxSizer(VERTICAL)
        
        st10 = StaticText(p2,-1,"Seleccione fecha inicial:")
        dpc1 = DatePickerCtrl(p2, style = DP_DROPDOWN|DP_SHOWCENTURY|DP_ALLOWNONE|TAB_TRAVERSAL)
        dpc1.Bind(EVT_DATE_CHANGED, self.fechaInicial, dpc1)
        s2.Add(st10,0,EXPAND|ALL,10)
        s2.Add(dpc1,0,EXPAND|ALL,10)

        st11 = StaticText(p2,-1,"Seleccione fecha final:")
        dpc2 = DatePickerCtrl(p2, style = DP_DROPDOWN|DP_SHOWCENTURY|DP_ALLOWNONE)
        dpc2.Bind(EVT_DATE_CHANGED, self.fechaFinal, dpc2)
        s2.Add(st11,0,EXPAND|ALL,10)
        s2.Add(dpc2,0,EXPAND|ALL,10)
        
        st2 = StaticText(p2,-1,"Cantidad de dias seleccionados:") #mostrar los dias en el frame
        s2.Add(st2,0,EXPAND|ALL,10)
        self.st0 = StaticText(p2, -1)
        s2.Add(self.st0,0,EXPAND|ALL,10)

        st1 = StaticText(p2,-1,"Capital Inicial")
        self.t1 = TextCtrl(p2,-1,validator=MyValidator()) #capital inicial

        st3 = StaticText(p2,-1,"Tasa Nominal Anual")
        font2 = Font(11, DECORATIVE, ITALIC, BOLD, underline = False)
        self.t3 = TextCtrl(p2,-1,validator=MyValidator()) # tasa
        self.st4 = StaticText(p2,-1)
        self.st4.SetFont(font2)
        st5 = StaticText(p2,-1, "Capital Final: ")
        s2.Add(st1,0,EXPAND|ALL,10)
        s2.Add(self.t1,0,EXPAND|ALL,10)

        s2.Add(st3,0,EXPAND|ALL,10)
        s2.Add(self.t3,0,EXPAND|ALL,10)
        s2.Add(st5,0,EXPAND|ALL,10)
        s2.Add(self.st4,0,EXPAND|ALL,10)
        p2.SetSizer(s2)

        b = Button(p2, -1, "Grabar Operacion") # boton para grabar plazo fijo
        s2.Add(b, flag = CENTER)
        b.Bind(EVT_BUTTON, self.grabaPF)
        self.resultado = StaticText(p2)
        s2.Add(self.resultado, flag = CENTER)
        p2.SetSizer(s2)
        f2.Show()
        return True  

    def fechaInicial(self, e):
        self.fi = e.GetDate()
        fecha = self.fi.Format("%d-%m-%Y")
        self.anioI = int(fecha[6:])
        self.mesI =int(fecha[3:5])
        self.diaI = int(fecha[:2])
       
    def fechaFinal(self, e):
        self.ff = e.GetDate()
        fecha = self.ff.Format("%d-%m-%Y")
        self.anioF = int(fecha[6:])
        self.mesF =int(fecha[3:5])
        self.diaF = int(fecha[:2])
        ff = date(self.anioF,self.mesF,self.diaF)
        fi = date(self.anioI,self.mesI,self.diaI)
        self.diasDif = (ff-fi).days
        self.st0.SetLabel(str(self.diasDif)) #seteamos el label en el frame de Plazo fijo (muestra los dias)

    def grabaPF(self, event): # graba el plazo fijo en la base de datos
        try:
            numero1 = float(self.t1.GetValue())
            numero2 = self.diasDif #
            numero3 = float(self.t3.GetValue())
            resultado = str(round(numero1 * (1 + (numero3/365*numero2)/100),2))
            self.st4.SetLabel(resultado)
            capIniNeg = numero1 * - 1 #agregue para que quede negativo sin tener que tocar todo
            cartel = MessageBox("La operacion ha sido registrada con exito.")
            tipoE = "Entrada"
            tipoS = "Salida"
            esp = "Plazo Fijo"
            subesp = "Plazo Fijo"
            fechaI = self.fi.Format("%d-%m-%Y")
            fechaF =self.ff.Format("%d-%m-%Y")
            cant = 1
            cantNeg = - 1 # para que quede negativa la cantidad
            montoF = resultado
            tna = self.t3.GetValue()
            con = sqlite3.connect("inversiones.db")
            cur = con.cursor()
            alta = f"INSERT INTO datos (Tipo, Especie, Subespecie, Fecha, Cantidad, Monto, TNA) VALUES ('{tipoE}','{esp}','{subesp}','{fechaI}','{cantNeg}','{capIniNeg}','{tna}')"
            cur.execute(alta)
            alta1 = f"INSERT INTO datos (Tipo, Especie, Subespecie, Fecha, Cantidad, Monto, TNA) VALUES ('{tipoS}','{esp}','{subesp}','{fechaF}','{cant}','{resultado}','{tna}')"
            cur.execute(alta1)
            con.commit()
            con.close()
        except:
            cartel2 = MessageBox("Error: verifique fechas")

    def configInicial(self,e):
        self.listaConfig = []
        f = self.f = Frame(None, -1, "Configuracion Inicial", size =(350,350),pos = (400,120))
        panel = self.panel = Panel(f)
        sizer = self.sizer = BoxSizer(VERTICAL)
        cartel = StaticText(panel, -1, "Comision en Acciones/Cedears %:")
        self.x1 = TextCtrl(panel,validator=MyValidator())
        cartel2 = StaticText(panel, -1, "Derechos de mercado en % :")
        self.x2 = TextCtrl(panel,validator=MyValidator())
        cartel3 = StaticText(panel, -1, "IVA sobre comision + Dchos. de mercado en % :")
        self.x3 = TextCtrl(panel,validator=MyValidator())
        blanco = StaticText(panel, -1, "")
        blanco2 = StaticText(panel, -1, "")
        blanco3 = StaticText(panel, -1, "")
        sizer.Add(cartel, 0)
        sizer.Add(self.x1,0)
        sizer.Add(blanco,0)
        sizer.Add(cartel2, 0)
        sizer.Add(self.x2,0)
        sizer.Add(blanco2,0)
        sizer.Add(cartel3, 0)
        sizer.Add(self.x3,0)
        sizer.Add(blanco3, 0)
        panel.SetSizer(sizer)
        b = Button(panel, -1, "Guardar Configuracion") # boton para grabar plazo fijo
        sizer.Add(b, flag = CENTER)
        b.Bind(EVT_BUTTON, self.guardaConfiguracion)
        self.resultado = StaticText(panel)
        sizer.Add(self.resultado, flag = CENTER)
        panel.SetSizer(sizer)
        self.conectarCostos() #llama a la funcion para obtener los valores de los costos actuales
        self.datosHistoricos() #llama a la funcion para mostrar los costos historicos en el frame
        f.Show()
        return True

    def conectarCostos(self): #llama a la base de datos y se fija cual fue el ultimo seteo de costos
        con = sqlite3.connect("inversiones.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM costos")
        tuplas = cur.fetchall()
        self.listaA = listaA = [list(e) for e in tuplas]
        for e in listaA:
            for i in range(4):
                e[i] = str(e[i])
        con.close()
        self.costoTotal = float(listaA[len(listaA) -1][4])
        
    def datosHistoricos(self): #sirve para mostrar en el frame de configuracion los ultimos datos seteados
        font = Font(10, DECORATIVE, ITALIC, NORMAL, underline = True)
        font2 = Font(10, DECORATIVE, ITALIC, BOLD, underline = False)
        titulo = StaticText(self.panel, -1, "Ultima configuración de datos guardada:" )
        titulo.SetFont(font)
        comisionGuardada = StaticText(self.panel, -1, "Comision: " + str(self.listaA[len(self.listaA) -1][1]) + "%")
        dchoMGuardado = StaticText(self.panel, -1, "Derechos de Mercado: " + str(self.listaA[len(self.listaA) -1][2])+ "%")
        ivaGuardado = StaticText(self.panel, -1, "IVA sobre comision + Dchos. de mercado: " + str(self.listaA[len(self.listaA) -1][3])+ "%")
        cTotalGuardado = StaticText(self.panel, -1, "Costo Total: " + str(self.listaA[len(self.listaA) -1][4])+ "%")
        cTotalGuardado.SetFont(font2)
        self.sizer.Add(titulo, 0)
        self.sizer.Add(comisionGuardada, 0)
        self.sizer.Add(dchoMGuardado, 0)
        self.sizer.Add(ivaGuardado, 0)
        self.sizer.Add(cTotalGuardado, 0)

    def guardaConfiguracion(self, event): #para configurar los costos (se ejecuta con el boton en configuracion)
        comision = float(self.x1.GetValue())
        dchoMercado = float(self.x2.GetValue())
        iva = float(self.x3.GetValue())
        costoTotal = float((comision + dchoMercado) + (comision + dchoMercado) * (iva/100))
        con = sqlite3.connect("inversiones.db")
        cur = con.cursor()
        alta = f"INSERT INTO costos (comision, dcho_mercado, iva, costo_total) VALUES ('{comision}','{dchoMercado}','{iva}','{costoTotal}')"
        cur.execute(alta)
        con.commit()
        con.close() 
        cartel = MessageBox("Configuracion guardada con exito.")
        self.f.Close()

    def cartera(self, event):
        import valorDolarHoy
        con = sqlite3.connect("inversiones.db")
        cur = con.cursor()
        cur.execute("SELECT Subespecie,sum(Cantidad),sum(Monto) FROM datos GROUP BY Subespecie")
        tuplas = cur.fetchall()

        lista0 = [list(e) for e in tuplas]
        for e in lista0:
            for i in range(3):
                e[i] = str(e[i])
        con.close()
        listaA = []
        for i in range(len(lista0)):
            if lista0[i][1] != "0.0":
                listaA.append(lista0[i])

        for i in range(len(listaA)):               
            if listaA[i][0] == "Dolares":
                totalDolar = (float(listaA[i][1])*-1) * float(valorDolarHoy.blueCompra)
                listaA[i][1] = str(float(listaA[i][1])*-1)
                listaA[i].insert(2,str(totalDolar))
                listaA[i].pop()
            elif listaA[i][0] == "Plazo Fijo":
                totalPlazoFijo = float(listaA[i][2])
                
            else:
                activo = str(listaA[i][0])
                last_price = si.get_quote_table(activo)["Quote Price"]
                resultado = round(float(last_price) * (float(listaA[i][1])*-1),2)
                listaA[i].insert(2,str(resultado))
                listaA[i].pop()
                listaA[i].insert(1,str(float(listaA[i][1])*-1))
                listaA[i].pop(2)

        listaB = []
        for i in range(len(listaA)): 
            if listaA[i][0] != "Plazo Fijo":
                listaB.append(listaA[i])

        f = Frame(None, -1, "Cartera", size=(300, 400))
        p = Panel(f)
        self.dvlc = dvlc = DataViewListCtrl(p)
        dvlc.AppendTextColumn('Subespecie')
        dvlc.AppendTextColumn('Cantidad')
        dvlc.AppendTextColumn('Monto actual')

        for e in listaB:
            dvlc.AppendItem(e)

        for c in self.dvlc.Columns: #para ordenar la tabla tocando sobre los titulo
            c.Sortable = True
            c.Reorderable = True

        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        p.SetSizer(sizer)
        f.Show()
        return True
       
    def resultadoglobal(self, event):
        con = sqlite3.connect("inversiones.db")
        cur = con.cursor()
        cur.execute("SELECT Tipo,Subespecie, sum(Cantidad), sum(Monto) FROM datos WHERE Tipo = 'Entrada' GROUP BY Subespecie ")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            for i in range(4):
                e[i] = str(e[i])
        con.close()
        for i in range(len(listaA)):
            precioCompra = float(listaA[i][3]) / float(listaA[i][2])
            listaA[i].append(str(precioCompra))
        con = sqlite3.connect("inversiones.db")
        cur = con.cursor()
        cur.execute("SELECT Tipo,Subespecie, sum(Cantidad), sum(Monto) FROM datos WHERE Tipo = 'Salida' GROUP BY Subespecie ")
        tuplas = cur.fetchall()
        listaB = [list(e) for e in tuplas]
        for e in listaB:
            for i in range(4):
                e[i] = str(e[i])
        con.close()
        for i in range(len(listaB)):
            precioVenta = float(listaB[i][3]) / float(listaB[i][2])
            listaB[i].append(str(precioVenta))
        for i in range(len(listaA)):
            for a in range(len(listaB)):
                if listaB[a][1] == listaA[i][1]:
                    rtdo = "$" + str(round((float(listaB[a][4]) - float(listaA[i][4])) * float(listaB[a][2]),2))
                    listaB[a].insert(5,rtdo)
        for i in range(len(listaB)):
            listaB[i].pop(4)
            listaB[i].pop(0)
            listaB[i].pop(1)
            listaB[i].pop(1)

        f = Frame(None, -1, "Resultados", size=(250, 500)) #este es el frame cuando tocamos "Resultados"
        p = Panel(f)
        self.dvlc = dvlc = DataViewListCtrl(p)
        dvlc.AppendTextColumn('Subespecie')
        dvlc.AppendTextColumn('Resultado Neto')

        for e in listaB:
            dvlc.AppendItem(e)

        for c in self.dvlc.Columns: # con esto podemos ordenar la tabla tocando sobre el titulo que queremos
            c.Sortable = True
            c.Reorderable = True

        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        p.SetSizer(sizer)
        f.Show()
        return True

    def movimientos(self, event): #muestra los movimientos
        con = sqlite3.connect("inversiones.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM datos")
        tuplas = cur.fetchall()

        listaA = [list(e) for e in tuplas]
        for e in listaA:
            for i in range(8):
                e[i] = str(e[i])
        con.close()

        for i in range(len(listaA)): 
            if listaA[i][1] == "Entrada":
                listaA[i][5] = str(float(listaA[i][5])*-1)
                listaA[i][6] = str(float(listaA[i][6])*-1)


        f = Frame(None, -1, "Movimientos", size=(700, 500))
        p = Panel(f)
        self.dvlc = dvlc = DataViewListCtrl(p)
        dvlc.AppendTextColumn('Id')
        dvlc.AppendTextColumn('Tipo')
        dvlc.AppendTextColumn('Especie')
        dvlc.AppendTextColumn('Subespecie')
        dvlc.AppendTextColumn('Fecha')
        dvlc.AppendTextColumn('Cantidad')
        dvlc.AppendTextColumn('Monto')
        dvlc.AppendTextColumn('TNA')
        for e in listaA:
            dvlc.AppendItem(e)

        for c in self.dvlc.Columns: #para ordenar la tabla tocando sobre los titulo
            c.Sortable = True
            c.Reorderable = True

        dvlc.SelectRow(0)
        hor = BoxSizer(HORIZONTAL) #generar el boton de abajo que dice "borrar"
        bB = Button(p, -1, "&Borrar")
        hor.Add(bB)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        bB.Bind(EVT_BUTTON, self.borrar)
        sizer.Add(hor)
        p.SetSizer(sizer)
        f.Show()
        return True

    def borrar(self, event): #accion de borrar
        def borraBD(id):
                con = sqlite3.connect("inversiones.db")
                cur = con.cursor()
                dele = f"DELETE from datos WHERE id={id}"
                cur.execute(dele)
                con.commit()
                con.close()
        d = Dialog(None, size =(200,200))
        s = BoxSizer(VERTICAL)
        st1 = StaticText(d, -1, '¿Desea borrar el movimiento?')
        okB = Button(d, ID_OK)
        caB = Button(d, ID_CANCEL)
        flags = ALIGN_CENTER|ALL
        s.Add(st1, 0, flags, 10)
        s.Add(okB, 0, flags, 10)
        s.Add(caB, 0, flags, 10)
        d.SetSizer(s)
        if d.ShowModal() == ID_OK: 
            row = self.dvlc.GetSelectedRow() #obtengo la fila donde estoy parado
            id = self.dvlc.GetTextValue(row, 0) 
            self.dvlc.DeleteItem(row)
            borraBD(id) #llama a la funcion para borrarlo de la base de datos
            self.dvlc.SelectRow(0)
        d.Destroy()    
        return True

    def acercaDe(self,event):
        font = Font(11, DECORATIVE, ITALIC, BOLD, underline = True)
        font2 = Font(8, DECORATIVE, ITALIC, BOLD, underline = False)
        font3 = Font(8, DECORATIVE, ITALIC, NORMAL, underline = False)
        f = Frame(None, -1, "Acerca de ", size = (660,210), pos = (400,120))
        panel = Panel(f)
        sizer = BoxSizer(VERTICAL)
        version = StaticText(panel, -1, "\nVersion: 1.0\n\n")
        version.SetFont(font)
        cartelito = StaticText(panel, -1, "El software Cartera de Inversiones Financieras es una obra intelectual creada por Alvaro Perez Garcia y Lucas Pastrana Parrello.\n\nEl uso y distribución del software Cartera de Inversiones Financieras está reservado solo a sus creadores\nCualquier uso del Software sin autorización de sus creadores constituye una infracción a los derechos de autor.\nProhibida su reproducción.Reservados todos los derechos del autor.")
        cartelito.SetFont(font3)
        fecha = StaticText(panel, -1,"\nNoviembre de 2020 - Rio Cuarto, Córdoba, Argentina.")
        fecha.SetFont(font2)
        sizer.Add(version, 0)
        sizer.Add(cartelito, 0)
        sizer.Add(fecha, 0)
        panel.SetSizer(sizer)
        f.Show()
        return True
        
    def instrucciones(self,event):
        f = Frame(None, -1, 'Instrucciones', size =(800,720), pos = (300,5))
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        image = StaticBitmap(p, -1, Bitmap("C:\itec\prog1\EFI\instrucciones.jpg", BITMAP_TYPE_ANY))
        s.Add(image, 0, ALL|EXPAND, 20)
        p.SetSizer(s)
        f.Show()
        return True

app = MyApp()
app.MainLoop()




