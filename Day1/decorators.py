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







    def opakuj_mnie():
        # time.sleep(3)
        print("Robie ciekawe rzeczy w Pythonie")