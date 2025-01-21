import tkinter as tk
from tkinter import ttk
import sql
import login
import principal
from tkinter import messagebox


class Main:
    def __init__(self):

        self.vlogin = login.Login()  # creamos un objeto tipo Login
        self.__cancelar, self.__usr, self.__acceso = self.vlogin.ventana() #mandamos a a llamar el metodo ventana del objeto vlogin


        if self.__cancelar != True:

            self.vPrincipal = principal.Principal(self.__acceso, self.__usr)
            self.vPrincipal.ventana()

m=Main()