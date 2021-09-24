from Token import Token
from Error import Error
from prettytable import PrettyTable
import re
TITULO="Pokeball";

class AnalizadorLexico:

    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = "A"
        self.i = 0

    def agregar_token(self, caracter, token, linea, columna):
        self.listaTokens.append(Token(caracter, token, linea, columna))
        self.buffer = ''

    def agregar_error(self, caracter, linea, columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))

    def estadoA(self, caracter):
        if caracter == ';':
            self.buffer += caracter
            self.columna += 1
            self.estado = "L"
        elif caracter == ',':
            self.buffer += caracter
            self.columna += 1
            self.estado = "K"
        elif caracter == '[':
            self.buffer += caracter
            self.columna += 1
            self.estado = "I"
        elif caracter == ']':
            self.buffer += caracter
            self.columna += 1
            self.estado = "J"
        elif caracter == '{':
            self.buffer += caracter
            self.columna += 1
            self.estado = "G"
        elif caracter == '}':
            self.buffer += caracter
            self.columna += 1
            self.estado = "H"
        elif caracter == '=':
            self.buffer += caracter
            self.columna += 1
            self.estado = "M"
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
            self.estado = "D"
        elif caracter == '#':
            self.buffer += caracter
            self.columna += 1
            self.estado = "E"
        elif caracter == '"':
            self.buffer += caracter
            self.columna += 1
            self.estado = "B"
        elif caracter == '@':
            self.buffer += caracter
            self.columna += 1
            self.estado = "F"
        elif caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
            self.estado = "C"
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t', ' ']:
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.buffer = ''
            self.columna += 1

    def estadoB(self, caracter):
        if caracter != "\"":
            self.buffer += caracter
            self.columna += 1
            self.estado = "N"
        else:
            self.estado = "A"
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.i -=1
            self.buffer = ''


    def estadoC(self, caracter):
        if caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
        else:
            if re.search("titulo|ancho|alto|filas|columnas|celdas|true|false|filtros|mirrorx|mirrory|doublemirror", self.buffer.lower()):
                self.agregar_token(self.buffer, 'reservada', self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
            else:
                self.agregar_error(self.buffer, self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
                self.buffer = ''

    def estadoD(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(self.buffer, 'digito', self.linea, self.columna)
            self.estado = "A"
            self.i -= 1

    def estadoE(self, caracter):
        if caracter.isalpha() or caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
            self.estado = "O"
        else:
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.estado = "A"
            self.buffer = ''
            self.i -= 1

    def estadoO(self, caracter):
        if caracter.isalpha() or caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(self.buffer, 'color hex', self.linea, self.columna)
            self.estado = "A"
            self.i -= 1

    def estadoF(self, caracter):
        if caracter == "@":
            self.buffer += caracter
            self.columna += 1
        else:
            if len(self.buffer) == 4:
                self.agregar_token(self.buffer, 'separador', self.linea, self.columna)

            else:
                self.agregar_error(self.buffer, self.linea, self.columna)
                self.buffer = ''
            self.estado = "A"
            self.i -= 1

    def estadoG(self, caracter):
        self.agregar_token(self.buffer, 'llave izquierda', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoH(self, caracter):
        self.agregar_token(self.buffer, 'llave derecha', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoI(self, caracter):
        self.agregar_token(self.buffer, 'corchete izquierdo', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoJ(self, caracter):
        self.agregar_token(self.buffer, 'corchete derecho', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoK(self, caracter):
        self.agregar_token(self.buffer, 'coma', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoL(self, caracter):
        self.agregar_token(self.buffer, 'punto y coma', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoM(self, caracter):
        self.agregar_token(self.buffer, 'simbolo =', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoN(self, caracter):
        if caracter != "\"":
            self.buffer += caracter
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_token(self.buffer, 'identificador', self.linea, self.columna)
            self.estado = "P"

    def estadoP(self, caracter):
        self.estado = "A"
        self.i -= 1

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        # recorrer caracter por caracter
        self.i = 0
        while self.i < len(cadena):
            if self.estado == "A":
                self.estadoA(cadena[self.i])
            elif self.estado == "B":
                self.estadoB(cadena[self.i])
            elif self.estado == "C":
                self.estadoC(cadena[self.i])
            elif self.estado == "D":
                self.estadoD(cadena[self.i])
            elif self.estado == "E":
                self.estadoE(cadena[self.i])
            elif self.estado == "F":
                self.estadoF(cadena[self.i])
            elif self.estado == "G":
                self.estadoG(cadena[self.i])
            elif self.estado == "H":
                self.estadoH(cadena[self.i])
            elif self.estado == "I":
                self.estadoI(cadena[self.i])
            elif self.estado == "J":
                self.estadoJ(cadena[self.i])
            elif self.estado == "K":
                self.estadoK(cadena[self.i])
            elif self.estado == "L":
                self.estadoL(cadena[self.i])
            elif self.estado == "M":
                self.estadoM(cadena[self.i])
            elif self.estado == "N":
                self.estadoN(cadena[self.i])
            elif self.estado == "O":
                self.estadoO(cadena[self.i])
            elif self.estado == "P":
                self.estadoP(cadena[self.i])
            self.i += 1
        self.impErrores()
        self.impTokens()

    # imprimeTokens
    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarData())
        print(x)

    # imprimeErrores
    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores) == 0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
            print(x)
