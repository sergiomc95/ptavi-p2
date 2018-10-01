#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import calcooHija


fichero = open(sys.argv[1],'r')
lista = fichero.readlines()

if __name__ == "__main__":

    Calculadora = calcooHija.CalculadoraHija()
    for linea in lista:
    #quitamos la coma a todos los elementos excepto el último
        elementos = linea[:-1].split(',')

        operando1 = int(elementos[1])
        operando2 = int(elementos[2])

        operaciones = {'suma': Calculadora.plus, 'resta': Calculadora.minus, 'divide': Calculadora.divide, 'multiplica': Calculadora.multiplica}

        operando = elementos[0]
        resultado = operaciones[operando](operando1, operando2)

        for elem in elementos[3:]:
            resultado = operaciones[operando](resultado,int(elem))
        print(resultado)
