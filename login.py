import tkinter as tk
from tkinter import ttk, messagebox
import sql
from PIL import Image, ImageTk

class Login:
    def __init__(self):
        self.__usuario = ""
        self.__contrasenia = ""
        self.__cancelar = False
        self.__nivel= 0
        self.__ancho=650
        self.__alto=400
        self.__txtusuario = None
        self.__txtcontra = None
        self.__ventanalogin = None
        self.__sql=sql.SQL()

    def ventana(self):
        #ventana
        self.__ventanalogin=tk.Tk()
        self.__ventanalogin.config(width=self.__ancho, height=self.__alto)
        self.__ventanalogin.config(bg="#D3D3D3")
        self.__ventanalogin.title("LOGIN")

        #Imagen
        logon=Image.open("./img/portada.png")
        logon=logon.resize((self.__ancho//2, self.__alto))
        logon=ImageTk.PhotoImage(logon)
        lblimagen=tk.Label(image=logon, width=self.__ancho//2, height=self.__alto)
        lblimagen.place(x=0, y=0)

        #TITULO
        titulo = tk.Label(self.__ventanalogin, bg="#D3D3D3", text="Inicio de sesión ", font=("Times New Roman", 30))
        titulo.place(x=358, y=50)

        # usuario y contraseña
        lblusuario=tk.Label(self.__ventanalogin, bg="#D3D3D3", text="Usuario ", font=("Sora",10))
        lblusuario.place(x=340, y=140)
        lblcontrasenia=tk.Label(self.__ventanalogin, bg="#D3D3D3", text="Contraseña ",font=("Sora",10))
        lblcontrasenia.place(x=340, y=210)

        # cajitas de usuario y contraseña
        self.__txtusuario=tk.Entry(self.__ventanalogin, width=45)
        self.__txtusuario.place(x=340, y=170)
        self.__txtcontra= tk.Entry(self.__ventanalogin, width=45, show="*")
        self.__txtcontra.place(x=340, y=240)



        # boton inicio y crear sesión
        botoninicio=tk.Button(self.__ventanalogin, bg = "#565656", text="Iniciar sesión", fg = "#D3D3D3",
                              width=35, height=1, font=("Sora", 10), command=self.__checkUserPass)
        botoninicio.place(x=340, y=298)
        botonrcear=tk.Button(self.__ventanalogin, bg = "#565656", text="Salir", fg = "#D3D3D3",
                             width=35, height=1,  font=("Sora", 10), command=self.__close)
        botonrcear.place(x=340, y=330)

        self.__ventanalogin.mainloop()
        return  self.__cancelar, self.__usuario, self.__nivel

    def __checkUserPass(self):
        self.__usuario = self.__txtusuario.get()
        self.__contrasenia = self.__txtcontra.get()
        id = self.__sql.validausuario(self.__usuario, self.__contrasenia)
        if id != None:
            self.__nivel = id[9]
            self.__ventanalogin.destroy()
        else:
            self.__usuario = ""
            self.__nivel = 0
            messagebox.showerror(message="Usuario o contraseña invalidos", title="ERROR")


    def __close(self):
        self.__cancelar = True
        self.__usuario = ""
        self.__nivel = 0
        self.__ventanalogin.destroy()
