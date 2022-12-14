#!/usr/local/bin/python3.8

#Luis Fernando Ch. 2022

from sys import path
import os, platform

#path.append('C:\\Users\\Aprendiz\\Documents\\CiscoPythonADSI\\PythonEssentials2\\Packete en grupo\\package')
path.append(path[0]+'/package')
from luis.operations import moduloDiv, exponenciacion, mult, suma, rest
from eduard.moduloEduard import hypotenusa, fac, cei
from juan.ejercicio import radio, gcd

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear()
    print('''
    --- MODULOS Y PAQUETES EN PYTHON ---
            
            --- Luis Fernando Ch.  ---

        Eliga una opcion: 
    ''')
    while True:
        print('''
        ------------------------------
        1. Residuo de divicion
        2. exponenciacion
        3. multiplicacion
        4. suma
        5. resta
        6. radio
        7. gcd
        8. tangente
        9. Hipotenusa
        10.Factorial
        11.Ceil
        12.
    ''')
        try:
            opcion=int(input('Eliga una opcion:  '))
            if opcion == 1:
                clear()
                moduloDiv()
            elif opcion == 2:
                clear()
                exponenciacion()
            elif opcion == 3:
                clear()
                mult()
            elif opcion == 4:
                clear()
                suma()
            elif opcion == 5:
                clear()
                rest()
            elif opcion == 6:
                clear()
                radio()
            elif opcion == 7:
                clear()
                gcd()
            elif opcion == 8:
                clear()
                pass
            elif opcion == 9:
                clear()
                print(hypotenusa())
            elif opcion == 10:
                clear()
                print(fac())
            elif opcion == 11:
                clear()
                print(cei())
            elif opcion == 12:
                pass
            else:
                print('Opci??n no v??lida')
        except:
            print('Opci??n no v??lida')
        finally:
            opc = input('Desea continuar? (s/n): ')
            if opc == 's':
                clear()
            else:
                clear()
                print('BYE')
                break



if __name__ == "__main__":
    main()




