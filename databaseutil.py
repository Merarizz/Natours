import sql
import pandas as pd
import warnings

class DBUtil:
    def __init__(self):
        self.__sql= sql.SQL()
        warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


    def setcp(self):
        file = pd.ExcelFile("./archivos/codigopostal.xlsx", engine="openpyxl")
        self.__sql.clearcp()
        id_pais = self.__sql.getidpais("México")
        #print(file.sheet_names)
        for sheet in file.sheet_names:
            #print(sheet)
            df = pd.read_excel("./archivos/codigopostal.xlsx", sheet)
            #print(df["d_codigo"], df["d_asenta"], df["d_ciudad"], df["d_estado"])
            df["d_ciudad"]=df["d_ciudad"].fillna(df["d_asenta"])
            #filtrar por columnas
            datos=df[["d_codigo", "d_asenta", "d_ciudad", "d_estado"]].values.tolist()
            for d in datos:
                d.append(id_pais)
                self.__sql.insertarcp(d)
                print(d)


    def setpaises(self):
        file = pd.read_excel("./archivos/prefijos.xlsx", engine="openpyxl")
        self.__sql.clearpaises()
        datos= file.values.tolist()
        print(type (datos))
        for x in datos:
            self.__sql.insertarpaises(x)

















































