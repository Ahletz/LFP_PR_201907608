#importar librerias 
from cmath import inf
from tkinter import *
from tkinter import filedialog
from io import open

#variable global con ruta archivos
archivo = ""

#Metodo para abrir un archivo 
def AbrirArchivo():
    global archivo
    archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/",filetypes=(("Archivos tipo data","*.data"),("Archivos tipo lfp","*.lfp")))
    
#Metodo abrir la vetana con boton        
def AbrirVentana():
    raiz =Tk()
    Button(raiz, text="Abrir Archivo",command=AbrirArchivo).pack()
    raiz.mainloop()

def LecturaData(): 
    print()

    

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
                

                print("Ruta del archivo\n")
                #ruta del archivo datos
                direcciondatos = archivo

                print(direcciondatos )
                #datos del documento
                infodata = open(direcciondatos)
                texto = infodata.read()
                #impresion informacion
                print(texto)
                print()

            elif (z==2):
                print("---------------------------carga intrucciones---------------------------")
                k = AbrirVentana()
                print("Ruta del archivo\n")
                #ruta archivo lfp
                direccionlfp = archivo

                print(direccionlfp)
                #datos del documento
                infolfp = open(direccionlfp)
                textointrucciones = infolfp.read()
                #impresion documentos
                print (textointrucciones)
                print()

            elif (z==3):
                print("analizar")
            elif (z==4):
                print("reporte")
            elif (z==5):
                print("Saliendo del programa---")
                salida = False

# llamado de los metodos y muestra de mensaes para el usuario 
Usuario = Sistema()
print("")
Usuario.Menu()

