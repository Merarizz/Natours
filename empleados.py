import tkinter as tk
from tkinter import ttk, NO
import sql
from PIL import Image, ImageTk
from tkinter import messagebox
import  re
import datetime

class Empleado:

    def __init__(self, ventana, nivel):
        self.__sql = sql.SQL()
        self.__ancho = 1072
        self.__alto = 630
        self.__ventana = ventana
        self.__nivel=nivel
        self.__data= None
        self.__datacp= None
        paises= self.__sql.getpaises()
        self.__datapaises={}
        self.__framealtas= None
        self.__framebajas= None
        self.__framecambios= None
        self.__framereportes= None
        self.__framebotones= None
        self.__nuevocp=False
        self.__lblimagennegado=None

        self.__ojo = Image.open("./img/ojo.png")
        self.__ojo = self.__ojo.resize((15, 15))
        self.__ojo = ImageTk.PhotoImage(self.__ojo)
        self.__noojo = Image.open("./img/noojo.png")
        self.__noojo = self.__noojo.resize((15, 15))
        self.__noojo = ImageTk.PhotoImage(self.__noojo)
        self.__strvar = tk.StringVar()
        self.__strvar.trace("w",self.paisesonchange)
        self.__strvar1 = tk.StringVar()
        self.__strvar1.trace("w", self.filtroonchange)

        if paises != None:
            for fila in paises:
                self.__datapaises[fila[1]]= [fila[0],fila[2]]

    def paisesonchange(self, index,value, op):
        self.__nuevocp=False
        self.__txtprefijo.delete(0,tk.END)
        if self.__cmbpais.get() != "":
           self.__txtprefijo.insert(0,self.__datapaises[self.__cmbpais.get()][1])
        #print(self.__cmbpais.get())

    def filtroonchange(self, index, values, op):
        filtro1= self.__cmbfiltro1.get()
        self.__cmbfiltro2.set("")
        if filtro1 != "" :
            if filtro1 == "Estatus":
                self.__cmbfiltro2 ["values"] = ["Todos", "Activo", "Vacaciones", "Incapacidad", "Baja"]
            elif filtro1 == "Puesto":
                self.__cmbfiltro2 ["values"] = ["Todos", "Gerente", "Vendedor", "Asistente"]
            elif filtro1 == "Sueldo" :
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


        #formulario
        self.__framealtas=tk.Frame(self.__ventana,  bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framealtas, text="Alta de empleado", bg="#FFFFFF", width=self.__ancho-20, height=200,font=("Sora",10))
        self.__generallblFrm.place(x=10,y=10)

        #nombre
        lblnombre=tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Nombre(s): ",font=("Sora",10))
        lblnombre.place(x=10, y=20)
        self.__txtnombre=tk.Entry(self.__generallblFrm, width=23, font=("Sora",10))
        self.__txtnombre.place(x=10, y=40)

        #appat
        lblappat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido paterno: ", font=("Sora", 10))
        lblappat.place(x=250, y=20)
        self.__txtappat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtappat.place(x=250, y=40)

        #apmat
        lblapmat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido materno: ", font=("Sora", 10))
        lblapmat.place(x=490, y=20)
        self.__txtapmat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtapmat.place(x=490, y=40)

        # CURP
        lblcurp = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="CURP: ", font=("Sora", 10))
        lblcurp.place(x=10, y=70)
        self.__txtcurp = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtcurp.place(x=10, y=90)

        # NSS
        lblnss = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="NSS: ", font=("Sora", 10))
        lblnss.place(x=250, y=70)
        self.__txtnss = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtnss.place(x=250, y=90)

        # Puesto
        lblpuesto = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Puesto: ", font=("Sora", 10))
        lblpuesto.place(x=490, y=70)
        self.__cmbpuesto = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                values=["Gerente", "Vendedor", "Asistente"])
        self.__cmbpuesto.place(x=490, y=90)

        #estatus
        lblestatus= tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Estatus: ", font=("Sora", 10))
        lblestatus.place(x=730, y=70)
        self.__cmbestatus = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",values=["Activo", "Vacaciones", "Incapacidad", "Baja"])
        self.__cmbestatus.place(x=730, y=90)

        #sueldo
        lblsueldo= tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Sueldo: ", font=("Sora", 10))
        lblsueldo.place(x=10, y=120)
        self.__txtsueldo= tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtsueldo.place(x=10, y=140)

        # comision
        lblcomision = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Comision: ", font=("Sora", 10))
        lblcomision.place(x=250, y=120)
        lblcomision = tk.Label(self.__generallblFrm, bg="#A9A9A9", text="Porcentaje máx.: 50 ", font=("Sora", 10))
        lblcomision.place(x=340, y=120)
        self.__txtcomision = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtcomision.place(x=250, y=140)

        # fechainiico
        lblinicio = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Fecha inicio: ", font=("Sora", 10))
        lblinicio.place(x=490, y=120)
        lblinicio = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblinicio.place(x=580, y=120)
        self.__txtinicio = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtinicio.place(x=490, y=140)

        # fechafinal
        lblfinal = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Fecha final: ", font=("Sora", 10))
        lblfinal.place(x=730, y=120)
        lblifinal= tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblifinal.place(x=820, y=120)
        self.__txtfinal = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtfinal.place(x=730, y=140)
        lblopcional = tk.Label(self.__generallblFrm, bg="#A9A9A9", text="Opcional", font=("Sora", 10))
        lblopcional.place(x=840, y=140)


        self.__datoslblFrm = tk.LabelFrame(self.__framealtas, text="Datos Generales", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=230, font=("Sora", 10))
        self.__datoslblFrm.place(x=10, y=210)


        #país
        lblpais=tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="País: ", font=("Sora", 10))
        lblpais.place(x=10, y=20)
        self.__cmbpais = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10),textvar=self.__strvar, state="readonly", values=list(self.__datapaises.keys()))
        self.__cmbpais.place(x=10, y=40)


        # Prefijo
        lblprefijo= tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Lada: ", font=("Sora", 10))
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

        #calle
        lblcalle= tk.Label(self.__datoslblFrm,bg="#FFFFFF", text="Calle: ", font=("Sora", 10))
        lblcalle.place(x=10, y=70)
        lblcalle = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Seguridad", font=("Sora", 8))
        lblcalle.place(x=50, y=70)
        self.__txtcalle= tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtcalle.place(x=10, y=100)

        #numeroexterior
        lblnumex=tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Número exterior: ", font=("Sora", 10))
        lblnumex.place(x=250, y=70)
        lblnumex = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: 1234", font=("Sora", 8))
        lblnumex.place(x=355, y=70)
        self.__txtnumex = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
        self.__txtnumex.place(x=250,y=100)

        #numerointerior
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
        self.__btncp= tk.Button(self.__datoslblFrm, text="Buscar >>", width=10, command=self.getcp)
        self.__btncp.place (x=120, y=160)


        #colonia
        lblcolonia= tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Colonia: ", font=("Sora", 10))
        lblcolonia.place(x=250,y=130)
        lblcolonia = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Valle Campana", font=("Sora", 8))
        lblcolonia.place(x=320, y=130)
        self.__cmbcolonia = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), state="readonly")
        self.__cmbcolonia.place(x=250, y=160)
        self.__txtcolonia= tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10), state="disabled")
        self.__txtcolonia.place(x=250,y= 160)

        #ciudad
        lblciudad = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Ciudad: ", font=("Sora", 10))
        lblciudad.place(x=490, y=130)
        lblciudad = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: Monterrey", font=("Sora", 8))
        lblciudad.place(x=550, y=130)
        self.__txtciudad = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10), state="disabled")
        self.__txtciudad.place(x=490, y=160)

        #estado
        lblestado= tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Estado: ", font=("Sora", 10))
        lblestado.place(x=730, y=130)
        lblestado = tk.Label(self.__datoslblFrm, bg="#A9A9A9", text="Ejemplo: N.L", font=("Sora", 8))
        lblestado.place(x=800, y=130)
        self.__txtestado = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10), state="disabled")
        self.__txtestado.place(x=730, y=160)

        #pais

        self.__contrasenialblFrm = tk.LabelFrame(self.__framealtas, text="Contraseña", bg="#FFFFFF",
                                           width=self.__ancho - 20, height=120, font=("Sora", 10))
        self.__contrasenialblFrm.place(x=10, y=450)

        #contrasenia
        lblcontrasenia = tk.Label(self.__contrasenialblFrm, bg="#A9A9A9", text="8 caracteres, 1 mayúscula, 1 minúscula, 1 dígito, 1 simbolo(.,_-&$%/#@+*)",
                                  font=("Sora", 8))
        lblcontrasenia.place(x=10, y=10)

        lblcontrasenia = tk.Label(self.__contrasenialblFrm, bg="#FFFFFF", text="Contraseña: ", font=("Sora", 10))
        lblcontrasenia.place(x=10, y=35)
        self.__txtcontrasenia = tk.Entry(self.__contrasenialblFrm, width=30, font=("Sora", 10), show="*")
        self.__txtcontrasenia.place(x=10, y=65)

        self.__btnver= tk.Button(self.__contrasenialblFrm, image= self.__ojo, width=20, height=20, command=self.togglepass)
        self.__btnver.place(x=250, y=65)
        lblconfcontrasenia= tk.Label(self.__contrasenialblFrm, bg="#FFFFFF", text="Confirmar contraseña: ",font=("Sora",10))
        lblconfcontrasenia.place(x=300, y=35)
        self.__txtconfcontrasenia = tk.Entry(self.__contrasenialblFrm, width=30, font=("Sora", 10), show="*")
        self.__txtconfcontrasenia.place(x=300, y=65)
        self.__btnverconf = tk.Button(self.__contrasenialblFrm, image= self.__ojo, width=20, height=20, command=self.togglepassconf)
        self.__btnverconf.place(x=520, y=65)
        self.__visible=False
        self.__visibleconf= False

        #botones
        btnagregar=tk.Button(self.__framealtas, text="Agregar", bg="#00c800", width=20, command=self.insertarempleado)
        btnagregar.place (x=900, y=590)

        self.__cmbpais.set("")




        #lo blanco
        self.__framealtas.place(x=130, y=110)

    def getcp(self):
        if self.__txtcp.get()=="":
            messagebox.showerror(message="AGREGA UN CÓDIGO POSTAL", title="ERROR")
        elif self.__txtcp.get().isnumeric():
            self.__txtcolonia.config(state="normal")
            self.__txtciudad.config(state="normal")
            self.__txtestado.config(state="normal")
            self.__datacp = self.__sql.getcp(self.__txtcp.get())
            self.__txtciudad.delete(0, tk.END)
            self.__txtestado.delete(0, tk.END)
            if self.__datacp == None:
                messagebox.showinfo(message="No se encontro el código postal. Rellene los datos y estos se guardaran ", title="No se encontro")
                self.__nuevocp=True
                self.__txtcolonia = tk.Entry(self.__datoslblFrm, width=23, font=("Sora", 10))
                self.__txtcolonia.place(x=250, y=160)
            else:
                self.__nuevocp=False
                self.__txtciudad.insert(0,self.__datacp[0][3])
                self.__txtestado.insert(0, self.__datacp[0][4])
                listacolonias=[]
                for fila in self.__datacp:
                    listacolonias.append(fila[2])
                    print(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__cmbcolonia = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), state="readonly", values=listacolonias)
                self.__cmbcolonia.place(x=250, y=160)

        else:
            messagebox.showerror(message="EL CÓDIGO POSTAL DEBE SER NUMERICO", title="ERROR")
    def togglepass(self):
        if self.__visible:
            self.__txtcontrasenia.config(show="*")
            self.__btnver.config(image=self.__ojo)
        else:
            self.__txtcontrasenia.config(show="")
            self.__btnver.config(image=self.__noojo)
        self.__visible=not self.__visible

    def togglepassconf(self):
        if self.__visibleconf:
            self.__txtconfcontrasenia.config(show="*")
            self.__btnverconf.config(image=self.__ojo)
        else:
            self.__txtconfcontrasenia.config(show="")
            self.__btnverconf.config(image=self.__noojo)
        self.__visibleconf=not self.__visibleconf

    def validanumeros(self):
        if self.__txtnss.get().isnumeric()  and self.__txtnumex.get().isnumeric() and self.__txtcp.get().isnumeric():
            regex = '[+-]?[0-9]+\.[0-9]+'
            if (re.search(regex, self.__txtsueldo.get()) or self.__txtsueldo.get().isnumeric()) and  (re.search(regex, self.__txtcomision.get()) or self.__txtcomision.get().isnumeric()):
                return True
            else:
                messagebox.showerror(
                    message="EL CAMPO DEBE SER NUMERICO O DECIMAL", title="ERROR")
                return False
        else:
            messagebox.showerror(
                message="EL CAMPO DEBE SER NUMÉRICO", title="ERROR")
            return False



    def insertarempleado(self):

        if self.validavacios() :

            if self.__txtcontrasenia.get() == self.__txtconfcontrasenia.get() and self.validacontrasenia():
                if self.validafecha(self.__txtinicio.get()) and (self.__txtfinal.get()=="" or self.validafecha(self.__txtfinal.get())  and self.validanumeros()):

                    if self.__nuevocp:
                        pais= self.__sql.getidpais(self.__cmbpais.get())
                        datos=[self.__txtcp.get(), self.__txtcolonia.get(), self.__txtciudad.get(), self.__txtestado.get(), pais]
                        self.__sql.insertarcp(datos)
                        messagebox.showinfo(message="SE AGREGÓ UN NUEVO REGISTRO AL CÓDIGO POSTAL", title="REGISTRO EXITOSO")

                    cp=self.__sql.getcpid(self.__txtcp.get(), self.__txtcolonia.get())

                    datos = [self.__txtcalle.get(), self.__txtnumex.get(), self.__txtnumint.get(), cp]
                    self.__sql.insertardireccion(datos)
                    nuevonivel= 3
                    if self.__cmbpuesto.get()=="Gerente":
                        nuevonivel=1
                    elif self.__cmbpuesto.get()=="Vendedor":
                        nuevonivel=2
                    iddireccion=self.__sql.ultimoiddireccion()

                    datos= [self.__txtnombre.get(), self.__txtappat.get(), self.__txtapmat.get(), self.__txtcurp.get(), self.__txtnss.get(),
                            self.__txttel.get(), iddireccion, self.__cmbpuesto.get(), nuevonivel, self.__txtemail.get(), self.__txtcontrasenia.get(),
                            self.__txtsueldo.get(), self.__txtcomision.get(), self.__txtinicio.get(), self.__cmbestatus.get()]
                    final= False
                    if self.__txtfinal.get() != "":
                        datos.append( self.__txtfinal.get())
                        final= True
                    self.__sql.insertarempleado(datos, final)
                    messagebox.showinfo(message="GUARDADO CORRECTAMENTE", title="REGISTRO EXITOSO")
                    self.__framealtas.destroy()
                    self.altas()

            else:
                messagebox.showerror(
                    message="LAS CONTRASEÑAS NO COINCIDEN O LA CONTRASEÑA NO TIENE EL FORMATO CORRECTO", title="ERROR")

        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")



    def bajas(self):
        self.actualizabotones("bajas")

        # formulario
        self.__framebajas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framebajas, text="Baja empleado", bg="#FFFFFF", width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)



        #empleado
        lblempleado= tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Empleado: ", font=("Sora", 10))
        lblempleado.place(x=50, y=10)

        self.__data = self.__sql.getempleados()
        listaempleados= []
        if self.__data != None:
            for fila in self.__data:
                empleado = fila [2] + " " + fila [3] + " " + fila [1]
                listaempleados.append(empleado)


        # empleados
        cmbempleados = ttk.Combobox(self.__generallblFrm, width=40, font=("Sora", 10), state="readonly", values= listaempleados)
        cmbempleados.place(x=120, y=10)

        btnseleccionar = tk.Button(self.__generallblFrm, text="Seleccionar", bg="#565656", width=20,fg="#D3D3D3", command= lambda: self.detallesempleado(cmbempleados.get()))

        btnseleccionar.place(x=480, y=10)


        self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20, height=350)
        self.__framedatos.place(x=10, y=80)



        # botones

        btneliminar = tk.Button(self.__framebajas, text="Eliminar", bg="#800000",width=20,fg="#D3D3D3",command=lambda : self.eliminarempleado(cmbempleados.get()))
        btneliminar.place(x=900, y=590)


        # lo blanco
        self.__framebajas.place(x=130, y=110)

    def eliminarempleado(self, nombre):

        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún empleado", title="ERROR")
        else:


            lista = nombre.split()
            # empleado
            empleado = [fila for fila in self.__data if
                        lista[0] == fila[2] and lista[1] == fila[3] and lista[2] == fila[1]]
            id_empleado= empleado[0][0]
            id_direccion= empleado[0][7]
            self.__sql.eliminarempleado(id_empleado)
            self.__sql.eliminardireccion(id_direccion)
            messagebox.showinfo(message="El empleado se elimino correctamente.", title="Registro eliminado")
            self.__framebajas.destroy()
            self.bajas()
    def detallesempleado (self, nombre):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún empleado", title="ERROR")
        else:
            self.__framedatos.destroy()
            self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20,
                                              height=450)
            self.__framedatos.place(x=10, y=80)

            lista= nombre.split()

            #empleado
            empleado= [fila for fila in self.__data if lista[0] == fila [2] and lista[1] == fila[3] and lista[2] == fila[1]]
            #print(empleado, type(empleado))
            lblnombre= tk.Label(self.__framedatos, bg="#FFFFFF", text="Nombre: ", font=("Sora", 10))
            lblnombre.place(x=5, y=5)
            lblnombrevalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=nombre, font=("Sora", 10))
            lblnombrevalor.place(x=80, y=5)

            #curp
            lblcurp = tk.Label(self.__framedatos, bg="#FFFFFF", text="Curp: ", font=("Sora", 10))
            lblcurp.place(x=5, y=25)
            lblcurpvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][4], font=("Sora", 10))
            lblcurpvalor.place(x=80, y=25)

            #NSS
            lblnss = tk.Label(self.__framedatos, bg="#FFFFFF", text="Nss: ", font=("Sora", 10) )
            lblnss.place(x=5, y=45)
            lblnssvalor = tk.Label(self.__framedatos,  bg="#FFFFFF", text=empleado[0][5], font=("Sora", 10))
            lblnssvalor.place(x=80, y=45)

            #telefono
            lbltelefono = tk.Label (self.__framedatos, bg="#FFFFFF", text="Teléfono: ", font=("Sora", 10))
            lbltelefono.place(x=5, y=65)
            telefono= "+ " + str(empleado[0][30]) + " " + str(empleado[0][6])
            lbltelefonovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=telefono, font=("Sora", 10))
            lbltelefonovalor.place(x=80, y=65)



            #puesto
            lblpuesto = tk.Label(self.__framedatos, bg="#FFFFFF", text="Puesto: ", font=("Sora", 10))
            lblpuesto.place(x=5, y=85)
            lblpuestovalor = tk.Label(self.__framedatos,  bg="#FFFFFF", text=empleado[0][8], font=("Sora", 10))
            lblpuestovalor.place(x=80, y=85)

            #correo
            lblcorreo = tk.Label(self.__framedatos, bg="#FFFFFF", text="Correo: ", font=("Sora", 10))
            lblcorreo.place(x=5, y=105)
            lblcorreovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][10], font=("Sora", 10))
            lblcorreovalor.place(x=80, y=105)

            # sueldo
            lblsueldo = tk.Label(self.__framedatos, bg="#FFFFFF", text="Sueldo: ", font=("Sora", 10))
            lblsueldo.place(x=5, y=125)
            lblsueldovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][12], font=("Sora", 10))
            lblsueldovalor.place(x=80, y=125)

            # comision
            lblcomision = tk.Label(self.__framedatos, bg="#FFFFFF", text="Comisión %", font=("Sora", 10))
            lblcomision.place(x=5, y=145)
            lblcomisionvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][13], font=("Sora", 10))
            lblcomisionvalor.place(x=80, y=145)

            # estatus
            lblestatus = tk.Label(self.__framedatos, bg="#FFFFFF", text="Estatus: ", font=("Sora", 10))
            lblestatus.place(x=5, y=165)
            lblestatusvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][16], font=("Sora", 10))
            lblestatusvalor.place(x=80, y=165)



            #direcciones



            #calle
            lblcalle = tk.Label(self.__framedatos, bg="#FFFFFF", text="Calle: ", font=("Sora", 10))
            lblcalle.place(x=5, y=185)
            lblcallevalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][18], font=("Sora", 10))
            lblcallevalor.place(x=80, y=185)

            #no_exterior
            lblexterior = tk.Label(self.__framedatos, bg="#FFFFFF", text="No. exterior: ", font=("Sora", 10))
            lblexterior.place(x=5, y=205)
            lblexteriorvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][19], font=("Sora", 10))
            lblexteriorvalor.place(x=80, y=205)

            # no_interior
            lblinterior = tk.Label(self.__framedatos, bg="#FFFFFF", text="No. interior: ", font=("Sora", 10))
            lblinterior.place(x=5, y=225)
            lblinteriorvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][20], font=("Sora", 10))
            lblinteriorvalor.place(x=80, y=225)

            #colonia
            lblcolonia = tk.Label(self.__framedatos, bg="#FFFFFF", text="Colonia:", font=("Sora", 10))
            lblcolonia.place(x=5, y=245)
            lblcoloniavalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][24], font=("Sora", 10))
            lblcoloniavalor.place(x=80, y=245)

            #cp
            lblcp= tk.Label(self.__framedatos, bg="#FFFFFF", text="Cp:", font=("Sora", 10))
            lblcp.place(x=5, y=265)
            lblcpvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][23], font=("Sora", 10))
            lblcpvalor.place(x=80, y=265)

            #ciudad
            lblciudad = tk.Label(self.__framedatos, bg="#FFFFFF", text="Ciudad:", font=("Sora", 10))
            lblciudad.place(x=5, y=285)
            lblciudadvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][25], font=("Sora", 10))
            lblciudadvalor.place(x=80, y=285)

            #estado
            lblestado = tk.Label(self.__framedatos, bg="#FFFFFF", text="Estado:", font=("Sora", 10))
            lblestado.place(x=5, y=305)
            lblestadovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][26], font=("Sora", 10))
            lblestadovalor.place(x=80, y=305)

            #pais
            lblpais = tk.Label(self.__framedatos, bg="#FFFFFF", text="País:", font=("Sora", 10))
            lblpais.place(x=5, y=325)
            lblpaisvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=empleado[0][29], font=("Sora", 10))
            lblpaisvalor.place(x=80, y=325)



    def muestradatos(self, nombre=""):
        if nombre == "":
            messagebox.showerror(message="No se selecciono ningún empleado", title="ERROR")
        self.cambios(nombre)
    def cambios(self, nombre=""):

        self.actualizabotones("cambios")

        # formulario
        self.__framecambios = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)
        self.__seleccionlblFrm = tk.LabelFrame(self.__framecambios, text="", bg="#FFFFFF",
                                               width=self.__ancho - 20, height=40, font=("Sora", 10))
        self.__seleccionlblFrm.place(x=10, y=5)

        self.__data = self.__sql.getempleados()
        listaempleados = []
        if (self.__data != None):
            for fila in self.__data:
                empleado = fila[2] + " " + fila[3] + " " + fila[1]
                listaempleados.append(empleado)

        # combo para seleccionar el empleado
        lblempleado = tk.Label(self.__seleccionlblFrm, bg="#FFFFFF", text="Empleado: ", font=("Sora", 10))
        lblempleado.place(x=50, y=10)
        self.__cmbempleado = ttk.Combobox(self.__seleccionlblFrm, width=40, font=("Sora", 10), state="readonly",
                                  values=listaempleados)
        self.__cmbempleado.place(x=120, y=10)
        btnseleccionar = tk.Button(self.__seleccionlblFrm, text="Seleccionar", bg="#565656", width=20,fg="#D3D3D3",
                                   command=lambda: self.muestradatos(self.__cmbempleado.get()))
        btnseleccionar.place(x=445, y=8)

        #formulario
        self.__generallblFrm = tk.LabelFrame(self.__framecambios, text="Editar empleado", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=200, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=50)

        # nombre
        lblnombre = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Nombre(s): ", font=("Sora", 10))
        lblnombre.place(x=10, y=20)
        self.__txtnombre = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtnombre.place(x=10, y=40)

        # appat
        lblappat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido paterno: ", font=("Sora", 10))
        lblappat.place(x=250, y=20)
        self.__txtappat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtappat.place(x=250, y=40)

        # apmat
        lblapmat = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Apellido materno: ", font=("Sora", 10))
        lblapmat.place(x=490, y=20)
        self.__txtapmat = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtapmat.place(x=490, y=40)

        # CURP
        lblcurp = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="CURP: ", font=("Sora", 10))
        lblcurp.place(x=10, y=70)
        self.__txtcurp = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtcurp.place(x=10, y=90)

        # NSS
        lblnss = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="NSS: ", font=("Sora", 10))
        lblnss.place(x=250, y=70)
        self.__txtnss = tk.Entry(self.__generallblFrm, width=23, font=("Sora", 10))
        self.__txtnss.place(x=250, y=90)

        # Puesto
        lblpuesto = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Puesto: ", font=("Sora", 10))
        lblpuesto.place(x=490, y=70)
        self.__cmbpuesto = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                        values=["Gerente", "Vendedor", "Asistente"])
        self.__cmbpuesto.place(x=490, y=90)

        # estatus
        lblestatus = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Estatus: ", font=("Sora", 10))
        lblestatus.place(x=730, y=70)
        self.__cmbestatus = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                         values=["Activo", "Vacaciones", "Incapacidad", "Baja"])
        self.__cmbestatus.place(x=730, y=90)

        # sueldo
        lblsueldo = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Sueldo: ", font=("Sora", 10))
        lblsueldo.place(x=10, y=120)
        self.__txtsueldo = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtsueldo.place(x=10, y=140)

        # comision
        lblcomision = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Comision: ", font=("Sora", 10))
        lblcomision.place(x=250, y=120)
        lblcomision = tk.Label(self.__generallblFrm, bg="#A9A9A9", text="Porcentaje máx.: 50 ", font=("Sora", 10))
        lblcomision.place(x=340, y=120)
        self.__txtcomision = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtcomision.place(x=250, y=140)

        # fechainiico
        lblinicio = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Fecha inicio: ", font=("Sora", 10))
        lblinicio.place(x=490, y=120)
        lblinicio = tk.Label(self.__generallblFrm, bg="#A9A9A9", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblinicio.place(x=580, y=120)
        self.__txtinicio = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtinicio.place(x=490, y=140)

        # fechafinal
        lblfinal = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Fecha final: ", font=("Sora", 10))
        lblfinal.place(x=730, y=120)
        lblifinal = tk.Label(self.__generallblFrm, bg="#A9A9A9", text="Formato: aaaa-mm-dd", font=("Sora", 8))
        lblifinal.place(x=820, y=120)
        self.__txtfinal = tk.Entry(self.__generallblFrm, width=23, font=("sora", 10))
        self.__txtfinal.place(x=730, y=140)
        lblopcional=tk.Label(self.__generallblFrm, bg="#A9A9A9", text="Opcional", font=("Sora", 10))
        lblopcional.place(x=840, y=140)

        self.__datoslblFrm = tk.LabelFrame(self.__framecambios, text="Datos Generales", bg="#FFFFFF",
                                           width=self.__ancho - 20, height=230, font=("Sora", 10))
        self.__datoslblFrm.place(x=10, y=250)

        # país
        lblpais = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="País: ", font=("Sora", 10))
        lblpais.place(x=10, y=20)
        self.__cmbpais = ttk.Combobox(self.__datoslblFrm, width=20, font=("Sora", 10), textvar=self.__strvar, state="readonly", values=list(self.__datapaises.keys()))
        self.__cmbpais.place(x=10, y=40)

        # Prefijo
        lblprefijo = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Lada: ", font=("Sora", 10))
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

        self.__contrasenialblFrm = tk.LabelFrame(self.__framecambios, text="Contraseña", bg="#FFFFFF",
                                                 width=self.__ancho - 20, height=120, font=("Sora", 10))
        self.__contrasenialblFrm.place(x=10, y=490)

        # contrasenia
        lblcontrasenia = tk.Label(self.__contrasenialblFrm, bg="#A9A9A9",
                                  text="8 caracteres, 1 mayúscula, 1 minúscula, 1 dígito, 1 simbolo(.,_-&$%/#@+*)",
                                  font=("Sora", 8))
        lblcontrasenia.place(x=10, y=10)

        lblcontrasenia = tk.Label(self.__contrasenialblFrm, bg="#FFFFFF", text="Contraseña: ", font=("Sora", 10))
        lblcontrasenia.place(x=10, y=35)
        self.__txtcontrasenia = tk.Entry(self.__contrasenialblFrm, width=30, font=("Sora", 10), show="*")
        self.__txtcontrasenia.place(x=10, y=65)
        self.__btnver = tk.Button(self.__contrasenialblFrm, image=self.__ojo, width=20, height=20,command=self.togglepass)
        self.__btnver.place(x=250, y=65)
        lblconfcontrasenia = tk.Label(self.__contrasenialblFrm, bg="#FFFFFF", text="Confirmar contraseña: ",
                                      font=("Sora", 10))
        lblconfcontrasenia.place(x=300, y=35)
        self.__txtconfcontrasenia = tk.Entry(self.__contrasenialblFrm, width=30, font=("Sora", 10), show="*")
        self.__txtconfcontrasenia.place(x=300, y=65)

        #####################################
        self.__btnverconf = tk.Button(self.__contrasenialblFrm, image=self.__ojo, width=20, height=20,
                                      command=self.togglepassconf)
        self.__btnverconf.place(x=520, y=65)
        self.__visible = False
        self.__visibleconf = False
        ########################################

        param1 = ""
        param2 = ""
        param3= ""
        param4= ""


        if nombre != "":
            lista = nombre.split()
            # empleado
            actual = [fila for fila in self.__data if lista[0] == fila[2] and lista[1] == fila[3] and lista[2] == fila[1]]
            self.__cmbempleado.set(nombre)
            self.__txtnombre.insert(0, actual[0][1])
            self.__txtappat.insert(0,actual[0][2])
            self.__txtapmat.insert(0, actual[0][3])
            self.__txtcurp.insert(0, actual[0][4])
            self.__txtnss.insert(0, actual[0][5])
            self.__txttel.insert(0, actual[0][6])
            self.__cmbpuesto.set(actual[0][8])
            self.__txtemail.insert(0, actual[0][10])
            self.__txtcontrasenia.insert(0, actual[0][11])
            self.__txtsueldo.insert(0, actual[0][12])
            self.__txtcomision.insert(0, actual[0][13])
            self.__txtinicio.insert(0, actual[0][14])
            if actual [0][15]==None :
                self.__txtfinal.insert(0, "")
            else:
                self.__txtfinal.insert(0, actual[0][15])
            self.__cmbestatus.set( actual[0][16])
            self.__txtcalle.insert(0, actual[0][18])
            self.__txtnumex.insert(0, actual[0][19])
            self.__txtnumint.insert(0, actual[0][20])
            self.__txtcp.insert(0, actual[0][23])
            self.__txtcolonia.insert(0, actual[0][24])
            self.__cmbcolonia.set(actual[0][24])
            self.__txtciudad.insert(0, actual[0][25])
            self.__txtestado.insert(0, actual[0][26])
            self.__cmbpais.set( actual[0][29])
            self.__txtprefijo.insert(0, actual[0][30])
            param1 = actual[0][0] #id_empelado
            param2 = actual[0][7] #id_direccion
            param3= actual[0][21] #id_cp
            param4= actual[0][27] #id_pais


        btneditar = tk.Button(self.__framecambios, text="Editar ", bg="#00c800", width=20, command= lambda: self.cambiosempleados(param1, param2, param3, param4))
        btneditar.place(x=900, y=590)

        if nombre == "":
            self.__cmbpais.set("")


        # lo blanco
        self.__framecambios.place(x=130, y=110)

    def cambiosempleados(self, id_empleado, id_direccion, id_cp, id_pais):


        if self.validavacios() and self.__cmbempleado.get() != "":

            if  self.__txtcontrasenia.get() == self.__txtconfcontrasenia.get() and self.validacontrasenia():
                if self.validafecha(self.__txtinicio.get()) and (self.__txtfinal.get()=="" or self.validafecha(self.__txtfinal.get())  and self.validanumeros()):

                    if self.__nuevocp:
                        datos=[self.__txtcp.get(), self.__txtcolonia.get(), self.__txtciudad.get(), self.__txtestado.get(), id_pais]
                        self.__sql.insertarcp(datos)
                        messagebox.showinfo(message="SE AGREGÓ UN NUEVO REGISTRO AL CÓDIGO POSTAL", title="REGISTRO EXITOSO")

                    cp=self.__sql.getcpid(self.__txtcp.get(), self.__txtcolonia.get())

                    datos = [self.__txtcalle.get(), self.__txtnumex.get(), self.__txtnumint.get(), cp, id_direccion]
                    self.__sql.editardireccion(datos)
                    nuevonivel= 3
                    if self.__cmbpuesto.get()=="Gerente":
                        nuevonivel=1
                    elif self.__cmbpuesto.get()=="Vendedor":
                        nuevonivel=2

                    datos= [self.__txtnombre.get(), self.__txtappat.get(), self.__txtapmat.get(), self.__txtcurp.get(), self.__txtnss.get(),
                            self.__txttel.get(), id_direccion, self.__cmbpuesto.get(), nuevonivel, self.__txtemail.get(), self.__txtcontrasenia.get(),
                            self.__txtsueldo.get(), self.__txtcomision.get(), self.__txtinicio.get(), self.__cmbestatus.get()]
                    final= False
                    if self.__txtfinal.get() != "":
                        datos.append( self.__txtfinal.get())
                        final= True
                    datos.append(id_empleado)
                    self.__sql.editarempleado(datos, final)
                    messagebox.showinfo(message="MODIFICADO CORRECTAMENTE", title="REGISTO EXITOSO")
                    self.__framecambios.destroy()
                    self.cambios()


            else:
                messagebox.showerror(message="LAS CONTRASEÑAS NO COINCIDEN", title="ERROR")

        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")


    def validafecha(self,fecha):
        fechaok=True
        listfecha = fecha.split("-")
        if len(listfecha) == 3:
            if len(listfecha[0]) == 4 and len(listfecha[1]) == 2 and len(listfecha[2]) == 2 and listfecha[0].isnumeric() \
                and listfecha[1].isnumeric() and listfecha[2].isnumeric():
                anio=int(listfecha[0])
                mes=int(listfecha[1])
                dia=int(listfecha[2])
                if not (anio>= 2024 and anio<=datetime.datetime.now().year):
                    messagebox.showerror(message="Año no válido", title="ERROR")
                    fechaok=False
                if not (mes>=1 and mes<=12):
                    messagebox.showerror(message="Mes no válido", title="ERROR")
                    fechaok = False
                if not (dia>=1 and dia<=31):
                    messagebox.showerror(message="Día no válido", title="ERROR")
                    fechaok = False
            else:
                messagebox.showerror(message="Formato de fecha no válido", title="ERROR")
                fechaok = False
        else:
            messagebox.showerror(message="Formato de fecha no válido", title="ERROR")
            fechaok = False
        return fechaok
    def validavacios(self):
        if not self.__nuevocp:
            self.__txtcolonia.delete(0,tk.END)
            self.__txtcolonia.insert(0,self.__cmbcolonia.get())
        if self.__txtnombre.get() == "" or self.__txtappat.get() == "" or self.__txtapmat == "" or self.__txtcurp.get() == "" or self.__txtnss == "" \
                or self.__txttel.get() == "" or self.__cmbpuesto.get() == "" or self.__cmbestatus.get() =="" or self.__txtemail.get() == "" \
                or self.__txtsueldo.get() == "" or self.__txtcomision.get() == "" or self.__txtcontrasenia.get() == ""\
                or self.__txtcalle.get() == "" or self.__txtnumex.get() == "" or self.__txtcolonia.get() == "" or self.__txtcp.get() == "" \
                or self.__cmbpais.get() == "" or self.__txtprefijo.get() == "" or self.__txtinicio.get() == ""\
                 or self.__txtciudad.get() == "" or self.__txtestado == "":
            return False
        else:
            return True

    def validacontrasenia(self):
        if len (self.__txtcontrasenia.get()) >= 8 and len (self.__txtcontrasenia.get())<=10:
            digito= re.compile(r'\d+')
            mayus=re.compile(r'[A-Z]+')
            minus = re.compile(r'[a-z]+')
            sim= ['.','_','&','$','%','/','#','@','+','*']
            pattern = f"[{re.escape(''.join(sim))}]"
            validar=[digito, mayus, minus]
            ok=True
            for validacion in validar :
                if not validacion.search(self.__txtcontrasenia.get()):
                    ok=False
                    print("Fallo", validacion)
            ok = ok and re.search(pattern, self.__txtcontrasenia.get())
            print("El resultado despues de los simbolos", ok)
            return ok
        else:
            return False
    def reportes(self):
        self.actualizabotones("reportes")

        # formulario
        self.__framereportes = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framereportes, text="Filtros:", bg="#FFFFFF", width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # empleado
        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)

        self.__data = self.__sql.getempleados()
        listaempelados = []
        if self.__data != None:
            for fila in self.__data:
                empleado = fila[2] + " " + fila[3] + " " + fila[1]
                listaempelados.append(empleado)

        # empleados
        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly", textvar=self.__strvar1,
                                    values=["Puesto", "Estatus", "Sueldo", "Comision", "Pais"])
        self.__cmbfiltro1.place(x=80, y=10)

        self.__cmbfiltro2 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                  values=[""])
        self.__cmbfiltro2.place(x=260, y=10)


        btnfiltrar = tk.Button(self.__generallblFrm, text="Filtrar", bg="#565656", width=20, fg="#D3D3D3",
                                   command=lambda: self.filtrar(self.__cmbfiltro1.get(), self.__cmbfiltro2.get()))
        btnfiltrar.place(x=480, y=5)

        self.__framedatos = tk.LabelFrame(self.__framereportes, text="Reporte", bg="#FFFFFF", width=self.__ancho - 20, height=400)
        self.__framedatos.place(x=10, y=80)

        self.__tablaempleados = ttk.Treeview(self.__framedatos,
                                           columns=("#", "Nombre", "appat", "apmat", "curp", "telefono", "estatus","puesto", "sueldo", "comision","correo", "pais"), show="headings")

        self.__tablaempleados.heading("#", text="Id", anchor=tk.W)
        self.__tablaempleados.column("#", minwidth=0, width=20, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("Nombre", text="Nombre", anchor=tk.W)
        self.__tablaempleados.column("Nombre", minwidth=0, width=85, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("appat", text="Paterno", anchor=tk.W)
        self.__tablaempleados.column("appat", minwidth=0, width=85, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("apmat", text="Materno", anchor=tk.W)
        self.__tablaempleados.column("apmat", minwidth=0, width=85, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("curp", text="Curp", anchor=tk.W)
        self.__tablaempleados.column("curp", minwidth=0, width=90, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("telefono", text="Teléfono", anchor=tk.W)
        self.__tablaempleados.column("telefono", minwidth=0, width=110, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("estatus", text="Estatus", anchor=tk.W)
        self.__tablaempleados.column("estatus", minwidth=0, width=90, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("sueldo", text="Sueldo", anchor=tk.W)
        self.__tablaempleados.column("sueldo", minwidth=0, width=90, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("comision", text="Comisión", anchor=tk.W)
        self.__tablaempleados.column("comision", minwidth=0, width=65, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("puesto", text="Puesto", anchor=tk.W)
        self.__tablaempleados.column("puesto", minwidth=0, width=65, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("correo", text="Correo", anchor=tk.W)
        self.__tablaempleados.column("correo", minwidth=0, width=127, stretch=NO, anchor=tk.W)
        self.__tablaempleados.heading("pais", text="País", anchor=tk.W)
        self.__tablaempleados.column("pais", minwidth=0, width=90, stretch=NO, anchor=tk.W)
        self.__tablaempleados.place(x=5, y=5, width=self.__ancho - 40, height=360)
        self.__cmbfiltro1.set("")
        self.__cmbfiltro2.set("")

        # lo blanco
        self.__framereportes.place(x=130, y=110)

    def filtrar(self,filtro1,filtro2):
        if filtro1 == "" or filtro2 == "":
            messagebox.showerror(message="Seleccione un filtro", title="ERROR")
        else:
            self.limpiartabla()
            empleados = self.__sql.getempleadoby(filtro1,filtro2)
            if empleados == None:
                messagebox.showinfo(message="No hay valores en este filtro", title="Sin registros")
            else:
                registro = []
                for fila in empleados:
                    registro = [fila[0], fila[1], fila[2], fila[3], fila[4], fila[6], fila[16], fila[8], "$" + str(fila[12]), str(fila[13]) + "%", fila[10], fila[17]]
                    self.__tablaempleados.insert(parent="", index=0, values=registro)

    def limpiartabla(self):
        elementos = self.__tablaempleados.get_children()
        for i in elementos:
            self.__tablaempleados.delete(i)

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
        self.__logon = Image.open("./img/empleados.png")
        self.__logon = self.__logon.resize((100, 100))
        self.__logon = ImageTk.PhotoImage(self.__logon)
        self.__lblimagen = tk.Label(self.__framebotones, image=self.__logon, width=100, height=100)
        self.__lblimagen.place(x=10, y=0)

        self.__btnaltas = tk.Button(self.__framebotones, bg="#565656", text="Altas", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.altas))
        self.__btnaltas.place(x=10, y=130)

        self.__btnbajas = tk.Button(self.__framebotones, bg="#565656", text="Bajas", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.bajas))
        self.__btnbajas.place(x=10, y=158)

        self.__btncambios = tk.Button(self.__framebotones, bg="#565656", text="Cambios", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.cambios))
        self.__btncambios.place(x=10, y=186)

        self.__btnreportes = tk.Button(self.__framebotones, bg="#565656", text="Reportes", width=12, height=1, font=("Sora", 10),fg="#D3D3D3", command=lambda: self.operacion(self.reportes))
        self.__btnreportes.place(x=10, y=214)

        self.__framebotones.place(x=0, y=120)

    def clearall(self):
        if self.__lblimagennegado  != None:
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

    def operacion(self, funcion):
        self.clearall()
        if self.__nivel==1:
            funcion()
        else:
            self.negado()