from src.logica.Operaciones import Operaciones
class Error(Exception):
    pass
class ErrorValor(Error):
    pass
if __name__=='__main__':
    operacion=Operaciones()
    while True:
       try:
           numero1 =operacion.ingresoDatos (input("Ingrese el primer número: "))
           numero2 =operacion.ingresoDatos (input("Ingrese el segundo número: "))
           for n in (numero1, numero2):
              if (not type(n) is float) and (not type(n) is int):
                 raise ErrorValor
           resultado = operacion.suma (numero1, numero2)
           print("{0:.2f} + {1:.2f} = {2:.2f}".format(numero1, numero2, resultado))
           break
       except ErrorValor:
           print(f"ERROR en \"{n}\", no es un valor valido. Vuelva a ingresar el numero.")
           print("")
    print("\nFin del Programa.")

