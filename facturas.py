import tkinter as tk
from tkinter import ttk, DISABLED, NO
import datetime
import sql
from tkinter import messagebox
from PIL import Image, ImageTk


# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors

class Factura:

    def __init__(self, ventana, nivel):
        self.__ancho = 1072
        self.__alto = 630
        self.__ventana = ventana
        self.__nivel = nivel
        self.__framealtas = None
        self.__framebajas = None
        self.__framefactura = None
        self.__framereportes = None
        self.__framebotones = None
        self.__sql = sql.SQL()
        self.__dataclientes = None
        self.__dataempleados = None
        self.__dataservicios = None
        self.__data = None
        self.__total = 0.0
        self.__strvar1 = tk.StringVar()
        self.__strvar1.trace("w", self.filtroonchange)
        clientes=self.__sql.getclientes()
        self.__dictclientes={}
        empleados=self.__sql.getempleados()
        self.__dictempleados={}
        self.__lblimagennegado=None

        if clientes != None:
            for fila in clientes:
                nombre = "" + fila[1] + " " + fila[2] + " " + fila[3]
                self.__dictclientes[nombre]= fila[0]

        if empleados != None:
            for fila in empleados:
                nombre="" + fila[1] + " " + fila[2] + " " + fila[3]
                self.__dictempleados[nombre]= fila[0]

        #"Status", "Cliente", "Empleado", "Fecha", "Total"
    def filtroonchange(self, index, values, op):
        filtro1= self.__cmbfiltro1.get()
        self.__cmbfiltro2.set("")
        if filtro1 != "" :
            if filtro1 == "Status":
                self.__cmbfiltro2 ["values"] = ["Todos","Activa", "Cancelada"]
            elif filtro1 == "Cliente" :
                self.__cmbfiltro2 ["values"] =  ["Todos"] + list(self.__dictclientes.keys())
            elif filtro1 == "Empleado" :
                self.__cmbfiltro2 ["values"] = ["Todos"] + list(self.__dictempleados.keys())
            elif filtro1== "Fecha":
                self.__cmbfiltro2 ["values"] = ["Todos", "2024", "2023", "2022", "2021", "2020"]
            else:
                self.__cmbfiltro2 ["values"] = ["Todos", "0-9999", "10000-49999", "50000-99999", "100000-máx"]

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

    def actualizabotones(self, subseccion):
        self.__btnaltas.config(bg="#565656", fg="#FFFFFF")
        self.__btncanceladas.config(bg="#565656", fg="#FFFFFF")
        self.__btnreportes.config(bg="#565656", fg="#FFFFFF")

        if subseccion== "altas":
            self.__btnaltas.config(bg="#DAA520", fg="#000000")
        elif subseccion== "bajas":
            self.__btncanceladas.config(bg="#DAA520", fg="#000000")
        elif subseccion == "reportes":
            self.__btnreportes.config(bg="#DAA520", fg="#000000")


    def altas(self):
        self.actualizabotones("altas")

        self.__framealtas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framealtas, text="Nueva factura", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=90, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=5)

        self.__dataclientes = self.__sql.getclientes()
        listaclientes = []
        if (self.__dataclientes != None):
            for fila in self.__dataclientes:
                cliente = fila[2] + " " + fila[3] + " " + fila[1]
                listaclientes.append(cliente)

        # cliente
        lblcliente = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Cliente:", font=("Sora", 11))
        lblcliente.place(x=10, y=5)
        self.__cmbcliente = ttk.Combobox(self.__generallblFrm, width=30, values=listaclientes, state="readonly")
        self.__cmbcliente.place(x=100, y=5)

        self.__dataempleados = self.__sql.getempleados()
        listaempleados = []
        if (self.__dataempleados != None):
            for fila in self.__dataempleados:
                empleado = fila[2] + " " + fila[3] + " " + fila[1]
                listaempleados.append(empleado)

        # empleado
        lblempleado = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Empleado: ", font=("Sora", 11))
        lblempleado.place(x=10, y=40)
        self.__cmbempleado = ttk.Combobox(self.__generallblFrm, width=30, values=listaempleados, state="readonly")
        self.__cmbempleado.place(x=100, y=40)

        fecha = datetime.date.today()
        anio = fecha.year
        dia = fecha.day
        mes = fecha.month

        # dia
        lbldia = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Día:", font=("Sora", 11))
        lbldia.place(x=350, y=5)
        self.__txtdia = tk.Entry(self.__generallblFrm, width=10, font=("Sora", 10))
        self.__txtdia.place(x=350, y=40)
        self.__txtdia.insert(0, dia)
        self.__txtdia.config(state="readonly")

        # mes
        lblmes = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mes:", font=("Sora", 11))
        lblmes.place(x=450, y=5)
        self.__txtmes = tk.Entry(self.__generallblFrm, width=15, font=("Sora", 10))
        self.__txtmes.place(x=450, y=40)
        self.__txtmes.insert(0, self.nombremes(mes))
        self.__txtmes.config(state="readonly")

        # año
        lblanio = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Año:", font=("Sora", 11))
        lblanio.place(x=600, y=5)
        self.__txtanio = tk.Entry(self.__generallblFrm, width=10, font=("Sora", 10))
        self.__txtanio.place(x=600, y=40)
        self.__txtanio.insert(0, anio)
        self.__txtanio.config(state="readonly")

        self.__datoslblFrm = tk.LabelFrame(self.__framealtas, text="Agregar Servicio", bg="#FFFFFF",
                                           width=self.__ancho - 20, height=80, font=("Sora", 10))
        self.__datoslblFrm.place(x=10, y=100)

        self.__dataservicios = self.__sql.getservicios()
        listaservicios = []
        if (self.__dataservicios != None):
            for fila in self.__dataservicios:
                servicio = fila[4]
                listaservicios.append(servicio)

        # servicio
        lblservicio = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Servicio: ", font=("Sora", 11))
        lblservicio.place(x=10, y=5)
        self.__cmbservicio = ttk.Combobox(self.__datoslblFrm, width=60, values=listaservicios, state="readonly")
        self.__cmbservicio.place(x=10, y=25)

        # cantidad
        lblcantidad = tk.Label(self.__datoslblFrm, bg="#FFFFFF", text="Cantidad:", font=("Sora", 11))
        lblcantidad.place(x=400, y=5)
        self.__txtcantidad = tk.Entry(self.__datoslblFrm, width=10, font=("Sora", 10))
        self.__txtcantidad.place(x=400, y=25)

        # boton agregar servicio
        btnagregaservicio = tk.Button(self.__datoslblFrm, text="Agregar Servicio", bg="#565656", width=20, fg="#D3D3D3",
                                      height=1, font=("Sora", 10), command=self.insertarservicio)
        btnagregaservicio.place(x=500, y=20)

        lblayuda = tk.Label(self.__framealtas, bg="#FFFFFF", fg="#FF0000",
                            text="Para eliminar un registro, seleccione el elemento y presione la tecla <SUPRIMIR>",
                            font=("Sora", 10))
        lblayuda.place(x=10, y=180)

        self.__detalleslblFrm = tk.LabelFrame(self.__framealtas, text="Detalles de Factura", bg="#FFFFFF",
                                              width=self.__ancho - 20, height=280, font=("Sora", 10))
        self.__detalleslblFrm.place(x=10, y=200)

        self.__tablafactura = ttk.Treeview(self.__detalleslblFrm,
                                           columns=("#", "servicio", "cantidad", "subtotal", "total"), show="headings")
        self.__tablafactura.bind("<Delete>", self.borrarservicio)
        self.__tablafactura.heading("#", text="ID", anchor=tk.W)
        self.__tablafactura.column("#", minwidth=0, width=20, stretch=NO, anchor=tk.W)
        self.__tablafactura.heading("servicio", text="Descripcion del servicio", anchor=tk.W)
        self.__tablafactura.column("servicio", minwidth=0, width=250, stretch=NO, anchor=tk.W)
        self.__tablafactura.heading("cantidad", text="Cantidad")
        self.__tablafactura.column("cantidad", minwidth=0, width=120, stretch=NO, anchor=tk.CENTER)
        self.__tablafactura.heading("subtotal", text="Costo unitario")
        self.__tablafactura.column("subtotal", minwidth=0, width=130, stretch=NO, anchor=tk.E)
        self.__tablafactura.heading("total", text="Costo Total")
        self.__tablafactura.column("total", minwidth=0, width=130, stretch=NO, anchor=tk.E)
        self.__tablafactura.place(x=5, y=5, width=self.__ancho - 40, height=230)

        lbltotal = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="Total (sin I.V.A.): $",
                            font=("Sora", 10, "bold"))
        lbltotal.place(x=400, y=235)
        self.__lbltotalsum = tk.Label(self.__detalleslblFrm, bg="#FFFFFF", text="0.0", font=("Sora", 10, "bold"))
        self.__lbltotalsum.place(x=600, y=235)

        # botones
        # botoncancelat y agregar

        btnagregar = tk.Button(self.__framealtas, text="Generar Factura", width=20, bg="#00c800", height=1,
                               font=("Sora", 10),
                               command=self.insertarfactura)
        btnagregar.place(x=900, y=590)

        # frame
        self.__framealtas.place(x=130, y=110)

    def insertarservicio(self):
        if (self.__cmbservicio.get() != "" and self.__txtcantidad.get() != ""):
            registro = []
            for fila in self.__dataservicios:
                if (fila[4] == self.__cmbservicio.get()):
                    total = int(self.__txtcantidad.get()) * int(fila[2])
                    registro = [fila[0], self.__cmbservicio.get(), self.__txtcantidad.get(), fila[2], str(total)]
                    self.__total += float(total)
            self.__tablafactura.insert(parent="", index=0, values=registro)
            self.__lbltotalsum.config(text=str(self.__total))
        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")

    def borrarservicio(self, _):
        for i in self.__tablafactura.selection():
            print(self.__tablafactura.item(i)["values"][4])
            self.__total -= float(self.__tablafactura.item(i)["values"][4])
            self.__tablafactura.delete(i)
        self.__lbltotalsum.config(text=str(self.__total))

    def insertarfactura(self):
        if self.validavacios():
            idfactura = int(self.__sql.ultimoidfactura()) + 1
            lista = self.__cmbcliente.get().split()
            # cliente
            cliente = [fila for fila in self.__dataclientes if
                       lista[0] == fila[2] and lista[1] == fila[3] and lista[2] == fila[1]]
            id_cliente = cliente[0][0]

            lista = self.__cmbempleado.get().split()
            # empleado
            empleado = [fila for fila in self.__dataempleados if
                        lista[0] == fila[2] and lista[1] == fila[3] and lista[2] == fila[1]]
            id_empleado = empleado[0][0]

            fecha = datetime.date.today()
            fechavalue = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day)

            datos = [idfactura, id_empleado, id_cliente, fechavalue, float(self.__lbltotalsum.cget("text")), "Activa"]
            self.__sql.insertarfactura(datos)
            # print(datos)
            id_venta = int(self.__sql.ultimoidventa()) + 1
            servicios = self.__tablafactura.get_children()
            for servicio in servicios:
                print(self.__tablafactura.item(servicio)['values'])
                id_servicio = self.__tablafactura.item(servicio)['values'][0]
                datos = [id_venta, id_servicio, idfactura]
                id_venta += 1
                self.__sql.insertarventa(datos)
            messagebox.showinfo(message="FACTURA GENERADA CORRECTAMENTE", title="REGISTO EXITOSO")
            self.__framealtas.destroy()
            self.altas()

        else:
            messagebox.showerror(message="CAMPOS VACÍOS", title="ERROR")

        # self.mostrarfactura()

    # PENDIENTE
    def mostrarfactura(self):
        # pdf = canvas.Canvas("facturas/ejemplo.pdf", pagesize=letter)
        # pdf.drawString(x=10, y=10, text="Hola Merari, este es un pdf")
        # pdf.save()

        winfactura = tk.Toplevel(self.__ventana)
        # winfactura.protocol('WM_DELETE_WINDOW', self.close)
        self.__printfactura = tk.LabelFrame(winfactura, text="", bg="#FFFFFF",
                                            width=self.__ancho - 20, height=90, font=("Sora", 10))
        self.__printfactura.place(x=10, y=5)

    def validavacios(self):
        if self.__cmbcliente.get() == "" or self.__cmbempleado.get() == "" or self.__txtdia == "" or self.__txtmes.get() == "" \
                or self.__txtanio.get() == "" or len(self.__tablafactura.get_children()) == 0:
            return False
        else:
            return True

    def bajas(self):
        self.actualizabotones("bajas")

        # formulario
        self.__framebajas = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framebajas, text="Cancelar factura", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # facturas
        lblfactura = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Factura No.: ", font=("Sora", 10))
        lblfactura.place(x=50, y=10)

        self.__data = self.__sql.getfacturas()
        listafacturas = []
        if (self.__data != None):
            for fila in self.__data:
                factura = fila[0]
                listafacturas.append(factura)

        # Combo de las facturas
        cmbfacturas = ttk.Combobox(self.__generallblFrm, width=40, font=("Sora", 10), state="readonly",
                                   values=listafacturas)
        cmbfacturas.place(x=122, y=10)

        btnseleccionar = tk.Button(self.__generallblFrm, text="Seleccionar", bg="#565656", width=20, fg="#D3D3D3",
                                   command=lambda: self.detallesfactura(cmbfacturas.get()))
        btnseleccionar.place(x=480, y=10)
        self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20,
                                          height=300)
        self.__framedatos.place(x=10, y=80)

        # botones

        btncancelar = tk.Button(self.__framebajas, text="Cancelar Factura",  bg="#800000",width=20,fg="#D3D3D3",
                                command=lambda: self.cancelarfactura(cmbfacturas.get()))
        btncancelar.place(x=900, y=590)

        # lo blanco
        self.__framebajas.place(x=130, y=110)

    def detallesfactura(self, id_factura):
        if id_factura != "":
            self.__framedatos.destroy()
            self.__framedatos = tk.LabelFrame(self.__framebajas, text="Detalles", bg="#FFFFFF", width=self.__ancho - 20,
                                              height=350)
            self.__framedatos.place(x=10, y=80)

            # empleado y cliente
            factura = self.__sql.getfactura(id_factura)
            empleado = self.__sql.getempleado(factura[0][1])
            cliente = self.__sql.getcliente(factura[0][2])
            ventas = self.__sql.getventa(id_factura)
            # print(empleado, type(empleado))

            # factura
            lblNO = tk.Label(self.__framedatos, bg="#FFFFFF", text="No. Factura: ", font=("Sora", 10))
            lblNO.place(x=5, y=5)
            lblnovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=factura[0][0], font=("Sora", 10))
            lblnovalor.place(x=80, y=5)

            lblfecha = tk.Label(self.__framedatos, bg="#FFFFFF", text="Fecha: ", font=("Sora", 10))
            lblfecha.place(x=5, y=25)
            lblfechavalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=factura[0][3], font=("Sora", 10))
            lblfechavalor.place(x=80, y=25)

            # cliente
            textcliente = cliente[0][0] + " " + cliente[0][1] + " " + cliente[0][2]
            lblcliente = tk.Label(self.__framedatos, bg="#FFFFFF", text="Cliente: ", font=("Sora", 10))
            lblcliente.place(x=5, y=45)
            lblclientevalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=textcliente, font=("Sora", 10))
            lblclientevalor.place(x=80, y=45)

            # empleado
            textempleado = empleado[0][0] + " " + empleado[0][1] + " " + empleado[0][2]
            lblempleado = tk.Label(self.__framedatos, bg="#FFFFFF", text="Empleado: ", font=("Sora", 10))
            lblempleado.place(x=5, y=65)
            lblempleadovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=textempleado, font=("Sora", 10))
            lblempleadovalor.place(x=80, y=65)
            ypos = 85
            for venta in ventas:
                # venta
                lblservicio = tk.Label(self.__framedatos, bg="#FFFFFF", text="Servicio: ", font=("Sora", 10))
                lblservicio.place(x=5, y=ypos)
                lblventavalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=venta[4], font=("Sora", 10))
                lblventavalor.place(x=80, y=ypos)

                # ypos +=20
                # lbltipo = tk.Label(self.__framedatos, bg="#FFFFFF", text="Tipo: ", font=("Sora", 10))
                # lbltipo.place(x=5, y=ypos)
                # lbltipovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=venta[1], font=("Sora", 10))
                # lbltipovalor.place(x=80, y=ypos)

                # ypos += 20
                # lblcosto = tk.Label(self.__framedatos, bg="#FFFFFF", text="Costo: ", font=("Sora", 10))
                # lblcosto.place(x=5, y=ypos)
                # lblcostovalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=venta[2], font=("Sora", 10))
                # lblcostovalor.place(x=80, y=ypos)

                ypos += 20
                # lbldescripcion = tk.Label(self.__framedatos, bg="#FFFFFF", text="Descripcion: ", font=("Sora", 10))
                # lbldescripcion.place(x=5, y=ypos)
                lbldescripcionvalor = tk.Label(self.__framedatos, bg="#FFFFFF", text=venta[3], font=("Sora", 10))
                lbldescripcionvalor.place(x=80, y=ypos)

                ypos += 20
        else:
            messagebox.showerror(message="Seleccione una factura", title="ERROR")

    def cancelarfactura(self, id_factura):
        if id_factura != "":
            datos = ["Cancelada", id_factura]
            self.__sql.editarfactura(datos)
            messagebox.showinfo(message="Factura cancelada", title="REGISTO EXITOSO")
            self.__framebajas.destroy()
            self.bajas()
        else:
            messagebox.showerror(message="Seleccione una factura", title="ERROR")

    def reportes(self):
        self.actualizabotones("reportes")

        # formulario
        self.__framereportes = tk.Frame(self.__ventana, bg="#FFFFFF", width=self.__ancho, height=self.__alto)

        self.__generallblFrm = tk.LabelFrame(self.__framereportes, text="Filtros:", bg="#FFFFFF",
                                             width=self.__ancho - 20, height=60, font=("Sora", 10))
        self.__generallblFrm.place(x=10, y=10)

        # facturas
        lblfiltro1 = tk.Label(self.__generallblFrm, bg="#FFFFFF", text="Mostrar: ", font=("Sora", 10))
        lblfiltro1.place(x=10, y=10)


        # facturas
        self.__cmbfiltro1 = ttk.Combobox(self.__generallblFrm, width=20, font=("Sora", 10), state="readonly",
                                  values=["Status", "Cliente", "Empleado", "Fecha", "Total"],  textvar=self.__strvar1)
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

        self.__tablafacturas= ttk.Treeview(self.__framedatos, columns=("#", "fecha","cliente", "empleado", "total", "status"), show="headings")

        self.__tablafacturas.heading("#", text="Id", anchor=tk.W)
        self.__tablafacturas.column("#", minwidth=0, width=20, stretch=NO, anchor=tk.W)
        self.__tablafacturas.heading("fecha", text="Fecha", anchor=tk.W)
        self.__tablafacturas.column("fecha", minwidth=0, width=200, stretch=NO, anchor=tk.W)
        self.__tablafacturas.heading("empleado", text="Empleado", anchor=tk.W)
        self.__tablafacturas.column("empleado", minwidth=0, width=200, stretch=NO, anchor=tk.W)
        self.__tablafacturas.heading("cliente", text="Cliente", anchor=tk.W)
        self.__tablafacturas.column("cliente", minwidth=0, width=200, stretch=NO, anchor=tk.W)
        self.__tablafacturas.heading("total", text="Total", anchor=tk.W)
        self.__tablafacturas.column("total", minwidth=0, width=340, stretch=NO, anchor=tk.W)
        self.__tablafacturas.heading("status", text="Status", anchor=tk.W)
        self.__tablafacturas.column("status", minwidth=0, width=100, stretch=NO, anchor=tk.W)
        self.__tablafacturas.place(x=5, y=5, width=self.__ancho - 40, height=360)

        self.__cmbfiltro1.set("")

        # lo blanco
        self.__framereportes.place(x=130, y=110)

    def filtrar(self,filtro1,filtro2):
        if filtro1 == "" or filtro2 == "":
            messagebox.showerror(message="Seleccione un filtro", title="ERROR")
        else:
            self.limpiartabla()
            facturas = self.__sql.getfacturasby(filtro1,filtro2, self.__dictclientes, self.__dictempleados)
            registro = []
            if facturas != None :
                for fila in facturas:
                    nombrec= fila [6] + " " + fila[7] + " " + fila[8]
                    nombree = fila[9] + " " + fila[10] + " " + fila[11]
                    registro = [fila[0], fila[3], nombrec, nombree,fila[4], fila[5]]
                    self.__tablafacturas.insert(parent="", index=0, values=registro)
            else:
                messagebox.showinfo(message="No hay registros", title="Sin registros")

    def limpiartabla(self):
        elementos = self.__tablafacturas.get_children()
        for i in elementos:
            self.__tablafacturas.delete(i)


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
        self.__logon = Image.open("./img/facturas.png")
        self.__logon = self.__logon.resize((100, 100))
        self.__logon = ImageTk.PhotoImage(self.__logon)
        self.__lblimagen = tk.Label(self.__framebotones, image=self.__logon, width=100, height=100)
        self.__lblimagen.place(x=10, y=0)

        self.__btnaltas = tk.Button(self.__framebotones, bg="#565656", text="Altas", fg="#D3D3D3", width=12, height=1,
                                    font=("Sora", 10), command=lambda: self.operacion(self.altas,"a"))
        self.__btnaltas.place(x=10, y=130)

        self.__btncanceladas = tk.Button(self.__framebotones, bg="#565656", text="Cancelar", fg="#D3D3D3", width=12,
                                         height=1,
                                         font=("Sora", 10), command=lambda: self.operacion(self.bajas, "b"))
        self.__btncanceladas.place(x=10, y=158)

        self.__btnreportes = tk.Button(self.__framebotones, bg="#565656", text="Reportes", fg="#D3D3D3", width=12,
                                       height=1,
                                       font=("Sora", 10), command=lambda: self.operacion(self.reportes, "r"))
        self.__btnreportes.place(x=10, y=186)

        self.__framebotones.place(x=0, y=120)

    def clearall(self):
        if self.__lblimagennegado != None:
            self.__lblimagennegado.destroy()
            self.__lblimagennegado=None

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
            if op == "a" or op=="r":
                funcion()
            else:
                self.negado()
        elif self.__nivel == 3:
            if op == "r" :
                funcion()
            else:
                self.negado()
        else:
            self.negado()
