import sys
class Calculadora():

    def plus(self, op1, op2):

        return op1 + op2
    def minus(self, op1, op2):

        return op1 - op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        variables = Calculadora()  # making the object
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except IndexError:
        sys.exit("Error: You need to give me numbers on the Command Line")



    if sys.argv[2] == "suma":
        result = variables.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = variables.minus(operando1, operando2)
    else:
        sys.exit('You can only add or subtract.')

print(result)
