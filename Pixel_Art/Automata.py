from Reportes import Reporte


class Automata:

    def __init__(self):
        self.reporte = Reporte()
        self.ruta = ''
        self.contenido = ''
        self.caracter = ''
        self.token = ''
        self.estado = 0
        self.lista_nombres = []
        self.lista_imagenes = []
        self.imagen = []
        self.lista_celdas = []
        self.celda = []
        self.filtros = []
        self.lista_tokens = []
        self.lista_errores = []

    def letra(self, caracter):  # -----> Método para saber si el carácter es una letra
        L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if caracter in L:
            return True
        else:
            return False

    def cadena(self, caracter):  # -----> Método para saber si el carácter es una letra
        C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        if caracter.lower() in C:
            return True
        else:
            return False

    def digito(self, caracter):  # -----> Método para saber si el carácter es un digito
        D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if caracter in D:
            return True
        else:
            return False

    def leer_archivo(self, ruta):
        self.ruta = ruta

        with open(self.ruta, mode='r') as archivo:
            self.contenido = archivo.read()

        f = 1
        c = 0
        while c < len(self.contenido):
            self.caracter = self.contenido[c]

            if self.estado == 0:  # -----------------------------------> Estado 0
                if self.letra(self.caracter):
                    self.estado = 1
                    self.lista_tokens.append(f'\tId\t\t Letras\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == '@':
                    self.estado = 34
                    self.lista_tokens.append(f'\tSeparador\t\t Caracteres\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                else:
                    self.estado = 0
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 1:  # -----------------------------------> Estado 1
                if self.letra(self.caracter):
                    self.estado = 1
                elif self.caracter == '=':
                    self.estado = 2
                    self.lista_tokens.append(f'\tSimbolo\t\t Caracter\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                else:
                    self.estado = 1
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 2:  # -----------------------------------> Estado 2
                if self.caracter == '"':
                    self.estado = 3
                    self.lista_tokens.append(f'\tNombre\t\t Caracteres\t\t Fila:\t {f}\t\t Columna:\t {c+2}')
                elif self.digito(self.caracter):
                    self.estado = 4
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tDigito\t\t Numeros\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == '{':
                    self.estado = 5
                    f = f + 1
                elif self.caracter == 'M':
                    self.estado = 20
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tFiltro\t\t Letras\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == 'D':
                    self.estado = 28
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tFiltro\t\t Letras\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                else:
                    self.estado = 2
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 3:  # -----------------------------------> Estado 3
                if self.cadena(self.caracter) or self.digito(self.caracter):
                    self.estado = 3
                    self.token = self.token + self.caracter
                elif self.caracter == ';':
                    self.estado = 0
                    self.lista_nombres.append(self.token)
                    self.imagen.append(self.token)
                    self.token = ''
                    f = f + 1
                else:
                    self.estado = 3
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 4:  # -----------------------------------> Estado 4
                if self.digito(self.caracter):
                    self.estado = 4
                    self.token = self.token + self.caracter
                elif self.caracter == ',':
                    self.estado = 5
                    self.celda.append(self.token)
                    self.token = ''
                elif self.caracter == ';':
                    self.estado = 0
                    self.imagen.append(self.token)
                    self.token = ''
                    f = f + 1
                else:
                    self.estado = 4
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 5:  # -----------------------------------> Estado 5
                if self.digito(self.caracter):
                    self.estado = 4
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tDigito\t\t Numeros\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == 'T' or self.caracter == 'F':
                    self.estado = 6
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tBandera\t\t Letras\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == '#':
                    self.estado = 13
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tColor\t\t Caracteres\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == '\t':
                    self.estado = 5
                    self.lista_tokens.append(f'\tTabulación\t\t Espacios\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                else:
                    self.estado = 5
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 6:  # -----------------------------------> Estado 6
                if self.caracter == 'R':
                    self.estado = 7
                    self.token = self.token + self.caracter
                elif self.caracter == 'A':
                    self.estado = 10
                    self.token = self.token + self.caracter
                else:
                    self.estado = 6
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 7:  # -----------------------------------> Estado 7
                if self.caracter == 'U':
                    self.estado = 8
                    self.token = self.token + self.caracter
                else:
                    self.estado = 7
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 8:  # -----------------------------------> Estado 8
                if self.caracter == 'E':
                    self.estado = 9
                    self.token = self.token + self.caracter
                else:
                    self.estado = 8
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 9:  # -----------------------------------> Estado 9
                if self.caracter == ',':
                    self.estado = 5
                    self.celda.append(self.token)
                    self.token = ''
                else:
                    self.estado = 9
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 10:  # -----------------------------------> Estado 10
                if self.caracter == 'L':
                    self.estado = 11
                    self.token = self.token + self.caracter
                else:
                    self.estado = 10
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 11:  # -----------------------------------> Estado 11
                if self.caracter == 'S':
                    self.estado = 12
                    self.token = self.token + self.caracter
                else:
                    self.estado = 11
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 12:  # -----------------------------------> Estado 12
                if self.caracter == 'E':
                    self.estado = 9
                    self.token = self.token + self.caracter
                else:
                    self.estado = 12
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 13:  # -----------------------------------> Estado 13
                if self.letra(self.caracter) or self.digito(self.caracter):
                    self.estado = 14
                    self.token = self.token + self.caracter
                else:
                    self.estado = 13
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 14:  # -----------------------------------> Estado 14
                if self.letra(self.caracter) or self.digito(self.caracter):
                    self.estado = 15
                    self.token = self.token + self.caracter
                else:
                    self.estado = 14
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 15:  # -----------------------------------> Estado 15
                if self.letra(self.caracter) or self.digito(self.caracter):
                    self.estado = 16
                    self.token = self.token + self.caracter
                else:
                    self.estado = 15
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 16:  # -----------------------------------> Estado 16
                if self.letra(self.caracter) or self.digito(self.caracter):
                    self.estado = 17
                    self.token = self.token + self.caracter
                else:
                    self.estado = 16
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 17:  # -----------------------------------> Estado 17
                if self.letra(self.caracter) or self.digito(self.caracter):
                    self.estado = 18
                    self.token = self.token + self.caracter
                else:
                    self.estado = 17
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 18:  # -----------------------------------> Estado 18
                if self.letra(self.caracter) or self.digito(self.caracter):
                    self.estado = 19
                    self.token = self.token + self.caracter
                else:
                    self.estado = 18
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 19:  # -----------------------------------> Estado 19
                if self.caracter == ',':
                    self.estado = 5
                    self.celda.append(self.token)
                    self.lista_celdas.append(self.celda)
                    self.token = ''
                    self.celda = []
                    f = f + 1
                elif self.caracter == '\n':
                    self.estado = 19
                    self.celda.append(self.token)
                    self.lista_celdas.append(self.celda)
                    self.imagen.append(self.lista_celdas)
                    self.token = ''
                    self.celda = []
                    self.lista_celdas = []
                    f = f + 1
                elif self.estado == ';':
                    self.estado = 0
                else:
                    self.estado = 19
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 20:  # -----------------------------------> Estado 20
                if self.caracter == 'I':
                    self.estado = 21
                    self.token = self.token + self.caracter
                else:
                    self.estado = 20
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 21:  # -----------------------------------> Estado 21
                if self.caracter == 'R':
                    self.estado = 22
                    self.token = self.token + self.caracter
                else:
                    self.estado = 21
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 22:  # -----------------------------------> Estado 22
                if self.caracter == 'R':
                    self.estado = 23
                    self.token = self.token + self.caracter
                else:
                    self.estado = 22
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 23:  # -----------------------------------> Estado 23
                if self.caracter == 'O':
                    self.estado = 24
                    self.token = self.token + self.caracter
                else:
                    self.estado = 23
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 24:  # -----------------------------------> Estado 24
                if self.caracter == 'R':
                    self.estado = 25
                    self.token = self.token + self.caracter
                else:
                    self.estado = 24
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 25:  # -----------------------------------> Estado 25
                if self.caracter == 'X':
                    self.estado = 26
                    self.token = self.token + self.caracter
                elif self.caracter == 'Y':
                    self.estado = 27
                    self.token = self.token + self.caracter
                elif self.caracter == ',':
                    self.estado = 2
                    self.filtros.append(self.token)
                    self.token = ''
                elif self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                else:
                    self.estado = 25
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 26:  # -----------------------------------> Estado 26
                if self.caracter == ',':
                    self.estado = 2
                    self.filtros.append(self.token)
                    self.token = ''
                elif self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                else:
                    self.estado = 26
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 27:  # -----------------------------------> Estado 27
                if self.caracter == ',':
                    self.estado = 2
                    self.filtros.append(self.token)
                    self.token = ''
                elif self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                else:
                    self.estado = 27
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 28:  # -----------------------------------> Estado 28
                if self.caracter == 'O':
                    self.estado = 29
                    self.token = self.token + self.caracter
                else:
                    self.estado = 28
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 29:  # -----------------------------------> Estado 29
                if self.caracter == 'U':
                    self.estado = 30
                    self.token = self.token + self.caracter
                else:
                    self.estado = 29
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 30:  # -----------------------------------> Estado 30
                if self.caracter == 'B':
                    self.estado = 31
                    self.token = self.token + self.caracter
                else:
                    self.estado = 30
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 31:  # -----------------------------------> Estado 31
                if self.caracter == 'L':
                    self.estado = 32
                    self.token = self.token + self.caracter
                else:
                    self.estado = 31
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 32:  # -----------------------------------> Estado 32
                if self.caracter == 'E':
                    self.estado = 33
                    self.token = self.token + self.caracter
                else:
                    self.estado = 32
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 33:  # -----------------------------------> Estado 33
                if self.caracter == 'M':
                    self.estado = 20
                    self.token = self.token + self.caracter
                else:
                    self.estado = 33
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 34:  # -----------------------------------> Estado 34
                if self.caracter == '@':
                    self.estado = 35
                else:
                    self.estado = 34
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 35:  # -----------------------------------> Estado 35
                if self.caracter == '@':
                    self.estado = 36
                else:
                    self.estado = 35
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 36:  # -----------------------------------> Estado 36
                if self.caracter == '@':
                    self.estado = 37
                else:
                    self.estado = 36
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')
            elif self.estado == 37:  # -----------------------------------> Estado 37
                if self.caracter == '\n':
                    self.estado = 0
                    self.filtros.append(self.token)
                    self.imagen.append(self.filtros)
                    self.lista_imagenes.append(self.imagen)
                    self.token = ''
                    self.filtros = []
                    self.imagen = []
                    f = f + 1
                else:
                    self.estado = 37
                    self.lista_errores.append(f'\tFila:\t {f}\t\t Columna:\t {c+1}\t\t Error:\t {self.caracter}')

            c = c + 1

    def mostrar_informacion(self):
        print('-->Imagenes:')
        print(len(self.lista_nombres))
        for i in self.lista_nombres:
            nombre = i
            print(nombre)
            print('------------------------------')

        print('-->Información:')
        print(len(self.lista_imagenes))
        for e in self.lista_imagenes:
            imagen = e
            print(imagen)
            print('------------------------------')

    def generar_reportes(self):
        self.reporte.reporte_tokens(self.lista_tokens)
        self.reporte.reporte_errores(self.lista_errores)
