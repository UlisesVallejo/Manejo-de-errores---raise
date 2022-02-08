from random import randint


class ErrorMinimo(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
            
    def __str__(self):
        if self.message:
            return f"ErrorMinimo: {self.message}"
        else:
            "Se generó ErrorMinimo."

class ErrorMaximo(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
            
    def __str__(self):
        if self.message:
            return f"ErrorMaximo: {self.message}"
        else:
            "Se generó ErrorMaximo."


valormin = 1
valormax = 5

while True:
    try:
        num = int(input(f"\nEscribe un valor entre {valormin} y {valormax}: "))
        
        if num < valormin:
            raise ErrorMinimo("El valor es menor al rango")
        elif num > valormax:
            raise ErrorMaximo("El valor es mayor al rango")

        
    except ValueError:
        print("Debe der un entero dentro del rango")
    except ErrorMinimo as e:
        print("ERROR: ",e)
    except ErrorMaximo as e:
        print("ERROR: ",e)
        
    finally:
        loteria = randint(valormin, valormax) 
        if num == loteria:
            print("ADIVINASTE, ERES BRUJO")
            break
        else:
            print("Gracias por participar, no adivinaste el número")