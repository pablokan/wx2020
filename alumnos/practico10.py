#Tenemos un archivo deudores.txt con información de personas que adeudan dinero.
#Necesitamos saber el nombre, la dirección de correo y el saldo de todos los que deben más de doscientos mil pesos y cuya deuda sea del año pasado.
#Hacer:
#Recorrer el archivo deudores.txt y grabar uno nuevo llamado morosos.txt con los datos requeridos. 
#Para los saldos, el nuevo archivo NO tiene que tener el signo pesos ($) ni los centavos.
#El nuevo archivo tiene que tener cabecera en la primera línea con los nombres de los datos, similar al archivo deudores.txt.
#Notas:
#Se debe usar una clase principal que al ser instanciada muestre el menú de opciones.
#Elegir libremente los métodos de lectura y escritura de archivos que prefieran.
#El formato del nuevo archivo debe ser legible, no hay un formato obligatorio.


class App():

    def __init__(self):
        op= ""
        while op != "3":
            print ("\nMenu de Opciones")
            print ("1- Ver lista de deudores")
            print ("2- Hacer una lista de morosos")
            print ("3- Salir")
            op= input( "Opcion: ")

            if op == "1":
                self. Deudores()
            elif op == "2":
                self.Morosos()
                self.MostrarMorosos()
        print ("Bye")

    
    def Deudores(self): #Podria hacer un método que sea para mostrar cualquier archivo.
        a= open ("alumnos/deudores.txt", "r", encoding="utf8")
        self.todo= a.readlines()
        print (len(self.todo), "Deudores:")
        for li in self.todo:
            li= li[:-1]
            print (li)
        a.close()
    
  
    
    def Morosos(self):
        archivo = open("alumnos/deudores.txt","r", encoding="utf8")
        morosos= open("alumnos/morosos.txt", "w")
        encabezado= "Nombre, Mail, Saldo"
        morosos.write(encabezado + "\n")
        c= 0
        todo= archivo.readlines()
        for li in todo:
            if "/2019" in li:
                lis= li.split(",")
                saldo= int(lis[4][1:-3])
                if saldo > 200000:
                    c +=1
                    morosos.write (str(c) + "- " + lis[1] + " - " + lis[2] + " - " + str(saldo) + "\n")
        archivo.close()
        morosos.close()
    
    def MostrarMorosos(self):
        a = open ("alumnos/morosos.txt","r",encoding="utf8" )
        self.todo= a.readlines()
        print (len(self.todo), "Morosos con deudas anteriores al 2020:")
        for li in self.todo:
            li= li[:-1]
            print (li)
        a.close()

a= App()

  







