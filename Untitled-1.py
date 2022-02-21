#importar librerias 
from tkinter import *
from tkinter import filedialog
from io import open
from matplotlib import pyplot #importa libreria para la creacion de graficas 
from flask import Flask, render_template #importar librerias flask para creacion de reporte html
import webbrowser #abrir navegador y html


#variable global 
archivo = ""
texto = ""
textointrucciones=""
palabra = ""
primer = ""
ultimo =""
pricant =0
ulticant=0
#intrucciones del documento 
Nombre =""
grafica=""
titulo=""
titulox=""
tituloy=""
#arreglos globales 
mesYanio = []
producto =[]
precio = []
cantidad = []
tot = []
primer5 = []
gan = []
cont = []
price = []


#pagina html
url = 'http://127.0.0.1:5000/'


#contador de productos y estados 
est =0
#eecutador de flask en el main 
ap = Flask(__name__)

#indicador de la ruta a ejecutar en el flask 
@ap.route('/')
def principal ():
    
    return render_template('repo.html',Nombres = primer5 , Precios= price,Cantidad = cont,Ventas = gan, p = primer, u = ultimo, uca = ulticant, pca = pricant )

#metodo para crear el reporte html
def Reporte():
    
    if __name__ == '__main__':
        ap.run()
    
#Metodo para abrir un archivo 
def AbrirArchivo():
    global archivo
    archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/",filetypes=(("Archivos tipo data","*.data"),("Archivos tipo lfp","*.lfp")))
    
#Metodo abrir la vetana con boton        
def AbrirVentana():
    raiz =Tk()
    Button(raiz, text="Abrir Archivo",command=AbrirArchivo).pack()
    raiz.mainloop()

def Numeros (): #cambiar valores a decimales y enteros 

    for i in range(len (precio)):

        precio [i]= float(precio[i])
        cantidad[i] = int(cantidad[i])

def Analisis(): #analisis de datos para ordenarlos 
    global tot #Lista con los totales de venta de cada producto 
    global primer5 #lista primeros 5 productos mas vendidos 
    global gan #lista ganancias primeros 5 productos
    global pricant #producto mas vendido
    global ulticant #producto menos vendido
    global primer #nombre producto mas vendido
    global ultimo #nombre producto menos vendido 
    global cont
    global price
    Numeros() #convertir numeros string a numeros 

    #auxiliares para el otdenamiento 
    aux1 = ""
    aux2 = 0
    aux3 = 0
    aux4 = 0

    for a in range (len(precio)):

        dato = float(precio[a]*cantidad[a]) #obtener el total de las ganacias por sus ventas y sus precios
        tot.append(dato) 
    
    #ordenamiento burbua para ordenar de mayor a menor 

    for j in range (len(producto)):
        for k in range(len(precio)-1):

            if tot[k] < tot[k+1]:
                 
                 #intercambio 
                 aux1 = producto[k]
                 aux2 = precio[k]
                 aux3 = cantidad[k]
                 aux4 = tot[k]

                 producto[k] = producto[k+1]
                 precio[k] = precio[k+1]
                 cantidad[k] = cantidad[k+1]
                 tot[k] = tot[k+1]

                 producto[k+1] = aux1
                 precio[k+1] = aux2
                 cantidad[k+1] = aux3
                 tot[k+1] = aux4

                 continue
            else: 
                continue
    for c in range(5):
        primer5.append(producto[c]) #agregar primeros  productos
        gan.append(tot[c])
        cont.append(cantidad[c])
        price.append(precio[c])
        
    
    primer = producto[0]
    ultimo = producto[len(producto)-1]
    pricant = cantidad[0]
    ulticant = cantidad[len(tot)-1]

    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C://Users//lopez//AppData//Local//Google//Chrome//Application//chrome.exe'))

    webbrowser.get('chrome').open(url)

    #llamamos la funcion para la pagina html con el reporte
    Reporte() 
    
               


#metodo para la creacion de graficas 
def Grafica():
    global grafica #uso de la variable global grafica 
    grafica = grafica.upper() #convertir texto en mayusculas 
    Numeros()

    if grafica == "BARRAS":

        pyplot.rcParams['toolbar'] = 'None' # Elimina la barra de herramientas de la imagen 

        pyplot.bar(producto, height=cantidad)
        pyplot.title(titulo)
        pyplot.ylabel(tituloy)
        pyplot.xlabel(titulox)
        pyplot.savefig(Nombre +".jpg")
        pyplot.show()
        
        
    elif grafica == "LINEAS":

        pyplot.rcParams['toolbar'] = 'None'

        pyplot.plot(producto,cantidad)
        pyplot.title(titulo)
        pyplot.ylabel(tituloy)
        pyplot.xlabel(titulox)
        pyplot.savefig(Nombre +".jpg")
        pyplot.show()
       

    elif grafica == "PIE":

        pyplot.rcParams['toolbar'] = 'None'

        pyplot.pie(cantidad, labels= producto)
        pyplot.axis('equal')
        pyplot.title(titulo)
        pyplot.savefig(Nombre +".jpg")
        pyplot.show()
        

        
    else: 
        print("No existe un tipo de grafica especificado")
   
#lectura del archivo .data e interpretacion de este
def LecturaData(): 
    global palabra #uso de la variable global para guardar texto 
    # uso global de arreglos 
    global mesYanio
    global producto 
    global precio
    global cantidad
    
    global est # estado 

    for i in range(len(texto)):#for para recorrer el texto 

        estado = texto[i] #leer la letra en la cual se encuentra el texto 

        if est == 0:
            
            if estado == ":":
                est = 1
                mesYanio.append(palabra)
                palabra = "" #limpieza de memoria palabra
                continue
            elif estado.isalpha(): #verificar si es una letra
                palabra += estado
                continue
            elif estado ==" " or estado =="\n" or estado =='\r' or estado =='\t':
                continue 
            else:
                continue
        if est == 1:

            if estado.isdigit():
                palabra+= estado
                continue
            elif estado == "=":
                continue
            elif estado == "(":
                est = 2
                mesYanio.append(palabra.upper())
                palabra =" " #limpieza de la palabra 
                continue
            elif estado ==" " or estado =="\n" or estado =='\r' or estado =='\t':
                continue
            else:
                continue
            
        if est == 2:
            if estado == "[":
                continue
            elif estado =='"':
                est = 3
                continue
            elif estado ==")":
                print ("Analisis del Texto Finalizado!!!\n")

            elif estado ==" " or estado =="\n" or estado =='\r' or estado =='\t':
                continue
            else:
                continue
             
        if est == 3: #para ver el nombre del producto 
            if estado == '"':
                continue
            elif estado == ',':
                producto.append(palabra.lstrip()) #agregar ombre del producto 
                palabra =""
                est = 4
                continue
            elif estado.isalnum() or estado ==" ":
                palabra += estado
                continue
            elif estado ==" " or estado =="\n" or estado =='\r' or estado =='\t':
                continue
            else:
                continue

        if est ==4: #para ver el precio del producto 
            
            if estado ==',':

                if palabra == '' or palabra == ' ' or palabra == '  ' or palabra == '   ':
                    precio.append("0")#agrega precio del producto si este no tiene existencia
                    est = 5
                    palabra = ""
                else: 
                    precio.append(palabra) #agregar precio del producto 
                    palabra =""
                    est = 5
            
                continue
            elif estado.isalnum() or estado ==" " or estado==".":
                palabra+=estado
                continue
            elif estado ==" " or estado =="\n" or estado =='\r' or estado =='\t':
                continue
            else:
                continue
            
        if est == 5: #para ver la cantidad del producto

            if estado.isalpha() or estado.isalnum():
                palabra+=estado
                continue
            elif estado ==']':
                continue
            elif estado == ';':
                if palabra == '' or palabra == ' ' or palabra == '  ' or palabra == '   ':
                    cantidad.append("0")#agrega cantidad del producto si este no tiene existencia
                    est = 2
                    palabra = ""
                else: 
                    cantidad.append(palabra)#agrega cantidad del producto 
                    est = 2
                    palabra = ""
                continue

            elif estado ==" " or estado =="\n" or estado =='\r' or estado =='\t':
                continue
            else:
                continue
    '''
    print("REPORTE: " + mesYanio[0] + " / " + mesYanio[1]) #impresion de el mes y el año de la fecha 
    for j in range (len (producto)): # ciclo para imprimir los datos de producto, precio y cantidad
        print(producto[j] + ": " + precio[j] +" / " + cantidad[j]) '''

def Lecturalfp():

    palabra ="" #variable contenedora del signo,letra o digito
    #uso de  intrucciones 
    global Nombre
    global grafica
    global titulo
    global titulox
    global tituloy

    estado = 0 #variable local de estado 
    text = ""

    for i in range(len(textointrucciones)):

        palabra = textointrucciones[i] #Letra, digito o signo en posicion 

        if estado == 0: 

            if palabra == "<":
                continue
            elif palabra == "¿":
                continue
            elif palabra == "Â":
                continue
            elif palabra.isalpha():
                text += palabra
                continue
            elif palabra == " " or palabra == "\n" or palabra == "\r" or palabra == "\t":
                continue
            elif palabra ==":":
                text = text.upper()
                if text == "NOMBRE":
                    estado = 1
                    text = ""
                    continue
                elif text == "GRAFICA":
                    estado = 2
                    text = ""
                    continue
                elif text == "TITULO":
                    estado = 3
                    text = ""
                    continue
                elif text == "TITULOX":
                    estado = 4
                    text = ""
                    continue
                elif text == "TITULOY":
                    estado = 5
                    text = ""
                    continue
                else: 
                    continue
            else:
                continue
        if estado == 1:

            if palabra =='"':
                continue
            elif palabra ==",":
                estado = 0
                Nombre= text
                text = ""
                continue
            elif palabra.isalnum():
                text+=palabra
                continue
            elif palabra == " " or palabra == "\n" or palabra == "\r" or palabra == "\t":
                continue
            else:
                continue
        if estado == 2:

            if palabra =='"':
                continue
            elif palabra ==",":
                estado = 0
                grafica= text
                text = ""
                continue
            elif palabra.isalpha():
                text+=palabra
                continue
            elif palabra == " " or palabra == "\n" or palabra == "\r" or palabra == "\t":
                continue
            else:
                continue
        if estado == 3:

            if palabra =='"':
                continue
            elif palabra ==",":
                estado = 0
                titulo= text
                text = ""
                continue
            elif palabra.isalpha():
                text+=palabra
                continue
            elif palabra == " " or palabra == "\n" or palabra == "\r" or palabra == "\t":
                continue
            else:
                continue
        if estado == 4:

            if palabra =='"':
                continue
            elif palabra ==",":
                estado = 0
                titulox= text
                text = ""
                continue
            elif palabra.isalpha():
                text+=palabra
                continue
            elif palabra == " " or palabra == "\n" or palabra == "\r" or palabra == "\t":
                continue
            else:
                continue
        if estado == 5:

            if palabra =='"':
                continue
            elif palabra =="," or palabra ==">" or palabra =="?":
                estado = 0
                tituloy= text
                text = ""
                continue
            elif palabra.isalpha():
                text+=palabra
                continue
            elif palabra == " " or palabra == "\n" or palabra == "\r" or palabra == "\t":
                continue
            else:
                continue
        else: 
            continue
    
    

class Sistema: 
    # Metodo de mensaje al incio del programa
    def __init__(self) :
        print ("-------------------------------Bienvenido-------------------------------")
    
    #Metodo para el menu de opciones de la aplicacion 
    def Menu(self): 
        
        z = 0
        salida = True
        while salida == True: #ciclo para mostrar menu hasta terinar el programa
        
            print("\nSeleccione una de las siguientes funciones: ")
            print ("||1. Carga Datos.        ||")
            print ("||2. Carga Intrucciones. ||")
            print ("||3. Analizar.           ||")
            print ("||4. Reportes.           ||")
            print ("||5. Salir.              ||")
            z = int (input())
            if (z==1):
                print ("---------------------------carga de archivo---------------------------\n")
                k = AbrirVentana()  
                

                #print("Ruta del archivo\n")
                #ruta del archivo datos
                direcciondatos = archivo

                print(direcciondatos )
                #datos del documento
                infodata = open(direcciondatos)
                global texto #variable global para utilizar texto 
                texto = infodata.read()
                #impresion informacion
               # print(texto)
                print()

            elif (z==2):
                print("---------------------------carga intrucciones---------------------------")
                k = AbrirVentana()
                #print("Ruta del archivo\n")
                #ruta archivo lfp
                direccionlfp = archivo

                print(direccionlfp)
                #datos del documento
                infolfp = open(direccionlfp)
                global textointrucciones #variable global para utilizar texto 
                textointrucciones = infolfp.read()
                #impresion documentos
               # print (textointrucciones)
                print()

            elif (z==3):

                LecturaData()#lectura del archivo .data
                
                Lecturalfp() #maneoj del archivo .lfp

                Grafica() #llamado de grafica 

            elif (z==4):

                LecturaData()#lectura del archivo .data
                
                Lecturalfp() #maneoj del archivo .lfp

                Analisis()

               
            elif (z==5):
                print("Saliendo del programa---")
                salida = False

# llamado de los metodos y muestra de mensaes para el usuario 
Usuario = Sistema()
print("")
Usuario.Menu()
#Reporte()




