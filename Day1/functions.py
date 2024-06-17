import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools
from typing import Callable


def times2(a: int | list) -> str | int:  # Union[str, int]
    if a == 0:
        return "przez zero nie mnoze"
    return a * 2


if __name__ == '__main__':
    print(times2(2))

    print(times2("string"))

    print(type(times2([1, 2, 3, 4])))
    print(times2([1, 2, 3, 4]))

    def funckja_jako_argument(f: Callable, x: int):
        print(f(x))

    funckja_jako_argument(times2, 32)
    funckja_jako_argument(lambda arg: arg + 2, 3)


    def powieksz(x: str) -> str:
        return x.upper()
    def tytul(napis: str) -> str:
        return napis.title()
    def zastosuj_dla_wszystkich(fun, *strings):
        print(strings)
        for a in strings:
            print(fun(a))


    zastosuj_dla_wszystkich(powieksz, 'siała', 'baba', 'mak', 'aaaaa')
    zastosuj_dla_wszystkich(tytul, 'siała', 'baba', 'mak', )

    # Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args
    def moja_suma(*liczby):
        suma = 0
        for i in liczby:
            suma += i
        return suma

    suma = moja_suma(1,2,3,4,5,15,18,50)
    print(suma)

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]

    print(moja_suma(*list1, *list2, *list3))  # *list1 = 1,2,3

    def my_sum(a, b, c):
        print(f"a={a}")
        print(a + b + c)

    slownik = {"a": 4, "b": 3, "c": 2}
    my_sum(**slownik)

    my_sum(*list1)
    #my_sum(*list3) # tu bedzie blad TypeError: my_sum() takes 3 positional arguments but 4 were given

    def pomnoz_razy_dwa(x):
        return x * 2
    def podziel_przez_trzy(x):
        return x / 3
    def dodaj_piec(x):
        return x + 5

    # napisz funkcje aplikuj ktora dostanie jako parametr wartosc i dowolna liczbe funkcji. Następnie zaaplikuje wszystkie te funkcje dla podajnej wartosci i zwroic ja


