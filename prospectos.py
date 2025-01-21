import tkinter as tk
from tkinter import ttk, NO
import sql
from PIL import Image, ImageTk
from tkinter import messagebox


class Prospecto:

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
        self.__sql = sql.SQL()
        self.__datacp = None
        paises = self.__sql.getpaises()
        self.__datapaises = {}
        self.__strvar = tk.StringVar()
        self.__nuevocp = False
        self.__strvar.trace("w", self.paisesonchange)
        self.__strvar1 = tk.StringVar()
        self.__strvar1.trace("w", self.filtroonchange)
        self.__lblimagennegado=None

        if paises != None:
            for fila in paises:
                self.__datapaises[fila[1]] = [fila[0], fila[2]]

    def filtroonchange(self, index, values, op):
        filtro1= self.__cmbfiltro1.get()
        self.__cmbfiltro2.set("")
        if filtro1 != "" :
            self.__cmbfiltro2 ["values"] = ["Todos"] + list(self.__datapaises.keys())

    def paisesonchange(self, index,value, op):
        self.__txtprefijo.delete(0,tk.END)
        if self.__cmbpais.get() != "":
            self.__txtprefijo.insert(0,self.__datapaises[self.__cmbpais.get()][1])
        #print(self.__cmbpais.get())

    def getcp(self):
        if self.__txtcp.get()=="":
            messagebox.showerror(message="AGREGA UN CÓDIGO POSTAL", title="ERROR")
        else:
            self.__datacp = self.__sql.getcp(self.__txtcp.get())
            self.__txtciudad.delete(0, tk.END)
            self.__txtestado.delete(0, tk.END)
            if self.__datacp == None:
                messagebox.showinfo(message="No se encontro el código postal. Rellene los datos y estos se guardaran ", title="No se encontro")
                self.__nuevocp=True
                self.__txtcolonia = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
                self.__txtcolonia.place(x=250, y=160)
            else:
                self.__txtciudad.insert(0,self.__datacp[0][3])
                self.__txtestado.insert(0, self.__datacp[0][4])
                listacolonias=[]
                for fila in self.__datacp:
                    listacolonias.append(fila[2])
                    print(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__cmbcolonia = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), state="readonly", values=listacolonias)
                self.__cmbcolonia.place(x=250, y=160)

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


        # formulario
        self.__framealtas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framealtas, text="Alta de prospecto", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=180, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)
        # self.__generalcanvas.create_rectangle(10,10,self.__ancho, 200)

        # lblarriba= tk.Label(self.__framealtas, bg="#FFFFFF", text="●—————————  Agregar empleado   —————————● ", font=("Sora", 18))
        # lblarriba.place(x=10, y=10)
        #
        # nombre
        lblnombre = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Nombre(s): ", font=("Sora", 10))
        lblnombre.place(x=10, y=10)
        self.__txtnombre = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtnombre.place(x=10, y=40)

        # appat
        lblappat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido paterno: ", font=("Sora", 10))
        lblappat.place(x=250, y=10)
        self.__txtappat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtappat.place(x=250, y=40)

        # apmat
        lblapmat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido materno: ", font=("Sora", 10))
        lblapmat.place(x=490, y=10)
        self.__txtapmat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtapmat.place(x=490, y=40)

        # empresa
        lblempresa = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Empresa: ", font=("Sora", 10))
        lblempresa.place(x=10, y=70)
        self.__txtempresa = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtempresa.place(x=10, y=90)

        # descripcion
        lbldescripcion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descripcion: ", font=("Sora", 10))
        lbldescripcion.place(x=250, y=70)
        self.__txtdescripcion = tk.Text(self.__generallblFrm, width=60, height=3, font=("Sora", 10))
        self.__txtdescripcion.place(x=250, y=90)


        self.__datoslblFrm = tk.LabelFrame(self.__framealtas, text="Datos Generales", bg="#FFFFFF",
                                           width=self.__ancho - 20, height=280, font=("Sora", 10))
        self.__datoslblFrm.place(x=10, y=190)

        # país
        lblpais = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="País: ", font=("Sora", 10))
        lblpais.place(x=10, y=20)
        self.__cmbpais = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), textvar=self.__strvar, state="readonly", values=list(self.__datapaises.keys()))
        self.__cmbpais.place(x=10, y=40)

        # Prefijo
        lblprefijo = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Prefijo: ", font=("Sora", 10))
        lblprefijo.place(x=250, y=20)
        self.__txtprefijo = tk.Entry(self.__datoslblFrm, width=13, font=("Sora", 10))
        self.__txtprefijo.place(x=250, y=40)

        # Telefono
        lbltel = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Teléfono: ", font=("Sora", 10))
        lbltel.place(x=300, y=20)
        self.__txttel = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txttel.place(x=300, y=40)

        # Correo
        lblemail = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Correo: ", font=("Sora", 10))
        lblemail.place(x=490, y=20)
        lblmail2 = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: ejemplo@gmail.com", font=("Sora", 8))
        lblmail2.place(x=550, y=20)
        self.__txtemail = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtemail.place(x=490, y=40)

        # calle
        lblcalle = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Calle: ", font=("Sora", 10))
        lblcalle.place(x=10, y=70)
        lblcalle = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Seguridad", font=("Sora", 8))
        lblcalle.place(x=50, y=70)
        self.__txtcalle = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtcalle.place(x=10, y=100)

        # numeroexterior
        lblnumex = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Número exterior: ", font=("Sora", 10))
        lblnumex.place(x=250, y=70)
        lblnumex = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: 1234", font=("Sora", 8))
        lblnumex.place(x=355, y=70)
        self.__txtnumex = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtnumex.place(x=250, y=100)

        # numerointerior
        lblnumint = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Número interior: ", font=("Sora", 10))
        lblnumint.place(x=490, y=70)
        lblnumint = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: 1A", font=("Sora", 8))
        lblnumint.place(x=600, y=70)
        self.__txtnumint = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtnumint.place(x=490, y=100)

        # cp
        lblcp = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Código postal: ", font=("Sora", 10))
        lblcp.place(x=10, y=130)
        self.__txtcp = tk.Entry(self.__datoslblFrm, width=15, font=("Sora", 10))
        self.__txtcp.place(x=10, y=160)
        self.__btncp = tk.Button(self.__datoslblFrm, text="Buscar", width=10, command=self.getcp)
        self.__btncp.place(x=120, y=160)

        # colonia
        lblcolonia = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Colonia: ", font=("Sora", 10))
        lblcolonia.place(x=250, y=130)
        lblcolonia = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Valle Campana", font=("Sora", 8))
        lblcolonia.place(x=320, y=130)
        self.__cmbcolonia = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), state="readonly")
        self.__cmbcolonia.place(x=250, y=160)
        self.__txtcolonia = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtcolonia.place(x=250, y=160)

        # ciudad
        lblciudad = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Ciudad: ", font=("Sora", 10))
        lblciudad.place(x=490, y=130)
        lblciudad = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Monterrey", font=("Sora", 8))
        lblciudad.place(x=550, y=130)
        self.__txtciudad = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtciudad.place(x=490, y=160)

        # estado
        lblestado = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Estado: ", font=("Sora", 10))
        lblestado.place(x=730, y=130)
        lblestado = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: N.L", font=("Sora", 8))
        lblestado.place(x=800, y=130)
        self.__txtestado = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtestado.place(x=730, y=160)


        btnagregar = tk.Button(self.__framealtas, text="Agregar", bg="#00c800", width=20, command=self.insertarprospecto)
        btnagregar.place(x=900, y=590)

        self.__cmbpais.set("")

        # lo blanco
        self.__framealtas.place(x=130, y=110)

    def insertarprospecto(self):

        if self.validavacios():
            if self.__nuevocp:
                pais = self.__sql.getidpais(self.__cmbpais.get())
                datos = [self.__txtcp.get(), self.__txtcolonia.get(), self.__txtciudad.get(), self.__txtestado.get(),
                         pais]
                self.__sql.insertarcp(datos)
                messagebox.showinfo(message="SE AGREGÓ UN NUEVO REGISTRO AL CÓDIGO POSTAL", title="REGISTRO EXITOSO")

            cp = self.__sql.getcpid(self.__txtcp.get(), self.__txtcolonia.get())

            datos = [self.__txtcalle.get(), self.__txtnumex.get(), self.__txtnumint.get(), cp]
            self.__sql.insertardireccion(datos)
            iddireccion = self.__sql.ultimoiddireccion()

            datos= [ self.__txtempresa.get(), self.__txttel.get(), self.__txtnombre.get(), self.__txtdescripcion.get("1.0", "end-1c"), iddireccion, self.__txtemail.get(), self.__txtappat.get(), self.__txtapmat.get()]
            self.__sql.insertarprospecto(datos)
            messagebox.showinfo(message="GUARDADO CORRECTAMENTE", title="REGISTO EXITOSO")
            self.__framealtas.destroy()
            self.altas()

        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")

    def validavacios(self):
        if not self.__nuevocp:
            self.__txtcolonia.delete(0,tk.END)
            self.__txtcolonia.insert(0,self.__cmbcolonia.get())
        if ( self.__txtempresa.get() == "" or self.__txtnombre.get() == "" or self.__txtdescripcion.get("1.0","end-1c") == "" or
                self.__txtemail.get() == "" or self.__txtappat.get() == "" or self.__txtapmat == "" or self.__txtcalle.get() == ""
                or self.__txtnumex.get() == "" or self.__txtcolonia.get() == "" or self.__txtcp.get() == "" or self.__txtciudad.get() == "" or
                self.__txtestado.get() == "" or self.__cmbpais.get() == ""):
            return False
        else:
            return True


    def detallesprospecto (self, nombre):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún prospecto", title="ERROR")
        else:
            self.__framedatos.destroy()
            self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20,
                                              height=300)
            self.__framedatos.place(x=10, y=80)
            lista= nombre.split()

            #prospecto
            prospecto= [fila for fila in self.__data if lista[0] == fila [7] and lista[1] == fila[8] and lista[2] == fila[3]]
            #print(empleado, type(empleado))

            # nombre
            lblnombre = tk.Label(self.__framedatos, bg="#FFFFFF", text="Nombre: ", font=("Sora", 10))
            lblnombre.place(x=5, y=5)
            lblnombrevalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=nombre, font=("Sora", 10))
            lblnombrevalor.place(x=80, y=5)

            #empresa
            lblempresa = tk.Label(self.__framedatos, bg="#FFFFFF", text="Empresa: ", font=("Sora", 10))
            lblempresa.place(x=5, y=25)
            lblempresavalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][1], font=("Sora", 10))
            lblempresavalor.place(x=80, y=25)

            # telefono
            lbltelefono = tk.Label(self.__framedatos, bg="#FFFFFF", text="Teléfono: ", font=("Sora", 10))
            lbltelefono.place(x=5, y=45)
            telefono= str(prospecto[0][22]) + " " + prospecto[0][2]
            lbltelefonovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=telefono, font=("Sora", 10))
            lbltelefonovalor.place(x=80, y=45)

            # correo
            lblcorreo = tk.Label(self.__framedatos, bg="#FFFFFF", text="Correo: ", font=("Sora", 10))
            lblcorreo.place(x=5, y=65)
            lblcorreovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][6], font=("Sora", 10))
            lblcorreovalor.place(x=80, y=65)

            #descripcion
            lbldescripcion = tk.Label(self.__framedatos, bg="#FFFFFF", text="Descripción: ", font=("Sora", 10))
            lbldescripcion.place(x=5, y=85)
            lbldescripcionvalor = tk.Label(self.__framedatos,  bg="#FFFFFF", text=prospecto[0][4], font=("Sora", 10))
            lbldescripcionvalor.place(x=80, y=85)



            #direcciones


            #calle
            lblcalle = tk.Label(self.__framedatos, bg="#FFFFFF", text="Calle: ", font=("Sora", 10))
            lblcalle.place(x=5, y=105)
            lblcallevalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][10], font=("Sora", 10))
            lblcallevalor.place(x=80, y=105)

            #no_exterior
            lblexterior = tk.Label(self.__framedatos, bg="#FFFFFF", text="No. exterior: ", font=("Sora", 10))
            lblexterior.place(x=5, y=125)
            lblexteriorvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][11], font=("Sora", 10))
            lblexteriorvalor.place(x=80, y=125)

            # no_interior
            lblinterior = tk.Label(self.__framedatos, bg="#FFFFFF", text="No. interior: ", font=("Sora", 10))
            lblinterior.place(x=5, y=145)
            lblinteriorvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][12], font=("Sora", 10))
            lblinteriorvalor.place(x=80, y=145)

            #colonia
            lblcolonia = tk.Label(self.__framedatos, bg="#FFFFFF", text="Colonia:", font=("Sora", 10))
            lblcolonia.place(x=5, y=165)
            lblcoloniavalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][16], font=("Sora", 10))
            lblcoloniavalor.place(x=80, y=165)

            #cp
            lblcp= tk.Label(self.__framedatos, bg="#FFFFFF", text="Cp:", font=("Sora", 10))
            lblcp.place(x=5, y=185)
            lblcpvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][15], font=("Sora", 10))
            lblcpvalor.place(x=80, y=185)

            #ciudad
            lblciudad = tk.Label(self.__framedatos, bg="#FFFFFF", text="Ciudad:", font=("Sora", 10))
            lblciudad.place(x=5, y=205)
            lblciudadvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][17], font=("Sora", 10))
            lblciudadvalor.place(x=80, y=205)

            #estado
            lblestado = tk.Label(self.__framedatos, bg="#FFFFFF", text="Ciudad:", font=("Sora", 10))
            lblestado.place(x=5, y=225)
            lblestadovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][18], font=("Sora", 10))
            lblestadovalor.place(x=80, y=225)

            #pais
            lblpais = tk.Label(self.__framedatos, bg="#FFFFFF", text="País:", font=("Sora", 10))
            lblpais.place(x=5, y=245)
            lblpaisvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=prospecto[0][21], font=("Sora", 10))
            lblpaisvalor.place(x=80, y=245)


    def bajas(self):
        self.actualizabotones("bajas")

        # formulario
        self.__framebajas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framebajas, text="Baja prospecto", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # prospecto
        lblprospecto= tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Prospecto: ", font=("Sora", 10))
        lblprospecto.place(x=50, y=10)

        self.__data = self.__sql.getprospectos()
        listaprospectos = []
        if self.__data != None:
            for fila in self.__data:
                prospecto = fila[7] + " " + fila[8] + " " + fila[3]
                listaprospectos.append(prospecto)

        # listadeprospectos
        cmbprospecto = ttk.Combobox(self.__generallblFrm, width=40, font=("Sora", 10), state="readonly",
                                 values=listaprospectos)
        cmbprospecto.place(x=120, y=10)

        btnseleccionar = tk.Button(self.__generallblFrm, text="Seleccionar", bg="#565656", fg="#D3D3D3",width=20, command= lambda: self.detallesprospecto(cmbprospecto.get()))
        btnseleccionar.place(x=480, y=10)

        self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20,
                                          height=300)
        self.__framedatos.place(x=10, y=80)

        # botones

        btneliminar = tk.Button(self.__framebajas, text="Eliminar", bg="#800000", width=20,fg="#D3D3D3", command= lambda : self.eliminarprospecto(cmbprospecto.get()))
        btneliminar.place(x=900, y=590)


        # lo blanco
        self.__framebajas.place(x=130, y=110)

    def eliminarprospecto(self, nombre):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún prospecto", title="ERROR")
        else:


            lista = nombre.split()
            # prospecto
            prospecto = [fila for fila in self.__data if
                        lista[0] == fila[7] and lista[1] == fila[8] and lista[2] == fila[3]]
            id_prospecto= prospecto[0][0]
            id_direccion= prospecto[0][5]
            self.__sql.eliminarprospecto(id_prospecto)
            self.__sql.eliminardireccion(id_direccion)
            messagebox.showinfo(message="El prospecto se elimino correctamente.", title="Registro eliminado")
            self.__framebajas.destroy()
            self.bajas()

    def muestradatos(self, nombre=""):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún empleado", title="ERROR")
        self.cambios(nombre)
    def cambios(self, nombre=""):
        self.actualizabotones("cambios")

        # formulario
        self.__framecambios = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)
        self.__seleccionlblFrm = tk.LabelFrame(self.__framecambios, text="", bg="#FFFFFF",
                                               width=self.__ancho - 20, height=45, font=("Sora", 10))
        self.__seleccionlblFrm.place(x=10, y=5)
        self.__data = self.__sql.getprospectos()
        listaprospectos = []
        if (self.__data != None):
            for fila in self.__data:
                prospecto = fila[7] + " " + fila[8] + " " + fila[3]
                listaprospectos.append(prospecto)

        # combo para seleccionar el prospecto
        lblprospecto = tk.Label(self.__seleccionlblFrm, bg="#FFFFFF", text="Prospecto: ", font=("Sora", 10))
        lblprospecto.place(x=50, y=10)
        self.__cmbprospecto = ttk.Combobox(self.__seleccionlblFrm, width=40, font=("Sora", 10), state="readonly",
                                  values=listaprospectos)
        self.__cmbprospecto.place(x=120, y=10)
        btnseleccionar = tk.Button(self.__seleccionlblFrm, text="Seleccionar", bg="#565656", fg="#D3D3D3", width=20,
                                   command=lambda: self.muestradatos(self.__cmbprospecto.get()))
        btnseleccionar.place(x=445, y=10)

        self.__generallblFrm = tk.LabelFrame(self.__framecambios, text="Editar prospecto", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=170, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=50)


        # nombre
        lblnombre = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Nombre(s): ", font=("Sora", 10))
        lblnombre.place(x=10, y=5)
        self.__txtnombre = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtnombre.place(x=10, y=35)

        # appat
        lblappat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido paterno: ", font=("Sora", 10))
        lblappat.place(x=250, y=5)
        self.__txtappat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtappat.place(x=250, y=35)

        # apmat
        lblapmat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido materno: ", font=("Sora", 10))
        lblapmat.place(x=490, y=5)
        self.__txtapmat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtapmat.place(x=490, y=35)

        # empresa
        lblempresa = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Empresa: ", font=("Sora", 10))
        lblempresa.place(x=10, y=60)
        self.__txtempresa = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtempresa.place(x=10, y=80)

        # descripcion
        lbldescripcion = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Descripcion: ", font=("Sora", 10))
        lbldescripcion.place(x=250, y=60)
        self.__txtdescripcion = tk.Text(self.__generallblFrm, width=60, height=3, font=("Sora", 10))
        self.__txtdescripcion.place(x=250, y=80)

        self.__datoslblFrm = tk.LabelFrame(self.__framecambios, text="Datos Generales", bg="#FFFFFF",
                                           width=self.__ancho - 20, height=250, font=("Sora", 10))
        self.__datoslblFrm.place(x=10, y=220)

        # país
        lblpais = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="País: ", font=("Sora", 10))
        lblpais.place(x=10, y=20)
        self.__cmbpais = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), textvar=self.__strvar, state="readonly", values=list(self.__datapaises.keys()))
        self.__cmbpais.place(x=10, y=40)


        # Prefijo
        lblprefijo = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Prefijo: ", font=("Sora", 10))
        lblprefijo.place(x=250, y=20)
        self.__txtprefijo = tk.Entry(self.__datoslblFrm, width=13, font=("Sora", 10))
        self.__txtprefijo.place(x=250, y=40)

        # Telefono
        lbltel = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Teléfono: ", font=("Sora", 10))
        lbltel.place(x=300, y=20)
        self.__txttel = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txttel.place(x=300, y=40)

        # Correo
        lblemail = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Correo: ", font=("Sora", 10))
        lblemail.place(x=490, y=20)
        lblmail2 = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: ejemplo@gmail.com", font=("Sora", 8))
        lblmail2.place(x=550, y=20)
        self.__txtemail = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtemail.place(x=490, y=40)

        # calle
        lblcalle = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Calle: ", font=("Sora", 10))
        lblcalle.place(x=10, y=70)
        lblcalle = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Seguridad", font=("Sora", 8))
        lblcalle.place(x=50, y=70)
        self.__txtcalle = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtcalle.place(x=10, y=100)

        # numeroexterior
        lblnumex = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Número exterior: ", font=("Sora", 10))
        lblnumex.place(x=250, y=70)
        lblnumex = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: 1234", font=("Sora", 8))
        lblnumex.place(x=355, y=70)
        self.__txtnumex = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtnumex.place(x=250, y=100)

        # numerointerior
        lblnumint = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Número interior: ", font=("Sora", 10))
        lblnumint.place(x=490, y=70)
        lblnumint = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: 1A", font=("Sora", 8))
        lblnumint.place(x=600, y=70)
        self.__txtnumint = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtnumint.place(x=490, y=100)

        # cp
        lblcp = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Código postal: ", font=("Sora", 10))
        lblcp.place(x=10, y=130)
        self.__txtcp = tk.Entry(self.__datoslblFrm, width=15, font=("Sora", 10))
        self.__txtcp.place(x=10, y=160)
        self.__btncp = tk.Button(self.__datoslblFrm, text="Buscar", width=10, command=self.getcp)
        self.__btncp.place(x=120, y=160)

        # colonia
        lblcolonia = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Colonia: ", font=("Sora", 10))
        lblcolonia.place(x=250, y=130)
        lblcolonia = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Valle Campana", font=("Sora", 8))
        lblcolonia.place(x=320, y=130)
        self.__cmbcolonia = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), state="readonly")
        self.__cmbcolonia.place(x=250, y=160)
        self.__txtcolonia = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtcolonia.place(x=250, y=160)

        # ciudad
        lblciudad = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Ciudad: ", font=("Sora", 10))
        lblciudad.place(x=490, y=130)
        lblciudad = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Monterrey", font=("Sora", 8))
        lblciudad.place(x=550, y=130)
        self.__txtciudad = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtciudad.place(x=490, y=160)

        # estado
        lblestado = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Estado: ", font=("Sora", 10))
        lblestado.place(x=730, y=130)
        lblestado = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: N.L", font=("Sora", 8))
        lblestado.place(x=800, y=130)
        self.__txtestado = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtestado.place(x=730, y=160)

        param1 = ""
        param2 = ""
        param3 = ""

        if nombre != "":
            lista = nombre.split()
            # prospecto
            actual = [fila for fila in self.__data if lista[0] == fila[7] and lista[1] == fila[8] and lista[2] == fila[3]]
            self.__cmbprospecto.set(nombre)
            self.__txtempresa.insert(0, actual[0][1])
            self.__txttel.insert(0,actual[0][2])
            self.__txtnombre.insert(0, actual[0][3])
            self.__txtdescripcion.insert("end-1c", actual[0][4])
            self.__txtemail.insert(0, actual[0][6])
            self.__txtappat.insert(0, actual[0][7])
            self.__txtapmat.insert(0,actual[0][8])
            self.__txtcalle.insert(0, actual[0][10])
            self.__txtnumex.insert(0, actual[0][11])
            self.__txtnumint.insert(0, actual[0][12])
            self.__txtcolonia.insert(0, actual[0][16])
            self.__cmbcolonia.set(actual[0][16])
            self.__txtcp.insert(0, actual[0][15])
            self.__txtciudad.insert(0, actual[0][17])
            self.__txtestado.insert(0, actual[0][18])
            self.__cmbpais.set( actual[0][21])
            param1 = actual[0][0]
            param2 = actual[0][5]
            param3 = actual[0][20]
        else:
            self.__cmbpais.set("")

        btneditar = tk.Button(self.__framecambios, text="Editar", bg="#00c800", width=20, command=lambda : self.cambiosprospecto(param1, param2, param3))
        btneditar.place(x=900, y=590)


        # lo blanco
        self.__framecambios.place(x=130, y=110)
        
    def cambiosprospecto(self, id_prospecto, id_direccion, id_pais):
        if self.validavacios() and self.__cmbprospecto.get() != "":
            if self.__nuevocp:
                datos = [self.__txtcp.get(), self.__txtcolonia.get(), self.__txtciudad.get(), self.__txtestado.get(),
                         id_pais]
                self.__sql.insertarcp(datos)
                messagebox.showinfo(message="SE AGREGÓ UN NUEVO REGISTRO AL CÓDIGO POSTAL", title="REGISTRO EXITOSO")
            cp = self.__sql.getcpid(self.__txtcp.get(), self.__txtcolonia.get())

            datos = [self.__txtcalle.get(), self.__txtnumex.get(), self.__txtnumint.get(), cp, id_direccion]
            self.__sql.editardireccion(datos)
            datos = [ self.__txtempresa.get(),   self.__txttel.get(),self.__txtnombre.get(),self.__txtdescripcion.get("1.0", "end-1c"),
                      id_direccion,  self.__txtemail.get(),self.__txtappat.get(), self.__txtapmat.get(),id_prospecto]
            self.__sql.editarprospecto(datos)
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

        # empleado
        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)


        # prospectos
        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                  values=["Pais"],  textvar=self.__strvar1)
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

        self.__tablaprospectos = ttk.Treeview(self.__framedatos,
                                             columns=( "#", "nombre", "appat", "apmat", "empresa",
                                                       "telefono", "correo", "pais"),
                                             show="headings")

        self.__tablaprospectos.heading("#", text="Id", anchor=tk.W)
        self.__tablaprospectos.column("#", minwidth=0, width=20, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("nombre", text="Nombre")
        self.__tablaprospectos.column("nombre", minwidth=0, width=83, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("appat", text="Paterno", anchor=tk.W)
        self.__tablaprospectos.column("appat", minwidth=0, width=83, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("apmat", text="Materno", anchor=tk.W)
        self.__tablaprospectos.column("apmat", minwidth=0, width=83, stretch=NO, anchor=tk.W)
        #self.__tablaprospectos.heading("curp", text="Curp", anchor=tk.W)
        #self.__tablaprospectos.column("curp", minwidth=0, width=90, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("empresa", text="Empresa", anchor=tk.W)
        self.__tablaprospectos.column("empresa", minwidth=0, width=80, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("telefono", text="Teléfono", anchor=tk.W)
        self.__tablaprospectos.column("telefono", minwidth=0, width=90, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("correo", text="Correo", anchor=tk.W)
        self.__tablaprospectos.column("correo", minwidth=0, width=144, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.heading("pais", text="País", anchor=tk.W)
        self.__tablaprospectos.column("pais", minwidth=0, width=85, stretch=NO, anchor=tk.W)
        self.__tablaprospectos.place(x=5, y=5, width=self.__ancho - 40, height=360)
        self.__cmbfiltro1.set("")
        self.__cmbfiltro2.set("")

        # lo blanco
        self.__framereportes.place(x=130, y=110)

    def filtrar(self,filtro1,filtro2):
        if filtro1 == "" or filtro2 == "":
            messagebox.showerror(message="Seleccione un filtro", title="ERROR")
        else:
            self.limpiartabla()
            prospectos = self.__sql.getprospectosby(filtro1,filtro2)
            if prospectos == None:
                messagebox.showinfo(message="No hay resistros en este filtro", title="Sin registros")
            else:
                registro = []
                for fila in prospectos:
                                #nombre #apapat #apmat   #tel      #empresa   #correo   #pai
                    registro = [fila[0], fila[3], fila[7], fila[8], fila[1], fila[2],fila[6], fila[9]]
                    self.__tablaprospectos.insert(parent="", index=0, values=registro)

    def limpiartabla(self):
        elementos = self.__tablaprospectos.get_children()
        for i in elementos:
            self.__tablaprospectos.delete(i)

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
        self.__logon = Image.open("./img/prospectos.png")
        self.__logon = self.__logon.resize((100, 100))
        self.__logon = ImageTk.PhotoImage(self.__logon)
        self.__lblimagen = tk.Label(self.__framebotones, image=self.__logon, width=100, height=100)
        self.__lblimagen.place(x=10, y=0)

        self.__btnaltas = tk.Button(self.__framebotones, bg="#565656", text="Altas", width=12, height=1,
                                    font=("Sora", 10), fg="#D3D3D3", command=lambda: self.operacion(self.altas, "a"))
        self.__btnaltas.place(x=10, y=130)

        self.__btnbajas = tk.Button(self.__framebotones, bg="#565656", text="Bajas", width=12, height=1,
                                    font=("Sora", 10), fg="#D3D3D3", command=lambda: self.operacion(self.bajas, "b"))
        self.__btnbajas.place(x=10, y=158)

        self.__btncambios = tk.Button(self.__framebotones, bg="#565656", text="Cambios", width=12, height=1,
                                      font=("Sora", 10), fg="#D3D3D3", command=lambda: self.operacion(self.cambios, "c"))
        self.__btncambios.place(x=10, y=186)

        self.__btnreportes = tk.Button(self.__framebotones, bg="#565656", text="Reportes", width=12, height=1,
                                       font=("Sora", 10), fg="#D3D3D3", command=lambda: self.operacion(self.reportes, "r"))
        self.__btnreportes.place(x=10, y=214)

        self.__framebotones.place(x=0, y=120)

    def clearall(self):
        if self.__lblimagennegado !=None:
            self.__lblimagennegado.destroy()
            self.__lblimagennegado=None
        if (self.__framecambios != None):
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
            if op=="r" or op=="a" or op=="c":
                funcion()
            else:
                self.negado()
        elif self.__nivel == 3:
            if op == "r" or op == "a" or op == "c":
                funcion()
            else:
                self.negado()
        else:
            self.negado()
