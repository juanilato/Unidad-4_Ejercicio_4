from tkinter import *
from tkinter import ttk
from functools import partial


class Calculadora(object):
    __ventana = None
    __operador = None
    __panel = None
    __operadorAux = None
    __primerOperando = None
    __segundoOperando = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
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
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='i', command=partial(self.ponerNUMERO, 'i')).grid(column=1, row=8, sticky=W)
        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            self.__primerOperando = valor + numero
            self.__panel.set(self.__primerOperando)

    def borrarPanel(self):
        self.__panel.set('0')

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado = 0
        if operacion == '+':
            resultado = complejo_sumar(operando1, operando2)
        elif operacion == '-':
            resultado = complejo_restar(operando1, operando2)
        elif operacion == '*':
            resultado = complejo_multiplicar(operando1, operando2)
        elif operacion == '/':
            resultado = complejo_dividir(operando1, operando2)

        self.__panel.set(resultado)

    def ponerOPERADOR(self, op):
        if op == '=':
            operacion = self.__operador.get()
            self.__segundoOperando = self.__panel.get()
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                operacion = self.__operador.get()
                self.__segundoOperando = self.__panel.get()
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op


def complejo_sumar(complejo1, complejo2):
    real1, imag1 = parsear_complejo(complejo1)
    real2, imag2 = parsear_complejo(complejo2)
    real_suma = real1 + real2
    imag_suma = imag1 + imag2
    return formatear_complejo(real_suma, imag_suma)


def complejo_restar(complejo1, complejo2):
    real1, imag1 = parsear_complejo(complejo1)
    real2, imag2 = parsear_complejo(complejo2)
    real_resta = real1 - real2
    imag_resta = imag1 - imag2
    return formatear_complejo(real_resta, imag_resta)


def complejo_multiplicar(complejo1, complejo2):
    real1, imag1 = parsear_complejo(complejo1)
    real2, imag2 = parsear_complejo(complejo2)
    real_mult = (real1 * real2) - (imag1 * imag2)
    imag_mult = (real1 * imag2) + (imag1 * real2)
    return formatear_complejo(real_mult, imag_mult)


def complejo_dividir(complejo1, complejo2):
    real1, imag1 = parsear_complejo(complejo1)
    real2, imag2 = parsear_complejo(complejo2)
    denominador = (real2 * real2) + (imag2 * imag2)
    real_div = ((real1 * real2) + (imag1 * imag2)) / denominador
    imag_div = ((imag1 * real2) - (real1 * imag2)) / denominador
    return formatear_complejo(real_div, imag_div)


def parsear_complejo(complejo):
    complejo = complejo.strip()
    real = 0
    imag = 0

    if complejo[0] == '-':
        complejo = complejo[1:]
        signo_real = -1
    else:
        signo_real = 1

    if complejo[-1] == 'i':
        complejo = complejo[:-1]
        signo_imag = 1
    else:
        signo_imag = 0

    if '+' in complejo:
        partes = complejo.split('+')
        real = float(partes[0]) * signo_real
        imag = float(partes[1]) * signo_imag
    elif '-' in complejo:
        partes = complejo.split('-')
        if partes[0] == '':
            partes = partes[1:]
            real = -float(partes[0]) * signo_real
            imag = -float(partes[1]) * signo_imag
        else:
            real = float(partes[0]) * signo_real
            imag = -float(partes[1]) * signo_imag
    else:
        if 'i' in complejo:
            imag = float(complejo) * signo_imag
        else:
            real = float(complejo) * signo_real

    return real, imag


def formatear_complejo(real, imag):
    if real != 0 and imag != 0:
        if imag > 0:
            return f"{real} + {imag}i"
        else:
            return f"{real} - {-imag}i"
    elif real != 0:
        return f"{real}"
    elif imag != 0:
        return f"{imag}i"
    else:
        return "0"


def main():
    calculadora = Calculadora()


if __name__ == '__main__':
    main()
