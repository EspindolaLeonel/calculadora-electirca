from os import system
import os
from functions import *

while True:
    print("  \n           BIENVENIDO A LA CALCULADORA ELECTRICA \n")
    print("¿Que desea realizar? \n\
    [1]- Calculos en corriente Alterna \n\
    [2]- Calculos en corriente continua \n\
    [3]- Salir")
    
    opcion=input("      Su eleccion es:  ")
 


    if opcion == "1":
        print("               Calculos en corriente alterna: \n \n\
            [1] - Corriente de un motor trifasico\n\
            [2] - Corriente de un motor monofasico\n\
            [3] - Potencia Activa Trifasica\n\
            [4] - Potencia Activa Monfasica\n\
            [5] - Potencia Reactiva Trifasica\n\
            [6] - Potencia Reactiva Monfasica\n\
            [7] - Valor de correccion del Factor de Potencia\n\
            [8] - Pasar de VAr a MicroFaradio\n\
            [9] - Salir ")
        option_selec = input("     Su eleccion es: ")
        if option_selec == "1":
                potencia_trifasica = int(input("ingrese el valor de la potencia en KW: "))
                tension = int(input("ingrese el valor de la tension red: "))
                cos_fi = input("ingrese el valor del coseno de fi: ")
                os.system("cls")
                print("\n El valor de la corriente es: ", calcular_corriente_trifasica(potencia_trifasica, tension, cos_fi), "Amperios")
        elif option_selec == "2":
                potencia_monofasica = int(input("ingrese el valor de la potencia en KW: "))
                tension =  int(input("ingrese el valor de la tension de la red: "))
                cos_fi = float(input("ingrese el valor del coseno de fi: "))
                os.system("cls")
                print("\n  El valor de la corriente es: ", calcular_corriente_monofasica(potencia_monofasica, tension, cos_fi), "Amperios" )
        elif option_selec == "3":
                corriente_trifasica = int(input("ingrese el valor de la corriente: "))
                tension = int(input("ingrese el valor de la tension: "))
                cos_fi = float(input("ingrese el valor del coseno de fi: "))
                os.system("cls")
                print("\n El valor de la Potencia Activa Trifasica es: ", calcular_potencia_activa_trifasica(corriente_trifasica, tension, cos_fi), "Watts")
        elif option_selec == "4":
                corriente_monofasica = int(input("Ingrese el valor de la corriente: "))
                tension = int(input("Ingrese el valor de la tension de la red: "))
                cos_fi = float(input("Ingrese el valor del coseno de fi: "))
                os.system("cls")
                print("\n El valor de la Potencia Activa Monofasica es: ", calcular_potencia_activa_monofasica(corriente_monofasica, tension, cos_fi) , "Watts")
        elif option_selec =="5":
                corriente_trifasica = int(input("Ingrese el valor de la corriente: "))
                tension = int(input("Ingrese el valor de la tension de la red: "))
                cos_fi = float(input("ingrese el valor del coseno de fi: "))
                os.system("cls")
                print("\n El valor de la Potencia Reactiva Trifasica es: ", calcular_potencia_reactiva_trifasica(corriente_trifasica, tension, cos_fi), "VAr")
        elif option_selec == "6":
                corriente_monofasica = int(input("Ingrese el valor de la corriente: "))
                tension = int(input("Ingrese el valor de la tension de la red: "))
                cos_fi = float(input("ingrese el valor del coseno de fi: "))
                os.system("cls")
                print("\n El valor de la Potencia Reactiva Monofasica es: ", calcular_potencia_reactiva_monofasica(corriente_trifasica, tension, cos_fi) , "VAr")
        elif option_selec == "7":
                potencia_activa = float(input("Ingrese el valor de la potencia activa en KW: "))
                potencia_reactiva = float(input("ingrese el valor de lea potencia reactiva en KVAr: "))
                os:system("cls")
                print("\n Para corregir su Factor de Potencia a 0.98, necesitas un condensador de: ", correccion_factor_potencia(potencia_activa, potencia_reactiva), "VAr" )
        elif option_selec == "8":
                tension = float(input("ingrese el valor de la tension: "))
                frecuencia = float(input("ingrese el valor de la frecuencia en Hz: "))
                q_reactiva = float(input("Ingrese el valor de la potencia reactiva en VAr: "))
                os.system("cls")
                print("\n El valor de tu capacitor es: ", VAr_a_faradio(tension, frecuencia, q_reactiva), "microfaradio")
        elif option_selec =="9":
            break

    elif opcion == "2":
        print( "              Calculos en corriente continua: \n \n\
        [1] - Corriente\n\
        [2] - Tension\n\
        [3] - Resistencia\n\
        [4] - Potencia\n\
        [5] - Caida de Tension \n\
        [6] - Salir")
        opcion_cc == input("      Su eleccion es: ")
        if option_cc == "1":
            tension = float(input("Ingrese el valor de la tension: "))
            resistencia = float(input("Ingrese el valor de la resistencia: "))
            os.system("cls")
            print("El valor de la Corriente es: ", corriente(tension, resistencia), "Ampers")

       # elif option__cc == "2":
       #     corriente = float(input())

    elif opcion == "3":
        break