import os

import pandas as pd
from numpy import zeros # import numpy as np

# from PodPakiet import functions
# from PodPakiet.functions import times3

from PodPakiet import times3



# stworzyli pakiet wypisywacz który będize zawiereał __init__.py - print z informacjami o pakiecie
# stworzy plik z pisacz, w nim napisz hello world i zaimportuj i wywołaj
# napiszcie dokumentacje dla hello world i wywołać dokumentacje tej funkcji z użyciem helpa
from wypisywacz import pisacz
# import wypisywacz.pisacz as np # tak nie robimy



# Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.
# W tym module dopisz funkcje walidacji danych dla funkcji BMI - czy waga < 200 i 1.00 < wzrost < 2.50. Jesli warunek nie jest spelniony
# rzuc wyjatkiem Value error.
# W pliku __init__.py ustaw zmienna __all__ tak aby tylko funkcja liczac BMI byla widoczna po imporcie pakietu
import BodyMassIndex as bmi
#from BodyMassIndex import calculate_bmi


# PYTHONPATH jest istotny
from Day1.functions import times2

#Nazwy modułów
#Importy cykliczne
#Importy relatywne - relative paths

if __name__ == "__main__":
    print(os.getenv("PYTHONPATH"))

    print(zeros((3,3)))

    #print(f'3x3={functions.times3(3)}')

    print(f'3x3={times3(3)}')

    # print(times4(4))
    pisacz.hello_world()
    help(pisacz.hello_world)

    try:
        height = [2.11, 1.80]
        weight = [100, 400]
        for h, w in zip(height, weight):
            bmi_result = bmi.calculate_bmi(h, w)
            print("Your BMI is:", bmi_result)
    except ValueError as e:
        print("Error:", e)

