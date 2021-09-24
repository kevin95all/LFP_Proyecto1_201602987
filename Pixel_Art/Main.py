from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Automata import Automata
import webbrowser
import os


class Main:

    def __init__(self):
        self.ventana = Tk()
        self.imagen = Label(self.ventana)
        self.automata = Automata()
        self.archivo_analizado = False
        self.ruta = ''

    def ventana_principal(self):
        self.ventana.title('Bitxelart')
        self.centrar_ventana()
        self.ventana.resizable(False, False)
        self.componentes()
        self.ventana.mainloop()

    def centrar_ventana(self):
        w, h = 850, 600
        w_pantalla = self.ventana.winfo_screenwidth()
        h_pantalla = self.ventana.winfo_screenheight()
        x = ((w_pantalla / 2) - (w / 2))
        y = ((h_pantalla / 2) - (h / 2)) - 50
        self.ventana.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

    def componentes(self):
        self.barra()
        self.botones()

    def barra(self):
        menu = Menu(self.ventana)  # -----> Creando la barra de opciones

        cargar = Menu(menu)  # -----> Creando las opciones para la barra
        analizar = Menu(menu)
        seleccionar = Menu(menu)
        reportes = Menu(menu)
        salir = Menu(menu)

        cargar.add_command(label='1. Cargar archivo', command=self.cargar_archivo)  # -----> Creando las acciones
        analizar.add_command(label='1. Analizar archivo', command=self.analizar_archivo)
        seleccionar.add_command(label='1. Seleccionar imagen', command=self.seleccionar_imagen)
        reportes.add_command(label='1. Ver reportes', command=self.ver_reportes)
        salir.add_command(label='1. Salir', command=self.salir)

        menu.add_cascade(label='Cargar', menu=cargar)  # -----> Agregando las opciones a la barra
        menu.add_cascade(label='Analizar', menu=analizar)
        menu.add_cascade(label='Seleccionar', menu=seleccionar)
        menu.add_cascade(label='Reportes', menu=reportes)
        menu.add_cascade(label='Salir', menu=salir)

        self.ventana.config(menu=menu)  # -----> Agregando la barra de opciones al contenedor

    def botones(self):
        original = Button(self.ventana, text='Original', width=12, height=2, command=self.mostrar_o)
        original.place(x=55, y=195)

        mirrorx = Button(self.ventana, text='Mirror X', width=12, height=2, command=self.mostrar_x)
        mirrorx.place(x=55, y=250)

        mirrory = Button(self.ventana, text='Mirror Y', width=12, height=2, command=self.mostrar_y)
        mirrory.place(x=55, y=305)

        doublem = Button(self.ventana, text='Double Mirror', width=12, height=2, command=self.mostrar_d)
        doublem.place(x=55, y=360)

        self.imagen.configure(bg='black', width=85, height=33)
        self.imagen.place(x=200, y=50)

    def mostrar_o(self):
        self.imagen.configure(bg='red')

    def mostrar_x(self):
        self.imagen.configure(bg='blue')

    def mostrar_y(self):
        self.imagen.configure(bg='green')

    def mostrar_d(self):
        self.imagen.configure(bg='cyan')

    def cargar_archivo(self):  # -----> Método para la busqueda de archivos (pxla)
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos PXLA', '*.pxla'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            messagebox.showinfo('Información', 'No se cargo ningun archivo')
        else:
            messagebox.showinfo('Información', 'Archivo cargado con exito')

    def analizar_archivo(self):  # -----> Método para empezar con el analisis del archivo
        if self.ruta == '':
            messagebox.showinfo('Información', 'No hay archivos cargados')
        else:
            self.automata.leer_archivo(self.ruta)
            self.archivo_analizado = True
            messagebox.showinfo('Información', 'Archivo analizado con exito')

    def seleccionar_imagen(self):
        if self.ruta == '':
            messagebox.showinfo('Información', 'No hay archivos cargados')
        else:
            if self.archivo_analizado:
                pass
            else:
                messagebox.showinfo('Información', 'No se ha analizado el archivo')

    def ver_reportes(self):
        if self.ruta == '':
            messagebox.showinfo('Información', 'No hay archivos cargados')
        else:
            if self.archivo_analizado:
                chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                tokens = 'file:///' + os.getcwd() + '/' + 'archivos_creados/tokens.html'
                errores = 'file:///' + os.getcwd() + '/' + 'archivos_creados/errores.html'

                webbrowser.get(chromedir).open_new_tab(tokens)
                webbrowser.get(chromedir).open_new_tab(errores)
            else:
                messagebox.showinfo('Información', 'No se ha analizado el archivo')

    def salir(self):
        self.ruta = ''
        self.archivo_analizado = False
        exit()


app = Main()  # -----> app es un objeto de la clase Main
app.ventana_principal()
