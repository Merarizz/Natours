import tkinter as tk
from tkinter import ttk
import sql
from PIL import Image, ImageTk
import empleados
import clientes
import servicios
import facturas
import prospectos
import estadisticas

class Principal:
    def __init__(self, nivel, nombre):
        self.__nombre=nombre
        self.__nivel=nivel
        self.__ancho=1210
        self.__alto=750

        #ventana
        self.__ventana=tk.Tk()
        self.__ventana.config(width=self.__ancho, height=self.__alto)
        self.__ventana.config(bg="#D3D3D3")
        title = "Sistema de clientes - Bienvenido " + self.__nombre
        self.__ventana.title(title)
        self.__ventana.resizable (False, False)
        self.__mainframe=tk.Frame(self.__ventana, width=self.__ancho, height=self.__alto, background="#A9A9A9")
        self.__mainframe.place(x=0, y=0)

        #objetos del sistema
        self.__objempleados = empleados.Empleado(self.__mainframe, nivel)
        self.__objclientes = clientes.Cliente(self.__mainframe, nivel)
        self.__objservicios = servicios.Servicio(self.__mainframe, nivel)
        self.__objfacturas = facturas.Factura(self.__mainframe, nivel)
        self.__objprospectos = prospectos.Prospecto(self.__mainframe, nivel)
        self.__objestadisticas = estadisticas.Estadisticas(self.__mainframe, nivel)



    def ventana(self):


        #parte blanca atras de los iconos
        canvas = tk.Canvas(width=self.__ancho, height=100, bg="#FFF")
        canvas.place(x=0, y=0)
        # linea separación
        canvaslinea = tk.Canvas(width=self.__ancho, height=2, bg="#000000")
        canvaslinea.place(x=120, y=100)



        #logo
        logon = Image.open("./img/logonatours.png")
        logon = logon.resize((100,100))
        logon = ImageTk.PhotoImage(logon)
        lblimagen = tk.Label(image=logon, width=100, height=100)
        lblimagen.place(x=10, y=10)

        #botones

        #boton empleados
        empleados=Image.open("./img/empleados.png")
        empleados=empleados.resize((50,50))
        empleados=ImageTk.PhotoImage(empleados)
        btnempleados= tk.Button(self.__ventana, image=empleados , text="Empleados", width=120, height=80,  font=("Sora", 10), command=self.__objempleados.botonestodos)
        btnempleados.place(x=121, y=10)

        #boton clientes
        clientes=Image.open("./img/clientes.png")
        clientes=clientes.resize((50,50))
        clientes=ImageTk.PhotoImage(clientes)
        btnclientes= tk.Button(self.__ventana, image=clientes , text="Clientes", width=120, height=80,  font=("Sora", 10), command=self.__objclientes.botonestodos)
        btnclientes.place(x=281, y=10)

        #botonprospectos
        prospectos=Image.open("./img/prospectos.png")
        prospectos=prospectos.resize((50,50))
        prospectos=ImageTk.PhotoImage(prospectos)
        btnprospectos=tk.Button(self.__ventana, image=prospectos , text="Prospectos", width=120, height=80,  font=("Sora", 10), command=self.__objprospectos.botonestodos)
        btnprospectos.place(x=440, y=10)

        #boton servicios
        servicios=Image.open("./img/servicios.png")
        servicios=servicios.resize((50,50))
        servicios=ImageTk.PhotoImage(servicios)
        btnservicios =tk.Button(self.__ventana, image=servicios , text="Servicios", width=120, height=80, font=("Sora", 10), command=self.__objservicios.botonestodos)
        btnservicios.place(x=600, y=10)

        #boton facturas
        facturas=Image.open("./img/facturas.png")
        facturas=facturas.resize((50,50))
        facturas=ImageTk.PhotoImage(facturas)
        btnfacturas = tk.Button(self.__ventana, image=facturas , text="Facturas", width=120, height=80, font=("Sora", 10), command=self.__objfacturas.botonestodos)
        btnfacturas.place(x=760, y=10)

        #boton estadisticas
        estadisticas=Image.open("./img/estadisticas.png")
        estadisticas=estadisticas.resize((50,50))
        estadisticas=ImageTk.PhotoImage(estadisticas)
        btnestadisticas = tk.Button(self.__ventana, image=estadisticas, text="Estadisticas", width=120, height=80, font=("Sora", 10), command=self.__objestadisticas.botonestodos)
        btnestadisticas.place(x=920, y=10)

        #boton salir
        salir=Image.open("./img/salir.png")
        salir=salir.resize((50,50))
        salir=ImageTk.PhotoImage(salir)
        btnsalir = tk.Button(self.__ventana, image=salir , text="Salir", width=120, height=80, font=("Sora", 10), command=self.__close)
        btnsalir.place(x=1080, y=10)

        self.__ventana.mainloop()

    def negado(self):

        # negado img
        logon = Image.open("./img/negado.png")
        logon = logon.resize((500, 500))
        logon = ImageTk.PhotoImage(logon)
        lblimagen = tk.Label(image=logon, width=500, height=500)
        lblimagen.place(x=150, y=120)


    def __close(self):
        self.__ventana.destroy()

#a=Principal(1,"Merari")
#a.ventana()

