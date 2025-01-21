import tkinter as tk
from tkinter import ttk, NO

import numpy as np

import sql
from PIL import Image, ImageTk
from tkinter import messagebox
import re
import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Estadisticas:

    def __init__(self, ventana, nivel):
        self.__sql = sql.SQL()
        self.__ancho = 1072
        self.__alto = 630
        self.__ventana = ventana
        self.__nivel=nivel
        self.__framempleados= None
        self.__frameclientes= None
        self.__frameprospectos= None
        self.__frameservicios= None
        self.__framebotones= None
        self.__framefacturas = None
        self.__frameventas = None
        self.__lblimagennegado= None

    def actualizabotones(self, subseccion):
        self.__btnempleados.config(bg="#565656", fg="#FFFFFF")
        self.__btnclientes.config(bg="#565656", fg="#FFFFFF")
        self.__btnprospectos.config(bg="#565656", fg="#FFFFFF")
        self.__btnservicios.config(bg="#565656", fg="#FFFFFF")
        self.__btnfacturas.config(bg="#565656", fg="#FFFFFF")
        self.__btnventas.config(bg="#565656", fg="#FFFFFF")
        self.__btnfiltrar.config(bg="#565656", fg="#FFFFFF")

        if subseccion== "empleados":
            self.__btnempleados.config(bg="#DAA520", fg="#000000")
        elif subseccion== "clientes":
            self.__btnclientes.config(bg="#DAA520", fg="#000000")
        elif subseccion== "prospectos":
            self.__btnprospectos.config(bg="#DAA520", fg="#000000")
        elif subseccion == "servicios":
            self.__btnservicios.config(bg="#DAA520", fg="#000000")
        elif subseccion== "facturas":
            self.__btnfacturas.config(bg="#DAA520", fg="#000000")
        elif subseccion == "ventas":
            self.__btnventas.config(bg="#DAA520", fg="#000000")
        elif subseccion == "filtrar":
            self.__btnfiltrar.config(bg="#DAA520", fg="#000000")


    def empleados(self):

        #self.actualizabotones("filtrar")

        # formulario
        self.__framempleados = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framempleados, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        lblfiltro2 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de grafica: ", font=("Sora", 10))
        lblfiltro2.place(x=10, y=40)

        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", values=["Puesto", "Estatus", "Sueldo", "Comision"])
        self.__cmbfiltro1.place(x=120, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Barra", "Pie", "Linea"])
        self.__cmbfiltro2.place(x=120, y=40)

        self.__btnfiltrar = tk.Button(self.__generallblFrm, text="Generar gráfica", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.graficar("empleados",self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        self.__btnfiltrar.place(x=320, y=40)

        # lbldescriptores = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descriptores estadísticos: ", font=("Sora", 12))
        # lbldescriptores.place(x=800,y=1)
        #
        # lblmedia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Media: ", font=("Sora", 10))
        # lblmedia.place(x=800, y=27)
        #
        # lbldesviacion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Desviación: ", font=("Sora", 10))
        # lbldesviacion.place(x=800, y=50)

        self.__framedatos = tk.LabelFrame(self.__framempleados, text="Gráfica", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=120)

        self.actualizabotones("empleados")

        # lo blanco
        self.__framempleados.place(x=130, y=110)

    def clientes(self):


        # formulario
        self.__frameclientes = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__frameclientes, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        lblfiltro2 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de grafica: ", font=("Sora", 10))
        lblfiltro2.place(x=10, y=40)

        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", values=["Pais", "Ventas"])
        self.__cmbfiltro1.place(x=120, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Barra", "Pie", "Linea"])
        self.__cmbfiltro2.place(x=120, y=40)

        self.__btnfiltrar = tk.Button(self.__generallblFrm, text="Generar gráfica", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.graficar("clientes",self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        self.__btnfiltrar.place(x=320, y=40)

        # lbldescriptores = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descriptores estadísticos: ", font=("Sora", 12))
        # lbldescriptores.place(x=800,y=1)
        #
        # lblmedia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Media: ", font=("Sora", 10))
        # lblmedia.place(x=800, y=27)
        #
        # lbldesviacion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Desviación: ", font=("Sora", 10))
        # lbldesviacion.place(x=800, y=50)

        self.__framedatos = tk.LabelFrame(self.__frameclientes, text="Gráfica", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=120)

        self.actualizabotones("clientes")

        # lo blanco
        self.__frameclientes.place(x=130, y=110)


    def prospectos(self):


        # formulario
        self.__frameprospectos = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__frameprospectos, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        lblfiltro2 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de grafica: ", font=("Sora", 10))
        lblfiltro2.place(x=10, y=40)

        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", values=["Pais"])
        self.__cmbfiltro1.place(x=120, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Barra", "Pie", "Linea"])
        self.__cmbfiltro2.place(x=120, y=40)

        self.__btnfiltrar = tk.Button(self.__generallblFrm, text="Generar gráfica", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.graficar("prospectos",self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        self.__btnfiltrar.place(x=320, y=40)

        # lbldescriptores = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descriptores estadísticos: ", font=("Sora", 12))
        # lbldescriptores.place(x=800,y=1)
        #
        # lblmedia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Media: ", font=("Sora", 10))
        # lblmedia.place(x=800, y=27)
        #
        # lbldesviacion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Desviación: ", font=("Sora", 10))
        # lbldesviacion.place(x=800, y=50)

        self.__framedatos = tk.LabelFrame(self.__frameprospectos, text="Gráfica", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=120)

        self.actualizabotones("prospectos")

        # lo blanco
        self.__frameprospectos.place(x=130, y=110)

    def servicios(self):


        # formulario
        self.__frameservicios = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__frameservicios, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        lblfiltro2 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de grafica: ", font=("Sora", 10))
        lblfiltro2.place(x=10, y=40)

        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", values=["Tipo de Servicio", "Sub-Tipo de Servicio", "Pais", "Costo", "Comision"])
        self.__cmbfiltro1.place(x=120, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Barra", "Pie", "Linea"])
        self.__cmbfiltro2.place(x=120, y=40)

        self.__btnfiltrar = tk.Button(self.__generallblFrm, text="Generar gráfica", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.graficar("servicios",self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        self.__btnfiltrar.place(x=320, y=40)

        # lbldescriptores = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descriptores estadísticos: ", font=("Sora", 12))
        # lbldescriptores.place(x=800,y=1)
        #
        # lblmedia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Media: ", font=("Sora", 10))
        # lblmedia.place(x=800, y=27)
        #
        # lbldesviacion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Desviación: ", font=("Sora", 10))
        # lbldesviacion.place(x=800, y=50)

        self.__framedatos = tk.LabelFrame(self.__frameservicios, text="Gráfica", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=120)

        self.actualizabotones("servicios")

        # lo blanco
        self.__frameservicios.place(x=130, y=110)

    def facturas(self):


        # formulario
        self.__framefacturas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framefacturas, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        lblfiltro2 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de grafica: ", font=("Sora", 10))
        lblfiltro2.place(x=10, y=40)

        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", values=["Status", "Empleado", "Cliente", "Total"])
        self.__cmbfiltro1.place(x=120, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Barra", "Pie", "Linea"])
        self.__cmbfiltro2.place(x=120, y=40)

        self.__btnfiltrar = tk.Button(self.__generallblFrm, text="Generar gráfica", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.graficar("facturas",self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        self.__btnfiltrar.place(x=320, y=40)

        # lbldescriptores = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descriptores estadísticos: ", font=("Sora", 12))
        # lbldescriptores.place(x=800,y=1)
        #
        # lblmedia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Media: ", font=("Sora", 10))
        # lblmedia.place(x=800, y=27)
        #
        # lbldesviacion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Desviación: ", font=("Sora", 10))
        # lbldesviacion.place(x=800, y=50)

        self.__framedatos = tk.LabelFrame(self.__framefacturas, text="Gráfica", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=120)

        self.actualizabotones("facturas")

        # lo blanco
        self.__framefacturas.place(x=130, y=110)

    def ventas(self):


        # formulario
        self.__frameventas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__frameventas, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        lblfiltro2 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de grafica: ", font=("Sora", 10))
        lblfiltro2.place(x=10, y=40)

        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", values=["Total", "Servicios", "Año corriente","Años"])
        self.__cmbfiltro1.place(x=120, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Barra", "Pie", "Linea"])
        self.__cmbfiltro2.place(x=120, y=40)

        self.__btnfiltrar = tk.Button(self.__generallblFrm, text="Generar gráfica", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.graficar("ventas",self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        self.__btnfiltrar.place(x=320, y=40)

        # lbldescriptores = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descriptores estadísticos: ", font=("Sora", 12))
        # lbldescriptores.place(x=800,y=1)
        #
        # lblmedia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Media: ", font=("Sora", 10))
        # lblmedia.place(x=800, y=27)
        #
        # lbldesviacion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Desviación: ", font=("Sora", 10))
        # lbldesviacion.place(x=800, y=50)

        self.__framedatos = tk.LabelFrame(self.__frameventas, text="Gráfica", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=120)

        self.actualizabotones("ventas")

        # lo blanco
        self.__frameventas.place(x=130, y=110)

    def graficar(self, seccion,filtro1, filtro2):
        self.actualizabotones("filtrar")

        if(filtro1 == "" or filtro2 == ""):
            messagebox.showerror(message="No se ha seleccionado un filtro", title="Campos vacios")
        else:
            #Nos traemos los datos para cada seccion
            if (seccion == "empleados"):
                x,y,titulo = self.graficaEmpleados(filtro1)
            elif (seccion == "clientes"):
                x,y,titulo = self.graficaClientes(filtro1)
            elif (seccion == "prospectos"):
                x,y,titulo = self.graficaProspectos(filtro1)
            elif (seccion == "servicios"):
                x,y,titulo = self.graficaServicios(filtro1)
            elif (seccion == "facturas"):
                x,y,titulo = self.graficaFacturas(filtro1)
            else: #Ventas
                x,y,titulo = self.graficaVentas(filtro1)

            #graficamos segun tipo de grafica
            if (filtro2 == "Pie"):
                self.graficaPie(x, y, titulo)
            elif (filtro2 == "Barra"):
                self.graficaBar(x, y, titulo)
            elif (filtro2 == "Linea"):
                self.graficaLinea(x, y, titulo)

    def graficaEmpleados(self,filtro1):
        x = []
        y = []
        titulo = ""
        if filtro1 == "Puesto":
            titulo = "Cantidad de empleados por puesto"
            query = "select count(puesto),puesto from empleados group by puesto;"
        elif filtro1 == "Estatus":
            titulo = "Cantidad de empleados por estatus"
            query = "select count(estatus), estatus from empleados group by estatus;"
        elif filtro1 == "Sueldo":
            titulo = "Distribucion de empleados por rangos de sueldo"
            query = "select count(id_empleado), case when sueldo < 4999 then '0 - 4,999' when sueldo between 5000 and 9999 then '5,000 - 9,999' when sueldo between 10000 and 49999 then '10,000 - 49,000' when sueldo between 10000 and 49999 then '10,000 - 49,000' when sueldo > 50000 then '50,000 - max' end as rango from empleados group by rango;"
        elif filtro1 == "Comision":
            titulo = "Distribucion de empleados por rangos de comision"
            query = "select count(id_empleado), case when comision <= 4.99 then '0 - 4.99' when comision between 5 and 9.99 then '5 - 9.99' when comision between 10 and 14.99 then '10 - 14.99' when comision between 15 and 19.99 then '15 - 19.99' when comision >= 20 then '20 - max' end as rango from empleados group by rango;"
        else: # fecha???
            titulo = ""


        data = self.__sql.custQuery(query)
        if data != None:
            for fila in data:
                x.append(fila[0])
                y.append(fila[1])
        return x, y, titulo

    def graficaClientes(self,filtro1):
        x = []
        y = []
        titulo = ""
        if filtro1 == "Pais":
            titulo = "Distribucion de clientes por paises de origen"
            query = "select count(pais), pais from (select paises.nombre as pais from clientes left join direcciones on direcciones.id_direccion=clientes.id_direccion left join cp on cp.id_cp=direcciones.id_cp left join paises on paises.id_pais=cp.id_pais) as temp group by pais; "
        else: #ventas
            titulo = "Distribucion de clientes por total de ventas historico"
            query = "select sum(facturas.total), (select concat(nombre,' ', ap_pat,' ', ap_mat) from clientes where facturas.id_cliente=clientes.id_cliente) as cliente from facturas where facturas.status='Activa' group by cliente;"

        data = self.__sql.custQuery(query)
        if data != None:
            for fila in data:
                x.append(fila[0])
                y.append(fila[1])
        return x, y, titulo

    def graficaProspectos(self, filtro1):
        x = []
        y = []
        titulo = "Distribucion de prospectos por pais de origen"
        query = "select count(pais), pais from (select paises.nombre as pais from prospectos left join direcciones on direcciones.id_direccion=prospectos.id_direccion left join cp on cp.id_cp=direcciones.id_cp left join paises on paises.id_pais=cp.id_pais) as temp group by pais;"
        data = self.__sql.custQuery(query)
        if data != None:
            for fila in data:
                x.append(fila[0])
                y.append(fila[1])
        return x, y, titulo

    def graficaServicios(self, filtro1):
        x = []
        y = []
        titulo = ""
        if filtro1 == "Tipo de Servicio":
            titulo = "Distribucion de servicios por tipo de servicio"
            query = "select count(tipo_servicio), tipo_servicio from servicios group by tipo_servicio"
        elif filtro1 == "Sub-Tipo de Servicio":
            titulo = "Distribucion de servicios por sub-tipo de servicio"
            query = "select count(subtipo), subtipo from servicios group by subtipo"
        elif filtro1 == "Pais":
            titulo = "Distribucion de servicios por pais"
            query = "select count(pais), pais from servicios group by pais"
        elif filtro1 == "Costo":
            titulo = "Distribucion de servicios por rangos de costo"
            query = "select count(id_servicio), case when costo < 4999 then '0 - 4,999' when costo between 5000 and 9999 then '5,000 - 9,999' when costo between 10000 and 49999 then '10,000 - 49,000' when costo between 10000 and 49999 then '10,000 - 49,000' when costo > 50000 then '50,000 - max' end as rango from servicios group by rango;"
        elif filtro1 == "Comision":
            titulo = "Distribucion de empleados por rangos de comision"
            query = "select count(id_servicio), case when comision <= 4.99 then '0 - 4.99' when comision between 5 and 9.99 then '5 - 9.99' when comision between 10 and 14.99 then '10 - 14.99' when comision between 15 and 19.99 then '15 - 19.99' when comision >= 20 then '20 - max' end as rango from servicios group by rango;"
        else: #fecha??
            titulo = ""
            query = ""

        data = self.__sql.custQuery(query)
        if data != None:
            for fila in data:
                x.append(fila[0])
                y.append(fila[1])
        return x, y, titulo

    def graficaFacturas(self, filtro1):
        x = []
        y = []
        titulo = ""
        if filtro1 == "Status":
            titulo = "Distribucion de facturas por status (activas-canceladas)"
            query = "select count(status), status from facturas group by status"
        elif filtro1 == "Empleado":
            titulo = "Cantidad de facturas emitidas y activas por empleado"
            query = "select count(facturas.id_empleado), (select concat( ap_pat) from empleados where facturas.id_empleado=empleados.id_empleado) as empleado from facturas where facturas.status='Activa' group by empleado; "
        elif filtro1 == "Cliente":
            titulo = "Cantidad de facturas activas por cliente"
            query = "select count(facturas.id_cliente), (select concat( ap_pat) from clientes where facturas.id_cliente=clientes.id_cliente) as cliente from facturas where facturas.status='Activa' group by cliente; "
        elif filtro1 == "Total":
            titulo = "Cantidad de facturas por rango de totales"
            query = "select count(id_factura), case when total < 9999 then '0 - 9,999' when total between 10000 and 49999 then '10,000 - 49,999' when total between 50000 and 99999 then '50,000 - 99,999' when total > 100000 then '100,000 - max' end as rango from facturas where facturas.status='Activa' group by rango;"
        else: #fecha??
            titulo = ""
            query = "select "

        data = self.__sql.custQuery(query)
        if data != None:
            for fila in data:
                x.append(fila[0])
                y.append(fila[1])
        return x, y, titulo

    def graficaVentas(self, filtro1):
        x = []
        y = []
        titulo = ""
        fecha = datetime.date.today()
        anio = fecha.year
        if filtro1 == "Total":
            titulo = "Cantidad de ventas totales por rangos"
            query = "select count(id_factura), case when total < 9999 then '0 - 9,999' when total between 10000 and 49999 then '10,000 - 49,999' when total between 50000 and 99999 then '50,000 - 99,999' when total > 100000 then '100,000 - max' end as rango from facturas where facturas.status='Activa' group by rango;"
        elif filtro1 == "Servicios":
            titulo = "Cantidad de servicios vendidos"
            query = "select count(ventas.id_servicio), servicios.tipo_servicio from ventas, servicios where ventas.id_servicio=servicios.id_servicio group by servicios.tipo_servicio;"
        elif filtro1 == "Año corriente":
            titulo = "Cantidad de ventas por mes en el año corriente"
            query = "select sum(total), month(fecha) from facturas where year(fecha)=" + str(anio) + " group by month(fecha);"
        else: #fecha??
            titulo = "Cantidad de ventas por año"
            query = "select sum(total), year(fecha) from facturas group by year(fecha);"

        data = self.__sql.custQuery(query)
        if data != None:
            for fila in data:
                x.append(fila[0])
                if(filtro1 == "Año corriente"):
                    y.append(self.nombremes(fila[1]))
                elif filtro1=="Años":
                    y.append(str(fila[1]))
                else:
                    y.append(fila[1])
        return x, y, titulo

    def nombremes(self, num):
        if (num == 1):
            return "Enero"
        elif (num == 2):
            return "Febrero"
        elif (num == 3):
            return "Marzo"
        elif (num == 4):
            return "Abril"
        elif (num == 5):
            return "Mayo"
        elif (num == 6):
            return "Junio"
        elif (num == 7):
            return "Julio"
        elif (num == 8):
            return "Agosto"
        elif (num == 9):
            return "Septiembre"
        elif (num == 10):
            return "Octubre"
        elif (num == 11):
            return "Noviembre"
        elif (num == 12):
            return "Diciembre"
        else:
            return "XXX"


    def graficaPie(self, x, y, titulo):
        if (len(x) == 0 or len(y) == 0):
            messagebox.showinfo(message="No se encontraron registros", title="Sin registros")
        else:
            frame= tk.Frame(self.__framedatos)
            frame.place(x=10,y=0)
            fig = Figure(figsize=(10,4),dpi=100)
            grafica = fig.add_subplot(111)
            grafica.pie(x, labels=y, startangle = 90, shadow = True, autopct ='%1.1f%%')
            grafica.set_title(titulo)
            canvas = FigureCanvasTkAgg(fig,frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=0,y=0)
            toolbar = NavigationToolbar2Tk(canvas, frame)
            toolbar.update()
            canvas.get_tk_widget().pack()

    def graficaLinea(self, x, y, titulo):
        if (len(x) == 0 or len(y) == 0):
            messagebox.showinfo(message="No se encontraron registros", title="Sin registros")
        else:
            frame = tk.Frame(self.__framedatos)
            frame.place(x=10, y=0)
            fig = Figure(figsize=(10, 4), dpi=100)
            grafica = fig.add_subplot(111)
            grafica.plot(y, x, "-o")
            grafica.set_title(titulo)

            #grafica.axis([0,max(y),0,len(x)])
            canvas = FigureCanvasTkAgg(fig, frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=0, y=0)
            toolbar = NavigationToolbar2Tk(canvas, frame)
            toolbar.update()
            canvas.get_tk_widget().pack()

    def graficaBar(self, x, y, titulo):
        if (len(x) == 0 or len(y) == 0):
            messagebox.showinfo(message="No se encontraron registros", title="Sin registros")
        else:
            frame = tk.Frame(self.__framedatos)
            frame.place(x=10, y=0)
            fig = Figure(figsize=(10, 4), dpi=100)
            grafica = fig.add_subplot(111)
            grafica.bar(y, x)
            grafica.set_title(titulo)
            canvas = FigureCanvasTkAgg(fig, frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=0, y=0)
            toolbar = NavigationToolbar2Tk(canvas, frame)
            toolbar.update()
            canvas.get_tk_widget().pack()



    def botonestodos(self):
        for elemento in self.__ventana.winfo_children():
            elemento.destroy()
        # parte blanca atras de los iconos izq
        canvas = tk.Canvas(self.__ventana, width=120, height=self.__alto, bg="#FFF")
        canvas.place(x=0, y=100)
        # linea separación izq
        canvaslinea = tk.Canvas(self.__ventana, width=2, height=self.__alto+20, bg="#000000")
        canvaslinea.place(x=120, y=100)

        self.__framebotones = tk.Frame(self.__ventana, bg="#FFFFFF", width=120, height=self.__alto)

        # logo
        self.__logon = Image.open("./img/estadisticas.png")
        self.__logon = self.__logon.resize((100, 100))
        self.__logon = ImageTk.PhotoImage(self.__logon)
        self.__lblimagen = tk.Label(self.__framebotones, image=self.__logon, width=100, height=100)
        self.__lblimagen.place(x=10, y=0)

        self.__btnempleados = tk.Button(self.__framebotones, bg="#565656", text="Empleados", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.empleados))
        self.__btnempleados.place(x=10, y=130)

        self.__btnclientes = tk.Button(self.__framebotones, bg="#565656", text="Clientes", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.clientes))
        self.__btnclientes.place(x=10, y=158)

        self.__btnprospectos = tk.Button(self.__framebotones, bg="#565656", text="Prospectos", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.prospectos))
        self.__btnprospectos.place(x=10, y=186)

        self.__btnservicios = tk.Button(self.__framebotones, bg="#565656", text="Servicios", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.servicios))
        self.__btnservicios.place(x=10, y=214)

        self.__btnfacturas = tk.Button(self.__framebotones, bg="#565656", text="Facturas", width=12, height=1,font=("Sora", 10), fg="#D3D3D3", command=lambda: self.operacion(self.facturas))
        self.__btnfacturas.place(x=10, y=242)

        self.__btnventas = tk.Button(self.__framebotones, bg="#565656", text="Ventas", width=12, height=1, font=("Sora", 10), fg="#D3D3D3", command=lambda: self.operacion(self.ventas))
        self.__btnventas.place(x=10, y=270)

        self.__framebotones.place(x=0, y=120)



    def clearall(self):
        if self.__lblimagennegado!=None:
            self.__lblimagennegado.destroy()
            self.__lblimagennegado=None

        if(self.__framempleados != None):
            self.__framempleados.destroy()
        if (self.__frameclientes != None):
            self.__frameclientes.destroy()
        if (self.__frameprospectos != None):
            self.__frameprospectos.destroy()
        if (self.__frameservicios != None):
            self.__frameservicios.destroy()
        if (self.__framefacturas != None):
            self.__framefacturas.destroy()
        if (self.__frameventas != None):
            self.__frameventas.destroy()

    def negado(self):
        # negado img
        self.__logon1 = Image.open("./img/negado.png")
        self.__logon1 = self.__logon1.resize((500, 500))
        self.__logon1 = ImageTk.PhotoImage(self.__logon1)
        self.__lblimagennegado = tk.Label(self.__ventana, image=self.__logon1, width=500, height=500)
        self.__lblimagennegado.place(x=150, y=120)

    def operacion(self, funcion):
        self.clearall()
        if self.__nivel==1:
            funcion()
        else:
            self.negado()
