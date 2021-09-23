from Token import Token
from Error import Error
from prettytable import PrettyTable


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
            self.agregar_token(caracter, 'puntoycoma', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == ',':
            self.agregar_token(caracter, 'coma', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == '[':
            self.agregar_token(caracter, 'corchete-izquierdo', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == ']':
            self.agregar_token(caracter, 'corchetederecho', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == '{':
            self.agregar_token(caracter, 'llave-izquierda', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == '}':
            self.agregar_token(caracter, 'llave-derecha', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == '=':
            self.agregar_token(caracter, 'igual', self.linea, self.columna)
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t', ' ']:
            self.columna += 1

    def estadoB(self):
        pass

    def estadoC(self):
        pass

    def estadoD(self):
        pass

    def estadoE(self):
        pass

    def estadoF(self):
        pass

    def estadoG(self):
        pass

    def estadoH(self):
        pass

    def estadoI(self):
        pass

    def estadoJ(self):
        pass

    def estadoK(self):
        pass

    def estadoL(self):
        pass

    def estadoM(self):
        pass

    def estadoN(self):
        pass

    def estadoO(self):
        pass

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        # recorrer caracter por caracter
        self.i = 0
        while self.i < len(cadena):
            if self.estado == "A":
                self.estadoA(cadena[self.i])
            elif self.estado == "B":
                self.estadoA(cadena[self.i])
            elif self.estado == "C":
                self.estadoA(cadena[self.i])
            elif self.estado == "D":
                self.estadoA(cadena[self.i])
            elif self.estado == "E":
                self.estadoA(cadena[self.i])
            elif self.estado == "F":
                self.estadoA(cadena[self.i])
            elif self.estado == "G":
                self.estadoA(cadena[self.i])
            elif self.estado == "H":
                self.estadoA(cadena[self.i])
            elif self.estado == "I":
                self.estadoA(cadena[self.i])
            elif self.estado == "J":
                self.estadoA(cadena[self.i])
            elif self.estado == "K":
                self.estadoA(cadena[self.i])
            elif self.estado == "L":
                self.estadoA(cadena[self.i])
            elif self.estado == "M":
                self.estadoA(cadena[self.i])
            elif self.estado == "N":
                self.estadoA(cadena[self.i])
            elif self.estado == "O":
                self.estadoA(cadena[self.i])
            self.i += 1

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
