import tkinter as tk
from datetime import datetime
from tkinter import ttk, NO
import sql
from PIL import Image, ImageTk
from tkinter import messagebox
import re

class Servicio:

    def __init__(self, ventana, nivel):
        self.__ancho = 1072
        self.__alto = 630
        self.__ventana = ventana
        self.__nivel = nivel
        self.__data = None
        self.__framealtas = None
        self.__framebajas = None
        self.__framecambios = None
        self.__framereportes = None
        self.__framebotones = None
        self.__strvar1 = tk.StringVar()
        self.__strvar1.trace("w", self.filtroonchange)
        self.__sql = sql.SQL()
        self.__lblimagennegado=None
        paises = self.__sql.getpaises()
        self.__datapaises = {}

        if paises != None:
            for fila in paises:
                self.__datapaises[fila[1]]= [fila[0],fila[2]]

    def filtroonchange(self, index, values, op):
        filtro1= self.__cmbfiltro1.get()
        self.__cmbfiltro2.set("")
        if filtro1 != "" :
            if filtro1 == "Tipo servicio":
                self.__cmbfiltro2 ["values"] = ["Todos","Paquete", "Vuelo", "Hotel", "Traslado", "Atraccion"]
            elif filtro1 == "Costo" :
                self.__cmbfiltro2 ["values"] = ["Todos", "0-4999", "5000-9999", "10000-49999", "50000-máx"]
            elif filtro1 == "Comision" :
                self.__cmbfiltro2 ["values"] = ["Todos", "0-4.99", "5-9.99", "10-14.99", "15-19.99", "20-máx"]
            else:
                self.__cmbfiltro2 ["values"] = ["Todos"] + list(self.__datapaises.keys())

    def actualizabotones(self, subseccion):
        self.__btnaltas.config(bg="#565656", fg="#FFFFFF")
        self.__btnbajas.config(bg="#565656", fg="#FFFFFF")
        self.__btncambios.config(bg="#565656", fg="#FFFFFF")
        self.__btnreportes.config(bg="#565656", fg="#FFFFFF")

        if subseccion== "altas":
            self.__btnaltas.config(bg="#DAA520", fg="#000000")
        elif subseccion== "bajas":
            self.__btnbajas.config(bg="#DAA520", fg="#000000")
        elif subseccion== "cambios":
            self.__btncambios.config(bg="#DAA520", fg="#000000")
        elif subseccion == "reportes":
            self.__btnreportes.config(bg="#DAA520", fg="#000000")

    def altas(self):
        self.actualizabotones("altas")

        self.__framealtas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framealtas, text="Alta servicio", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # Servicio
        lbltipo = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de servicio:", font=("Sora", 11))
        lbltipo.place(x=10, y=20)
        self.__cmbtipo = ttk.Combobox(self.__generallblFrm,
                                          width=60, values=["Paquete", "Vuelo", "Hotel", "Traslado", "Atraccion"])
        self.__cmbtipo.place(x=10, y=40)

        # Titulo
        lbltitulo = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Título: ", font=("Sora", 11))
        lbltitulo.place(x=450, y=20)
        self.__txttitulo = tk.Entry(self.__generallblFrm, width=40, font=("Sora", 12), highlightthickness=3)
        self.__txttitulo.place(x=450, y=40)

        #detalles
        self.__detalleslblFrm = tk.LabelFrame(self.__framealtas, text="Detalles de servicio", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=270, font=("Sora", 10))
        self.__detalleslblFrm.place(x=10, y=120)

        #subtipo
        lblsubtipo= tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Subtipo:", font=("Sora", 11))
        lblsubtipo.place(x=10, y=10)
        self.__cmbsubtipo = ttk.Combobox(self.__detalleslblFrm,
                                          width=60, values=["Lunamielero", "Graduación", "Todo incluido", "N/A"])
        self.__cmbsubtipo.place(x=10, y=40)

        # fechainicio
        lblinicio = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Fecha inicio: ", font=("Sora", 10))
        lblinicio.place(x=450, y=10)
        lblinicio = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblinicio.place(x=540, y=10)
        self.__txtinicio = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtinicio.place(x=450, y=40)

        # fechafinal
        lblfinal = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Fecha final: ", font=("Sora", 10))
        lblfinal.place(x=690, y=10)
        lblifinal = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblifinal.place(x=780, y=10)
        self.__txtfinal = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtfinal.place(x=690, y=40)

        # país
        lblpais = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="País:", font=("Sora", 11))
        lblpais.place(x=10, y=80)
        self.__cmbpais = ttk.Combobox(self.__detalleslblFrm,
                                         width=60, values=list(self.__datapaises.keys()))
        self.__cmbpais.place(x=10, y=105)

        # estado
        lblestado = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Estado: ", font=("Sora", 10))
        lblestado.place(x=450, y=80)
        lblestado = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="(ó región)", font=("Sora", 8))
        lblestado.place(x=540, y=80)
        self.__txtestado = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtestado.place(x=450, y=105)

        # ciudad
        lblciudad = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Ciudad: ", font=("Sora", 10))
        lblciudad.place(x=690, y=80)
        lblciudad = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="Provincia", font=("Sora", 8))
        lblciudad.place(x=780, y=80)
        self.__txtciudad = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtciudad.place(x=690, y=105)

        #detalles
        lbldetalles= tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Detalles:", font=("Sora", 11))
        lbldetalles.place(x=10, y=150)
        self.__txtdetalles = tk.Text(self.__detalleslblFrm, width=50, height=3)
        self.__txtdetalles.place(x=10, y=175)

        # Restricciones
        lblrestricciones = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Restricciones: ", font=("Sora", 11))
        lblrestricciones.place(x=450, y=150)
        self.__txtrestricciones = tk.Text(self.__detalleslblFrm, width=50, height=3)
        self.__txtrestricciones.place(x=450, y=175)

        #Costos
        self.__costoslblFrm = tk.LabelFrame(self.__framealtas, text="Costos", bg="#FFFFFF",
                                              width=self.__ancho - 20, height=120, font=("Sora", 10))
        self.__costoslblFrm.place(x=10, y=395)

        #Costo
        lblcosto=tk.Label(self.__costoslblFrm, bg="#FFFFFF", text="Costo $:", font=("Sora",11))
        lblcosto.place(x=10, y=10)
        self.__txtcosto = tk.Entry(self.__costoslblFrm, width=25, font=("Sora", 12), highlightthickness=3)
        self.__txtcosto.place(x=10, y=40)

        #comision
        lblcomision=tk.Label(self.__costoslblFrm, bg="#FFFFFF", text="Comisión:", font=("Sora",11))
        lblcomision.place(x=450, y=10)
        self.__txtcomision = tk.Entry(self.__costoslblFrm, width=25, font=("Sora", 12), highlightthickness=3)
        self.__txtcomision.place(x=450, y=40)

        # boton agregar
        btnagregar= tk.Button(self.__framealtas, bg="#00c800", text="Agregar", width=20, command= self.insertarservicio)
        btnagregar.place(x=900, y=590)

        #frame
        self.__framealtas.place(x=130, y=110)

    def validafecha(self,fecha):
        fechaok=True
        listfecha = fecha.split("-")
        if len(listfecha) == 3:
            if len(listfecha[0]) == 4 and len(listfecha[1]) == 2 and len(listfecha[2]) == 2 and listfecha[0].isnumeric() \
                and listfecha[1].isnumeric() and listfecha[2].isnumeric():
                anio=int(listfecha[0])
                mes=int(listfecha[1])
                dia=int(listfecha[2])
                if not (anio>=datetime.now().year):
                    messagebox.showerror(message="Año no válido", title="ERROR")
                    fechaok=False
                if not (mes>=1 and mes<=12) and (datetime.now().year==anio and mes<datetime.now().month):
                    messagebox.showerror(message="Mes no válido", title="ERROR")
                    fechaok = False
                if not (dia>=1 and dia<=31) and (datetime.now().year==anio and datetime.now().month==mes and dia<datetime.now().day):
                    messagebox.showerror(message="Día no válido", title="ERROR")
                    fechaok = False
            else:
                messagebox.showerror(message="Formato de fecha no válido", title="ERROR")
                fechaok = False
        else:
            messagebox.showerror(message="Formato de fecha no válido", title="ERROR")
            fechaok = False
        return fechaok

    def validanumeros(self):
        regex = '[+-]?[0-9]+\.[0-9]+'
        if (re.search(regex, self.__txtcosto.get()) or self.__txtcosto.get().isnumeric()) and  (re.search(regex, self.__txtcomision.get()) or self.__txtcomision.get().isnumeric()):
            return True
        else:
            messagebox.showerror(
                message="EL CAMPO DEBE SER NUMERICO O DECIMAL", title="ERROR")
            return False

    def insertarservicio(self):
        if self.validavacios():
            if self.validafecha(self.__txtinicio.get()) and (self.__txtfinal.get()=="" or self.validafecha(self.__txtfinal.get())  and self.validanumeros()):
                datos = [self.__cmbtipo.get(), self.__txtcosto.get(), self.__txtdetalles.get("1.0","end-1c"),
                         self.__txttitulo.get(), self.__txtcomision.get(), self.__txtinicio.get(),
                         self.__txtrestricciones.get("1.0","end-1c"), self.__cmbsubtipo.get(), self.__txtciudad.get(), self.__txtestado.get(),
                         self.__cmbpais.get()]
                final = False
                if self.__txtfinal.get() != "":
                    datos.append(self.__txtfinal.get())
                    final = True
                self.__sql.insertarservicio(datos, final)
                messagebox.showinfo(message="GUARDADO CORRECTAMENTE", title="REGISTO EXITOSO")
                self.__framealtas.destroy()
                self.altas()

        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")



    def validavacios(self):

        if (self.__txtcosto.get() == "" or self.__txtdetalles.get("1.0","end-1c") == "" \
                or self.__txttitulo.get() == "" or self.__cmbtipo.get() == "" or self.__txtcomision.get() == "" or
                self.__txtinicio.get()=="" or self.__cmbsubtipo.get()== "" or self.__cmbpais.get()==""):
            return False
        else:
            return True

    def bajas(self):
        self.actualizabotones("bajas")

        # formulario
        self.__framebajas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framebajas, text="Baja servicio", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # servicio
        lblservicio = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Servicio: ", font=("Sora", 10))
        lblservicio.place(x=50, y=10)

        self.__data = self.__sql.getservicios()
        listaservicios= []
        if (self.__data != None):
            for fila in self.__data:
                servicio = fila[4]
                listaservicios.append(servicio)

        # Combo de los servicios
        cmbservicios = ttk.Combobox(self.__generallblFrm, width=40, font=("Sora", 10), state="readonly", values=listaservicios)
        cmbservicios.place(x=120, y=10)

        btnseleccionar = tk.Button(self.__generallblFrm, text="Seleccionar",  bg="#565656", width=20,fg="#D3D3D3",
                                   command=lambda: self.detallesservicio(cmbservicios.get()))
        btnseleccionar.place(x=480, y=10)

        #frame
        self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20, height=500)
        self.__framedatos.place(x=10, y=80)

        # botones

        btneliminar = tk.Button(self.__framebajas, text="Eliminar", bg="#800000", width=20,fg="#D3D3D3", command= lambda: self.eliminarservicio(cmbservicios.get()))
        btneliminar.place(x=900, y=590)


        # lo blanco
        self.__framebajas.place(x=130, y=110)

    def eliminarservicio(self, nombre):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún servicio", title="ERROR")
        else:

            # servicio
            servicio = [fila for fila in self.__data]
            id_servicio= servicio[0][0]
            self.__sql.eliminarservicio(id_servicio)
            messagebox.showinfo(message="El servicio se elimino correctamente.", title="Registro eliminado")
            self.__framebajas.destroy()
            self.bajas()

    def detallesservicio(self, titulo):

        if (titulo == ""):
            messagebox.showerror(message="No se selecciono ningun servicio", title="ERROR")
        else:
            self.__framedatos.destroy()
            self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20, height=500)
            self.__framedatos.place(x=10, y=80)
            servicios = [fila for fila in self.__data]
            # print(self.__data)

            # titulo
            lbltitulo = tk.Label(self.__framedatos, bg="#FFFFFF", text="Servicio: ", font=("Sora", 10))
            lbltitulo.place(x=5, y=5)
            lbltitulovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=titulo, font=("Sora", 10))
            lbltitulovalor.place(x=100, y=5)

            # tiposervicio
            lbltiposervicio = tk.Label(self.__framedatos, bg="#FFFFFF", text="Tipo: ", font=("Sora", 10))
            lbltiposervicio.place(x=5, y=25)
            lbltiposerviciovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][1], font=("Sora", 10))
            lbltiposerviciovalor.place(x=100, y=25)

            # Costo
            lblcosto = tk.Label(self.__framedatos, bg="#FFFFFF", text="Costo: ", font=("Sora", 10))
            lblcosto.place(x=5, y=45)
            lblcostovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][2], font=("Sora", 10))
            lblcostovalor.place(x=100, y=45)

            # detalles
            lbldetalles = tk.Label(self.__framedatos, bg="#FFFFFF", text="Detalles: ", font=("Sora", 10))
            lbldetalles.place(x=5, y=65)
            lbldetallesvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][3], font=("Sora", 10))
            lbldetallesvalor.place(x=100, y=65)

            # comision
            lblcomision = tk.Label(self.__framedatos, bg="#FFFFFF", text="Comisión: ", font=("Sora", 10))
            lblcomision.place(x=5, y=85)
            lblcomisionvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][5], font=("Sora", 10))
            lblcomisionvalor.place(x=100, y=85)

            # inicio
            lblinicio = tk.Label(self.__framedatos, bg="#FFFFFF", text="Fecha inicio: ", font=("Sora", 10))
            lblinicio.place(x=5, y=105)
            lbliniciovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][6], font=("Sora", 10))
            lbliniciovalor.place(x=100, y=105)

            # final
            lblfinal = tk.Label(self.__framedatos, bg="#FFFFFF", text="Fecha final: ", font=("Sora", 10))
            lblfinal.place(x=5, y=125)
            lblfinalvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][7], font=("Sora", 10))
            lblfinalvalor.place(x=100, y=125)

            # Restricciones
            lblrestricciones = tk.Label(self.__framedatos, bg="#FFFFFF", text="Restricciones: ", font=("Sora", 10))
            lblrestricciones.place(x=5, y=145)
            lblrestriccionesvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][8], font=("Sora", 10))
            lblrestriccionesvalor.place(x=100, y=145)

            # sugbtipo
            lblsubtipo = tk.Label(self.__framedatos, bg="#FFFFFF", text="Subtipo: ", font=("Sora", 10))
            lblsubtipo.place(x=5, y=165)
            lblsubtipovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][9], font=("Sora", 10))
            lblsubtipovalor.place(x=100, y=165)

            # ciudad
            lblciudad = tk.Label(self.__framedatos, bg="#FFFFFF", text="Ciudad: ", font=("Sora", 10))
            lblciudad.place(x=5, y=185)
            lblciudadvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][10], font=("Sora", 10))
            lblciudadvalor.place(x=100, y=185)

            # estado
            lblestado = tk.Label(self.__framedatos, bg="#FFFFFF", text="Estado: ", font=("Sora", 10))
            lblestado.place(x=5, y=205)
            lblestadovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][11], font=("Sora", 10))
            lblestadovalor.place(x=100, y=205)

            # Pais
            lblpais = tk.Label(self.__framedatos, bg="#FFFFFF", text="País: ", font=("Sora", 10))
            lblpais.place(x=5, y=225)
            lblpaisvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=servicios[0][12], font=("Sora", 10))
            lblpaisvalor.place(x=100, y=225)



    def muestradatos(self, nombre=""):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún servicio", title="ERROR")
        self.cambios(nombre)
    def cambios(self, nombre=""):
        self.actualizabotones("cambios")

        self.__framecambios = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)
        self.__seleccionlblFrm = tk.LabelFrame(self.__framecambios, text="", bg="#FFFFFF", width=self.__ancho - 20, height=45, font=("Sora", 10))
        self.__seleccionlblFrm.place(x=10, y=5)
        self.__data = self.__sql.getservicios()
        listaservicios = []
        if (self.__data != None):
            for fila in self.__data:
                servicio = fila[4]
                listaservicios.append(servicio)

        # combo para seleccionar el servicio
        lblservicio = tk.Label(self.__seleccionlblFrm, bg="#FFFFFF", text="Servicio: ", font=("Sora", 10))
        lblservicio.place(x=50, y=10)
        self.__cmbservicio = ttk.Combobox(self.__seleccionlblFrm, width=40, font=("Sora", 10), state="readonly",
                                  values=listaservicios)
        self.__cmbservicio.place(x=120, y=10)
        btnseleccionar = tk.Button(self.__seleccionlblFrm, text="Seleccionar", bg="#565656", width=20,fg="#D3D3D3",
                                   command=lambda: self.muestradatos(self.__cmbservicio.get()))
        btnseleccionar.place(x=445, y=10)
        self.__generallblFrm = tk.LabelFrame(self.__framecambios, text="Editar servicio", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=100, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=50)

        # Servicio
        lbltipo = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Tipo de servicio:", font=("Sora", 11))
        lbltipo.place(x=10, y=20)
        self.__cmbtipo = ttk.Combobox(self.__generallblFrm,
                                          width=60, values=["Paquete", "Vuelo", "Hotel", "Traslado", "Atraccion"])
        self.__cmbtipo.place(x=10, y=40)

        # Titulo
        lbltitulo = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Título: ", font=("Sora", 11))
        lbltitulo.place(x=450, y=20)
        self.__txttitulo = tk.Entry(self.__generallblFrm, width=40, font=("Sora", 12), highlightthickness=3)
        self.__txttitulo.place(x=450, y=40)

        # detalles
        self.__detalleslblFrm = tk.LabelFrame(self.__framecambios, text="Detalles de servicio", bg="#FFFFFF",
                                              width=self.__ancho - 20, height=270, font=("Sora", 10))
        self.__detalleslblFrm.place(x=10, y=160)

        # subtipo
        lblsubtipo = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Subtipo:", font=("Sora", 11))
        lblsubtipo.place(x=10, y=10)
        self.__cmbsubtipo = ttk.Combobox(self.__detalleslblFrm,
                                         width=60, values=["Lunamielero", "Graduación", "Todo incluido", "N/A"])
        self.__cmbsubtipo.place(x=10, y=40)

        # fechainicio
        lblinicio = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Fecha inicio: ", font=("Sora", 10))
        lblinicio.place(x=450, y=10)
        lblinicio = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblinicio.place(x=540, y=10)
        self.__txtinicio = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtinicio.place(x=450, y=40)

        # fechafinal
        lblfinal = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Fecha final: ", font=("Sora", 10))
        lblfinal.place(x=690, y=10)
        lblifinal = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblifinal.place(x=780, y=10)
        self.__txtfinal = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtfinal.place(x=690, y=40)

        # país
        lblpais = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="País:", font=("Sora", 11))
        lblpais.place(x=10, y=80)
        self.__cmbpais = ttk.Combobox(self.__detalleslblFrm,
                                      width=60, values=list(self.__datapaises.keys()))
        self.__cmbpais.place(x=10, y=105)

        # estado
        lblestado = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Estado: ", font=("Sora", 10))
        lblestado.place(x=450, y=80)
        lblestado = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="(ó región)", font=("Sora", 8))
        lblestado.place(x=540, y=80)
        self.__txtestado = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtestado.place(x=450, y=105)

        # ciudad
        lblciudad = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Ciudad: ", font=("Sora", 10))
        lblciudad.place(x=690, y=80)
        lblciudad = tk.Label(self.__detalleslblFrm, bg="#A9A9A9", text="Provincia", font=("Sora", 8))
        lblciudad.place(x=780, y=80)
        self.__txtciudad = tk.Entry(self.__detalleslblFrm, width=23, font=("sora", 10))
        self.__txtciudad.place(x=690, y=105)

        # detalles
        lbldetalles = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Detalles:", font=("Sora", 11))
        lbldetalles.place(x=10, y=150)
        self.__txtdetalles = tk.Text(self.__detalleslblFrm, width=50, height=3)
        self.__txtdetalles.place(x=10, y=175)

        # Restricciones
        lblrestricciones = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Restricciones: ", font=("Sora", 11))
        lblrestricciones.place(x=450, y=150)
        self.__txtrestricciones = tk.Text(self.__detalleslblFrm, width=50, height=3)
        self.__txtrestricciones.place(x=450, y=175)

        # Costos
        self.__costoslblFrm = tk.LabelFrame(self.__framecambios, text="Costos", bg="#FFFFFF",
                                            width=self.__ancho - 20, height=120, font=("Sora", 10))
        self.__costoslblFrm.place(x=10, y=440)

        # Costo
        lblcosto = tk.Label(self.__costoslblFrm, bg="#FFFFFF", text="Costo $:", font=("Sora", 11))
        lblcosto.place(x=10, y=10)
        self.__txtcosto = tk.Entry(self.__costoslblFrm, width=25, font=("Sora", 12), highlightthickness=3)
        self.__txtcosto.place(x=10, y=40)

        # comision
        lblcomision = tk.Label(self.__costoslblFrm, bg="#FFFFFF", text="Comisión:", font=("Sora", 11))
        lblcomision.place(x=450, y=10)
        self.__txtcomision = tk.Entry(self.__costoslblFrm, width=25, font=("Sora", 12), highlightthickness=3)
        self.__txtcomision.place(x=450, y=40)


        param1 = ""


        if nombre != "":
            # servicios

            actual = [fila for fila in self.__data if nombre== fila[4]]

            self.__cmbtipo.set(actual[0][1])
            self.__txtcosto.insert(0, actual[0][2])
            self.__txtdetalles.insert("end-1c", actual[0][3])
            self.__txttitulo.insert(0, actual[0][4])
            self.__txtcomision.insert(0, actual[0][5])
            self.__txtinicio.insert(0, actual[0][6])
            if actual [0][7] != None:
                self.__txtfinal.insert(0, actual[0][7])
            self.__txtrestricciones.insert("end-1c", actual[0][8])
            self.__cmbsubtipo.set(actual[0][9])
            self.__txtciudad.insert(0, actual[0][10])
            self.__txtestado.insert(0, actual[0][11])
            self.__cmbpais.set( actual[0][12])
            self.__cmbservicio.set( nombre)
            param1 = actual[0][0]



        # botones
        # botoncancelat y agregar
        btnagregar = tk.Button(self.__framecambios, bg="#00c800", text="Editar", width=20, command= lambda: self.cambiosservicios(param1))
        btnagregar.place(x=900, y=590)

        # frame
        self.__framecambios.place(x=130, y=110)

    def cambiosservicios(self, id_servicio):
        if self.validavacios():
            if self.validafecha(self.__txtinicio.get()) and (self.__txtfinal.get() == "" or self.validafecha(self.__txtfinal.get()) and self.validanumeros()):
                final= False
                datos = [self.__cmbtipo.get(), self.__txtcosto.get(), self.__txtdetalles.get("1.0","end-1c"),
                         self.__txttitulo.get(), self.__txtcomision.get(), self.__txtinicio.get(),
                         self.__txtrestricciones.get("1.0","end-1c"), self.__cmbsubtipo.get(), self.__txtciudad.get(),
                         self.__txtestado.get(), self.__cmbpais.get()]
                if self.__txtfinal.get() != "":
                    datos.append(self.__txtfinal.get())
                    final= True
                datos.append(id_servicio)
                self.__sql.editarservicio(datos, final)

                messagebox.showinfo(message="MODIFICADO CORRECTAMENTE", title="REGISTO EXITOSO")
                self.__framecambios.destroy()
                self.cambios()
        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")

    def reportes(self):
        self.actualizabotones("reportes")

        # formulario
        self.__framereportes = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framereportes, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # servicio
        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)


        # servicios
        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                  values=["Tipo servicio", "Pais", "Costo", "Comision"], textvar=self.__strvar1)
        self.__cmbfiltro1.place(x=80, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                  values=[""])
        self.__cmbfiltro2.place(x=260, y=10)

        btnfiltrar = tk.Button(self.__generallblFrm, text="Filtrar", bg="#565656", width=20, fg="#D3D3D3",
                               command=lambda: self.filtrar(self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        btnfiltrar.place(x=480, y=5)

        self.__framedatos = tk.LabelFrame(self.__framereportes, text="Reporte", bg="#FFFFFF", width=self.__ancho - 20,
                                          height=400)
        self.__framedatos.place(x=10, y=80)

        self.__tablaservicios = ttk.Treeview(self.__framedatos,
                                             columns=( "#", "tipo", "subtipo", "titulo", "costo", "comision", "pais"), show="headings")

        self.__tablaservicios.heading("#", text="Id", anchor=tk.W)
        self.__tablaservicios.column("#", minwidth=0, width=20, stretch=NO, anchor=tk.W)
        self.__tablaservicios.heading("tipo", text="Tipo", anchor=tk.W)
        self.__tablaservicios.column("tipo", minwidth=0, width=200, stretch=NO, anchor=tk.W)
        self.__tablaservicios.heading("subtipo", text="Subtipo", anchor=tk.W)
        self.__tablaservicios.column("subtipo", minwidth=0, width=200, stretch=NO, anchor=tk.W)
        self.__tablaservicios.heading("titulo", text="Titulo", anchor=tk.W)
        self.__tablaservicios.heading("costo", text="Costo", anchor=tk.W)
        self.__tablaservicios.column("titulo", minwidth=0, width=200, stretch=NO, anchor=tk.W)
        self.__tablaservicios.column("costo", minwidth=0, width=93, stretch=NO, anchor=tk.W)
        self.__tablaservicios.heading("comision", text="Comisión", anchor=tk.W)
        self.__tablaservicios.column("comision", minwidth=0, width=93, stretch=NO, anchor=tk.W)
        self.__tablaservicios.heading("pais", text="País", anchor=tk.W)
        self.__tablaservicios.column("pais", minwidth=0, width=120, stretch=NO, anchor=tk.W)
        self.__tablaservicios.place(x=5, y=5, width=self.__ancho - 40, height=360)
        self.__cmbfiltro1.set("")
        self.__cmbfiltro2.set("")

        # lo blanco
        self.__framereportes.place(x=130, y=110)

    def filtrar(self,filtro1,filtro2):
        if filtro1 == "" or filtro2 == "":
            messagebox.showerror(message="Seleccione un filtro", title="ERROR")
        else:
            self.limpiartabla()
            servicios = self.__sql.getserviciosby(filtro1,filtro2)
            if servicios == None:
                messagebox.showinfo(message="No hay valores en este filtro", title="Sin registros")
            else:
                registro = []
                for fila in servicios:
                    registro = [fila[0], fila[1], fila[9], fila[4], "$" + str(fila[2]), str(fila[5])+ "%", fila[12]]
                    self.__tablaservicios.insert(parent="", index=0, values=registro)

    def limpiartabla(self):
        elementos = self.__tablaservicios.get_children()
        for i in elementos:
            self.__tablaservicios.delete(i)

    def botonestodos(self):

        for elemento in self.__ventana.winfo_children():
            elemento.destroy()
        # parte blanca atras de los iconos izq
        canvas = tk.Canvas(self.__ventana, width=120, height=self.__alto, bg="#FFF")
        canvas.place(x=0, y=100)
        # linea separación izq
        canvaslinea = tk.Canvas(self.__ventana, width=2, height=self.__alto + 20, bg="#000000")
        canvaslinea.place(x=120, y=100)

        self.__framebotones = tk.Frame(self.__ventana, bg="#FFFFFF", width=120, height=self.__alto)
        # logo
        self.__logon = Image.open("./img/servicios.png")
        self.__logon = self.__logon.resize((100, 100))
        self.__logon = ImageTk.PhotoImage(self.__logon)
        self.__lblimagen = tk.Label(self.__framebotones, image=self.__logon, width=100, height=100)
        self.__lblimagen.place(x=10, y=0)

        self.__btnaltas = tk.Button(self.__framebotones, bg="#565656", text="Altas", width=12, height=1, font=("Sora", 10),fg="#D3D3D3",
                                    command=lambda: self.operacion(self.altas, "a"))
        self.__btnaltas.place(x=10, y=130)

        self.__btnbajas = tk.Button(self.__framebotones, bg="#565656", text="Bajas", width=12, height=1, font=("Sora", 10),fg="#D3D3D3",
                                    command=lambda: self.operacion(self.bajas, "b"))
        self.__btnbajas.place(x=10, y=158)

        self.__btncambios = tk.Button(self.__framebotones, bg="#565656", text="Cambios", width=12, height=1,
                                      font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.cambios, "c"))
        self.__btncambios.place(x=10, y=186)

        self.__btnreportes = tk.Button(self.__framebotones, bg="#565656", text="Reportes", width=12, height=1,
                                       font=("Sora", 10),fg="#D3D3D3", command= lambda: self.operacion(self.reportes, "r"))
        self.__btnreportes.place(x=10, y=214)

        self.__framebotones.place(x=0, y=120)

    def clearall(self):
        if self.__lblimagennegado != None:
            self.__lblimagennegado.destroy()
            self.__lblimagennegado=None

        if(self.__framecambios != None):
            self.__framecambios.destroy()
        if (self.__framealtas != None):
            self.__framealtas.destroy()
        if (self.__framebajas != None):
            self.__framebajas.destroy()
        if (self.__framereportes != None):
            self.__framereportes.destroy()
    def negado(self):

        # negado img
        self.__logon1 = Image.open("./img/negado.png")
        self.__logon1 = self.__logon1.resize((500, 500))
        self.__logon1 = ImageTk.PhotoImage(self.__logon1)
        self.__lblimagennegado = tk.Label(self.__ventana, image=self.__logon1, width=500, height=500)
        self.__lblimagennegado.place(x=150, y=120)

    def operacion(self, funcion, op):
        self.clearall()
        if self.__nivel == 1:
            funcion()
        elif self.__nivel == 2:
            if op == "a" or op == "b" or op == "c" or op == "r":
                funcion()
            else:
                self.negado()
        elif self.__nivel == 3:
            if op == "a" or op == "c" or op == "r":
                funcion()
            else:
                self.negado()
        else:
            self.negado()
