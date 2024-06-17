import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools


def do_opakowania():
    print("Opakuj mnie")


def dekorator(funkcja):
    def opakowujaca():
        print('*' * 15)
        funkcja()
        print('*' * 15)

    return opakowujaca


@dekorator
def do_opakwoanie_2():
    print("Skladnia dekorator pythona")


if __name__ == '__main__':
    udekorowana = dekorator(do_opakowania)
    udekorowana()

    do_opakwoanie_2()


    # Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
    # Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()",
    def licz_czas(fun):
        def wew():
            poczatek = datetime.now()
            fun()
            koniec = datetime.now()
            print(f'Wywolanie trwalo {koniec - poczatek}')

        return wew


    @licz_czas
    def opakuj_mnie():
        #time.sleep(3)
        print("Robie ciekawe rzeczy w Pythonie")

    opakuj_mnie()

    @licz_czas
    def opakowanie_inne():
        print("inna funkcja")


    opakowanie_inne()


    def dekorator_z_1_parametrem(fun):
        def wew(liczba: int):
            print("Hurra działa z parametrem")
            print(fun(liczba))

        return wew


    @dekorator_z_1_parametrem
    def dodaj_cztery(liczba: int) -> int:
        return liczba + 4

    dodaj_cztery(2)




    def dekorator_do_funkcji_z_parameterami(fun):
        def wew(*args, **kwargs):
            print("Hurra działa zawsze")
            fun(*args, **kwargs)
            print("Po wszystkim")

        return wew


    @dekorator_do_funkcji_z_parameterami
    def dekorowana(x: str):
        print(f'siema {x}')
    @dekorator_do_funkcji_z_parameterami
    def dekorowana_bez_p():
        print(f'siema')

    dekorowana("Janek")
    dekorowana(x="Wojtek")
    dekorowana_bez_p()


    def star(func):
        def inner(*args, **kwargs):
            print("*" * 15)
            func(*args, **kwargs)
            print("*" * 15)

        return inner


    def percent(func):
        def inner(*args, **kwargs):
            print("%" * 15)
            func(*args, **kwargs)
            print("%" * 15)

        return inner


    @percent
    @star
    def printer(msg):    #  printer = percent(star(printer))
        print(msg)

    printer("Hello World")


    def hello_decorator(func):
        def inner1(*args, **kwargs):
            print("before Execution")

            # getting the returned value
            returned_value = func(*args, **kwargs)
            print("after Execution")

            # returning the value to the original frame
            return returned_value

        return inner1

    @hello_decorator
    def sum_two_numbers(a: int, b: int) -> int:
        print("Inside the function sum_two_numbers")
        return a + b


    result = sum_two_numbers(12,4)
    print(f"Wynik dodawania: 12 + 4 = {result}")


    # Dodaj dekorator który zliczy czas wykonywania tej funkcji z parametrami. Zaloguj na konsole wszystkie przekazane parametry




    def opakuj_mnie_z_parametrami(x, napis_do_wypisania):
        for i in range(x):
            time.sleep(1)
        print(f"Robie ciekawe rzeczy w Pythonie {napis_do_wypisania}")
        return 0


    returned_value = opakuj_mnie_z_parametrami(x=1, napis_do_wypisania="jestem cool")