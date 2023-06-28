from tkinter import *
from tkinter import ttk
from functools import partial
import cmath


class Calculadora:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculadora de Números Complejos')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        self.__ventana.resizable(0, 0)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        self.__primerOperando = None
        self.__segundoOperando = None
        self.__contador = 0
        opts = { 'ipadx': 18, 'ipady': 60 , 'sticky': 's' }
        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='i', command=partial(self.ponerNUMERO, 'i')).grid(column=4, row=7)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerNUMERO, '+')).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerNUMERO, '-')).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerNUMERO, '*')).grid(column=3, row=8, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerNUMERO, '/')).grid(column=4, row=8, sticky=W)
        ttk.Button(mainframe, text='C', command=self.borrarPanel).grid(column=4, row=4, sticky=W)
        
        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            self.__primerOperando = self.convertir(str(valor))
            self.__panel.set(numero)

    def borrarPanel(self):
        self.__panel.set('')

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado = 0
        if operacion == '+':
            resultado = operando1 + operando2
        elif operacion == '-':
            resultado = operando1 - operando2
        elif operacion == '*':
            resultado = operando1 * operando2
        elif operacion == '/':
            resultado = operando1 / operando2
        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        if op == '=':
            operacion = self.__operador.get()
            self.__segundoOperando = self.convertir(str(self.__panel.get()))
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                operacion = self.__operador.get()
                self.__segundoOperando = self.convertir(str(self.__panel.get()))
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op

    def convertir(self, cadena):
        if cadena == '+':
            return '+'
        elif cadena == '-':
            return '-'
        elif cadena == '*':
            return '*'
        elif cadena == '/':
            return '/'
        elif 'i' in cadena:
            partes = cadena.split('+')
            if len(partes) > 1:
                real = float(partes[0])
                imag = float(partes[1][:-1])
                return Imaginario(real, imag)
            elif len(partes) == 1:
                partes = cadena.split('-')
                real = float(partes[0])
                imag = float(partes[1][:-1]) * -1
                return Imaginario(real, imag)
        else:
            return float(cadena)

class Imaginario:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def getImaginario(self):
        return self.imaginario
    def getReal(self):
        return self.real

    def __add__(self, other):
        real = self.real + other.real
        imaginario = self.imaginario + other.imaginario
        return Imaginario(real, imaginario)

    def __sub__(self, other):
        real = self.real - other.real
        imaginario = self.imaginario - other.imaginario
        return Imaginario(real, imaginario)

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginario * other.imaginario)
        imaginario = (self.real * other.imaginario) + (self.imaginario * other.real)
        return Imaginario(real, imaginario)

    def __truediv__(self, other):
        divisor = (other.real ** 2) + (other.imaginario ** 2)
        real = ((self.real * other.real) + (self.imaginario * other.imaginario)) / divisor
        imaginario = ((self.imaginario * other.real) - (self.real * other.imaginario)) / divisor
        return Imaginario(real, imaginario)
                        

    def __str__(self):
            return f"{str(self.real)} + {str(self.imaginario)}i"
def main():
    calculadora = Calculadora()

if __name__ == '__main__':
    main()
