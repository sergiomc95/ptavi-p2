#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplica(self, op1, op2):
        return op1 * op2

    def divide(self, op1, op2):

        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")


if __name__ == "__main__":
        try:
            operando1 = int(sys.argv[1])
            operando2 = int(sys.argv[3])
            variables = CalculadoraHija()
        except ValueError:
            sys.exit("Error: Non numerical parameters")
        except IndexError:
            sys.exit("Error: You need to give me numbers on the Command Line")

        if sys.argv[2] == "suma":
            result = variables.plus(operando1, operando2)
        elif sys.argv[2] == "resta":
            result = variables.minus(operando1, operando2)

        elif sys.argv[2] == "multiplica":
            result = variables.multiplica(operando1, operando2)
        elif sys.argv[2] == "divide":

            result = variables.divide(operando1, operando2)
        else:
            sys.exit('You can only add or subtract.')
        print(result)
