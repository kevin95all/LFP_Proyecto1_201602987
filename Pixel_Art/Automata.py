class Automata:

    def __init__(self):
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
                elif self.digito(self.caracter):
                    self.estado = 4
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tDigito\t\t Numeros\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == '{':
                    self.estado = 5
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
                if self.caracter != '"' or self.caracter != ';':
                    self.estado = 3
                    self.token = self.token + self.caracter
                    self.lista_tokens.append(f'\tNombre\t\t Caracteres\t\t Fila:\t {f}\t\t Columna:\t {c+1}')
                elif self.caracter == ';':
                    self.estado = 0
                    self.lista_nombres.append(self.token)
                    self.imagen.append(self.token)
                    self.token = ''
                    f = f + 1

            c = c + 1
