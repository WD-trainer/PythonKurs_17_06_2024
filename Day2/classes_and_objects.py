from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod



class Osoba:
    # imie = "Wojciech"
    # nazwisko = "Dudzik"
    # wiek = 31

    def __init__(self, imie: str, nazwisko:str, wiek:int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypiszMnie(self):
        print(self.imie, self.nazwisko, self.wiek)

    def __str__(self):
        return f'Cześć jestem: {self.imie}, {self.nazwisko}, {self.wiek}'

    def przywitaj_kolege(self, imie):
        print(f"Cześć {imie} jestem: {self.imie}")



# l = list()
o = Osoba("Wojciech", "Dudzik", 31)
#print(o.imie, o.wiek, o.nazwisko)
o.wypiszMnie()


# o.zawod = "Trener"
# print(o.zawod)

#o.imie = "Krzysztof" # *tak nie powinniśmy robić
print(o.imie, o.wiek, o.nazwisko)

o2 = Osoba(imie="Krzysztof", nazwisko="Nowak", wiek=32)
print(o2.imie, o2.wiek, o2.nazwisko)

lista_osob = [o, o2]

for osoba in lista_osob:
    print(osoba)

o.przywitaj_kolege("Przemysław")

print("*" * 45)

#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.


