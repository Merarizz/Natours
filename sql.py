import sqlite3
import os.path
import pandas as pd
import warnings

class SQL:
    def __init__(self):
        self.__bd="./bd/Natours"
        self.__conector=None
        self.__exists=False
        self.conectar()
        warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


    def validausuario(self, nombre, contra):
        cursor = self.__conector.cursor()
        query = "select * from empleados where nombre = '" + nombre + "' and contrasena = '" + contra + "'"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = None
        else:
            id = data[0]
        return id



    def conectar(self):
        if os.path.isfile(self.__bd):
            self.__exists=True

        self.__conector=sqlite3.connect( self.__bd)
        if not self.__exists:
            self.creartablas()
            self.llenardatos()
            print("se crearon las tablas")


    def creartablas(self):
        cursor=self.__conector.cursor()
        tablasarchivo=open("./bd/tablas.txt", "r")
        for linea in tablasarchivo:
            cursor.execute(linea)

    def llenardatos(self):
        #cursor=self.__conector.cursor()
        self.setpaises()
        self.setcp()
        #datosarchivo = open("./bd/datos.txt", "r")
        #for linea in datosarchivo:
            #cursor.execute(linea)




    def setcp(self):
        file = pd.ExcelFile("./archivos/codigopostal.xlsx", engine="openpyxl")
        self.clearcp()
        id_pais = self.getidpais("México")
        # print(file.sheet_names)
        for sheet in file.sheet_names:
            # print(sheet)
            df = pd.read_excel("./archivos/codigopostal.xlsx", sheet)
            # print(df["d_codigo"], df["d_asenta"], df["d_ciudad"], df["d_estado"])
            df["d_ciudad"] = df["d_ciudad"].fillna(df["d_asenta"])
            # filtrar por columnas
            datos = df[["d_codigo", "d_asenta", "d_ciudad", "d_estado"]].values.tolist()
            for d in datos:
                d.append(id_pais)
                self.insertarcp(d)
                print(d)

    def setpaises(self):
        file = pd.read_excel("./archivos/prefijos.xlsx", engine="openpyxl")
        self.clearpaises()
        datos = file.values.tolist()
        print(type(datos))
        for x in datos:
            self.insertarpaises(x)



    #LLENAR LAS TABLAS--------------------
    def insertarcp(self,listadatos):
        cursor= self.__conector.cursor()
        query=("insert into cp(cp, colonia, ciudad, estado, id_pais)")
        query+= "values(?,?,?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def insertarpaises(self, listadatos):
        cursor = self.__conector.cursor()
        query = ("insert into paises(nombre, prefijo)")
        query += "values(?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    # INSERTAR--------------------
    def insertarempleado(self,listadatos, fechafinal):
        cursor = self.__conector.cursor()
        if fechafinal:
            query = ("insert into empleados( nombre, ap_pat, ap_mat, curp, nss, telefono, id_direccion, "
                     "puesto, acceso, correo, contrasena, sueldo, comision, fecha_inicio, estatus, fecha_final)")
            query+= "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        else:
            query = ("insert into empleados( nombre, ap_pat, ap_mat, curp, nss, telefono, id_direccion, "
                     "puesto, acceso, correo, contrasena, sueldo, comision, fecha_inicio, estatus)")
            query += "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def insertarcliente(self,listadatos):
        cursor = self.__conector.cursor()
        query = ("insert into clientes( nombre, ap_pat, ap_mat, curp, telefono, nom_empresa, id_direccion, "
                 "correo)")
        query+= "values(?,?,?,?,?,?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def insertarprospecto(self,listadatos):
        cursor = self.__conector.cursor()
        query = ("insert into prospectos( empresa, telefono, nombre, descripcion, id_direccion, correo, "
                 "ap_pat,ap_mat)")
        query+= "values(?,?,?,?,?,?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def insertarservicio(self,listadatos, final):
        cursor = self.__conector.cursor()
        if final:
            query = "insert into servicios(tipo_servicio, costo, detalles, titulo, comision, fecha_inicio, restricciones, subtipo, ciudad, estado, pais, fecha_final)"
            query+= "values(?,?,?,?, ?, ?,?,?,?, ?,?,?)"
        else:
            query = "insert into servicios(tipo_servicio, costo, detalles, titulo, comision, fecha_inicio, restricciones, subtipo, ciudad, estado, pais)"
            query += "values(?,?,?,?, ?, ?,?,?,?, ?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def insertardireccion(self,listadatos):
        cursor = self.__conector.cursor()
        query = ("insert into direcciones( calle, no_exterior, no_interior, id_cp)")
        query += "values(?,?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()


    def insertarfactura(self,listadatos):
        cursor = self.__conector.cursor()
        query = "insert into facturas(id_factura, id_empleado, id_cliente, fecha, total, status)"
        query += "values(?,?,?,?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def insertarventa(self,listadatos):
        cursor = self.__conector.cursor()
        query = "insert into ventas(id_venta, id_servicio, id_factura)"
        query += "values(?,?,?)"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    # ELIMINAR-------------------
    def eliminarempleado(self,id_empleado):
        cursor = self.__conector.cursor()
        query = "delete from empleados where id_empleado=" + str(id_empleado)
        cursor.execute(query)
        self.__conector.commit()

    def eliminardireccion(self,id_direccion):
        cursor = self.__conector.cursor()
        query = "delete from direcciones where id_direccion=" + str(id_direccion)
        cursor.execute(query)
        self.__conector.commit()

    def eliminarcp(self,id_cp):
        cursor = self.__conector.cursor()
        query = "delete from cp where id_cp=" + str(id_cp)
        cursor.execute(query)
        self.__conector.commit()

    def eliminarcliente(self, id_cliente):
        cursor = self.__conector.cursor()
        query = "delete from clientes where id_cliente=" + str(id_cliente)
        cursor.execute(query)
        self.__conector.commit()

    def eliminarprospecto(self, id_prospecto):
        cursor = self.__conector.cursor()
        query = "delete from prospectos where id_prospecto=" + str(id_prospecto)
        cursor.execute(query)
        self.__conector.commit()

    def eliminarservicio(self, id_servicio):
        cursor = self.__conector.cursor()
        query = "delete from servicios where id_servicio=" + str(id_servicio)
        cursor.execute(query)
        self.__conector.commit()

    #EDITAR--------------------
    def editarempleado(self, listadatos, fechafinal):
        cursor = self.__conector.cursor()
        if fechafinal:
            query = ("update empleados set nombre=?, ap_pat=?, ap_mat=?, curp=?, nss=?, telefono=?, id_direccion=?, "
                     "puesto=?, acceso=?, correo=?, contrasena=?, sueldo=?, comision=?, fecha_inicio=?, fecha_final=?, estatus=?")
        else:
            query = (
                "update empleados set nombre=?, ap_pat=?, ap_mat=?, curp=?, nss=?, telefono=?, id_direccion=?, "
                "puesto=?, acceso=?, correo=?, contrasena=?, sueldo=?, comision=?, fecha_inicio=?, estatus=?")
        query += "where id_empleado= ?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def editarcp(self, listadatos):
        cursor = self.__conector.cursor()
        query = ("update cp set cp=?, colonia=?, ciudad=?, estado=?, id_pais=?")
        query += "where id_cp= ?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def editarcliente(self,listadatos):
        cursor = self.__conector.cursor()
        query = ("update clientes set nombre=?, ap_pat=?, ap_mat=?, curp=?, telefono=?, nom_empresa=?, "
                 "id_direccion=?, correo=?")
        query+= " where id_cliente=?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def editardireccion(self, listadatos):
        cursor = self.__conector.cursor()
        query = ("update direcciones set calle=?, no_exterior=?, no_interior=?, id_cp=?")
        query += " where id_direccion=?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def editarprospecto(self, listadatos):
        cursor = self.__conector.cursor()
        query = ("update prospectos set empresa=?, telefono=?, nombre=?, descripcion=?, id_direccion=?, "
                 "correo=?, ap_pat=?,ap_mat=?")
        query += " where id_prospecto=?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def editarservicio(self, listadatos, final):
        cursor = self.__conector.cursor()
        if final:
            query = ("update servicios set tipo_servicio=?, costo=?, detalles=?, titulo=?, comision=?, fecha_inicio=?,"
                     "restricciones=?, subtipo=?, ciudad=?, estado=?, pais=?, fecha_final=?")
            query += " where id_servicio=?"
        else:
            query = (
                "update servicios set tipo_servicio=?, costo=?, detalles=?, titulo=?, comision=?, fecha_inicio=?,"
                "restricciones=?, subtipo=?, ciudad=?, estado=?, pais=?")
            query += " where id_servicio=?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

    def editarfactura(self, listadatos):
        cursor = self.__conector.cursor()
        query = "update facturas set status=?"
        query += " where id_factura=?"
        cursor.execute(query, listadatos)
        self.__conector.commit()

     # ULTIMO--------------------

    def ultimoidempleado(self):
        cursor = self.__conector.cursor()
        query = "select id_empleado from empleados order by id_empleado desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id=0
        else:
            id= data[0][0]
        return id

    def ultimoidprospecto(self):
        cursor = self.__conector.cursor()
        query = "select id_prospecto from prospectos order by id_prospecto desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    def ultimoidcliente(self):
        cursor = self.__conector.cursor()
        query = "select id_cliente from clientes order by id_cliente desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    def ultimoidservicio(self):
        cursor = self.__conector.cursor()
        query = "select id_servicio from servicios order by id_servicio desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]

        return id


    def ultimoiddireccion(self):
        cursor = self.__conector.cursor()
        query = "select id_direccion from direcciones order by id_direccion desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    def ultimocp(self):
        cursor = self.__conector.cursor()
        query = "select id_cp from cp order by id_cp desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    def ultimoidfactura(self):
        cursor = self.__conector.cursor()
        query = "select id_factura from facturas order by id_factura desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    def ultimoidventa(self):
        cursor = self.__conector.cursor()
        query = "select id_venta from ventas order by id_venta desc limit 1;"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    # GET--------------------

    def getcpid(self, codigo, colonia):
        cursor = self.__conector.cursor()
        query = "select id_cp from cp where cp='" + codigo + "' and colonia = '" + colonia + "';"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id
    def getidpais(self, pais):
        cursor = self.__conector.cursor()
        query = "select id_pais from paises where nombre='" + pais + "';"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]

        return id

    def getiddireccion(self, pais):
        cursor = self.__conector.cursor()
        query = "select id_direccion from paises where nombre='" + pais + "';"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            id = 0
        else:
            id = data[0][0]
        return id

    def getempleados(self):
        cursor = self.__conector.cursor()
        query = ("select * from empleados left join direcciones on empleados.id_direccion=direcciones.id_direccion"
                 " left join cp on direcciones.id_cp=cp.id_cp left join paises on cp.id_pais=paises.id_pais;")
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getclientes(self):
        cursor = self.__conector.cursor()
        query = ("select * from clientes left join direcciones on clientes.id_direccion=direcciones.id_direccion"
                 " left join cp on direcciones.id_cp=cp.id_cp left join paises on cp.id_pais=paises.id_pais;")
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getprospectos(self):
        cursor = self.__conector.cursor()
        query = ("select * from prospectos left join direcciones on prospectos.id_direccion=direcciones.id_direccion"
                 " left join cp on direcciones.id_cp=cp.id_cp left join paises on cp.id_pais=paises.id_pais;")
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getservicios(self):
        cursor = self.__conector.cursor()
        query = "Select * from servicios"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getpaises(self):
        cursor = self.__conector.cursor()
        query = "Select * from paises"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data)<=0:
            data = None
        return data

    def getfacturas(self):
        cursor = self.__conector.cursor()
        query = "Select * from facturas where status= 'Activa'"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getfactura(self, id_factura):
        cursor = self.__conector.cursor()
        query = "Select * from facturas where id_factura=" + str(id_factura)
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getcliente(self,id_cliente):
        cursor = self.__conector.cursor()
        query = "Select nombre,ap_pat,ap_mat from clientes where id_cliente=" + str(id_cliente)
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getcp(self,codigo):
        cursor = self.__conector.cursor()
        query = "Select * from cp where cp=" + str(codigo)
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getempleado(self,id_empleado):
        cursor = self.__conector.cursor()
        query = "Select nombre,ap_pat,ap_mat from empleados where id_empleado=" + str(id_empleado)
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getventa(self,id_factura):
        cursor = self.__conector.cursor()
        query = "Select * from servicios where id_servicio in ( Select id_servicio from ventas where id_factura=" + str(id_factura) + ")"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

# filtros
    def getempleadoby(self,campo, valor):
        cursor = self.__conector.cursor()
        if valor == "Todos":
            query = "select empleados.*, paises.nombre from empleados,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = empleados.id_direccion)));"
        elif campo == "Estatus" or campo == "Puesto":
            query = "select empleados.*, paises.nombre from empleados,paises where " + campo + "='" + valor + "' and paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = empleados.id_direccion)));"
        elif campo == "Pais":
            query = "select * from (select empleados.*, paises.nombre as pais from empleados,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = empleados.id_direccion)))) as a where a.pais= '" + valor + "';"
        else :
            rangos=valor.split("-")
            if rangos [1]=="máx":
                query = "select empleados.*, paises.nombre from empleados,paises where " + campo + ">" + rangos[0] + " and paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = empleados.id_direccion)));"
            else:
                query = "select empleados.*, paises.nombre from empleados,paises where " + campo + " between " + rangos[0] + " and " + rangos[1] + " and paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = empleados.id_direccion)));"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getclienteby(self,campo, valor):
        cursor = self.__conector.cursor()
        if valor == "Todos":
            query = "select clientes.*, paises.nombre from clientes,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = clientes.id_direccion)));"
        elif campo == "Pais":
            query = "select * from (select clientes.*, paises.nombre as pais from clientes,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = clientes.id_direccion)))) as a where a.pais= '" + valor + "';"
        else:
            rangos = valor.split("-")
            if rangos[1] == "máx":
                #select clientes.*,ventas.*, paises.nombre as pais from clientes, paises, (select id_cliente, sum(total) as totales from facturas where status="Activa" group by id_cliente) as ventas where ventas.totales between 100000 and 300000 and clientes.id_cliente=ventas.id_cliente and paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = clientes.id_direccion)));
                query = "select clientes.*,ventas.*, paises.nombre as pais from clientes, paises, (select id_cliente, sum(total) as totales from facturas where status='Activa' group by id_cliente) as ventas where ventas.totales > " + rangos[0] +" and clientes.id_cliente=ventas.id_cliente and paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = clientes.id_direccion)));"
            else:
                query = "select clientes.*,ventas.*, paises.nombre as pais from clientes, paises, (select id_cliente, sum(total) as totales from facturas where status='Activa' group by id_cliente) as ventas where ventas.totales between " + rangos[0] + " and " + rangos[1] + " and clientes.id_cliente=ventas.id_cliente and paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = clientes.id_direccion)));"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getprospectosby(self,campo, valor):
        cursor = self.__conector.cursor()
        if valor == "Todos":
            query = "select prospectos.*, paises.nombre from prospectos,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = prospectos.id_direccion)));"
        elif campo == "Pais":
            query = "select * from (select prospectos.*, paises.nombre as pais from prospectos,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = prospectos.id_direccion)))) as a where a.pais= '" + valor + "';"

        else:
            query = "select prospectos.*, paises.nombre from prospectos,paises where paises.nombre=(select nombre from paises where id_pais=(select id_pais from cp where id_cp=(select id_cp from direcciones where id_direccion = prospectos.id_direccion)));"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getserviciosby(self,campo, valor):
        cursor = self.__conector.cursor()
        if valor == "Todos":
            query="select * from servicios; "
        elif campo == "Tipo servicio":
            query= "select * from servicios where tipo_servicio='" + valor + "';"
        elif campo == "Pais":
            query= "select * from servicios where pais='" + valor + "';"
        else:
            rangos = valor.split("-")
            if rangos[1] == "máx":
                query = "select * from servicios where " + campo + ">" + rangos[0]
            else:
                query = "select * from servicios where " + campo + " between " + rangos[0] + " and " + rangos[1]
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data


    def getfacturasby(self,campo, valor, diclientes, dicempleados):
        cursor = self.__conector.cursor()
        if valor == "Todos":
            query = ("select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente,"
                     " empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
                     "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado ")
        elif campo=="Total":
            rangos = valor.split("-")
            if rangos[1] == "máx":
                query = "select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente, "
                query+= "empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
                query+= "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado where " + campo + ">" + rangos[0]
            else:
                query = "select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente, "
                query += "empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
                query += "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado where " + campo + " between " + rangos[0] + " and " + rangos[1]
        elif campo == "Cliente":
            id_cliente=diclientes[valor]
            query = "select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente, "
            query += "empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
            query += "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado where facturas.id_cliente=" + str(id_cliente)
        elif campo == "Empleado":
            id_empleado = dicempleados[valor]
            query = "select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente, "
            query += "empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
            query += "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado where facturas.id_empleado=" + str(id_empleado)
        elif campo == "Status":

            query = "select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente, "
            query += "empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
            query += "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado where facturas.status ='" + valor + "'"
        else:
            query = "select facturas.*, clientes.nombre as ncliente,clientes.ap_pat as pcliente, clientes.ap_mat as mcliente, "
            query += "empleados.nombre, empleados.ap_pat, empleados.ap_mat from facturas left join clientes on "
            query += "facturas.id_cliente=clientes.id_cliente left join  empleados on  facturas.id_empleado= empleados.id_empleado where year(fecha)=" + valor

        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def getpaisesby(self,tabla):
        cursor = self.__conector.cursor()
        query = "select pais from direcciones where id_direccion in ( select id_direccion from " + tabla + ")"
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def custQuery(self,query):
        cursor = self.__conector.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) <= 0:
            data = None
        return data

    def clearpaises(self):
        cursor= self.__conector.cursor()
        query= "delete from paises;"
        cursor.execute(query)

    def clearcp(self):
        cursor = self.__conector.cursor()
        query = "delete from cp;"
        cursor.execute(query)


    def cerrar(self):
        self.__conector.close()

#s=SQL()






