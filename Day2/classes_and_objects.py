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
class Samochod:
    def __init__(self, marka:str, model:str, kierowca: Osoba, rejestracja:str = "DOMYSLNA"):
        self.__marka = marka
        self.model = model
        self.rejestracja = rejestracja
        self.kierowca = kierowca

    def wyswietl(self):
        print(f"Samochod: {self.__marka}, {self.model}, {self.rejestracja}, {self.kierowca}")

    def __str__(self):
        return f'Samochod: {self.__marka}, {self.model}, {self.rejestracja}, {self.kierowca}'

    def __repr__(self):
        return f'Samochod("{self.__marka}", "{self.model}", "{self.rejestracja}")'

    def _funckje_dla_mechanika(self):
        print("Naprawiam")


s1 = Samochod("Opel", "Astra", o)
s2 = Samochod("Audi", "R8", kierowca=o2, rejestracja="KR12345")

s1.wyswietl()
s2.wyswietl()

napis_z_samochod =  str(s1)
print(napis_z_samochod)

s1._funckje_dla_mechanika()
# print(s1.__marka) # tu bedzie blad

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        print("Get radius")
        return self._radius

    def set_radius(self, value):
        print("Set radius")
        self._radius = value

    radius = property(fget=get_radius,
                      # fset=set_radius,
                      doc="Radius property of circle")

kolo = Circle(20)

print(kolo.radius)
try:
    kolo.radius = 30
except Exception as err:
    print(err)


class Rectangle:
    def __init__(self, a:int, b:int):
        self._a = a
        self.b = b

    @property
    def a(self):
        print("Get a")
        return self._a

    # @a.setter
    # def a(self, value):
    #     print("Set a")
    #     self._a = value


r = Rectangle(4,2)
r.b = 8
# r.a = 30
print(f'Rectangle {r.a}, {r.b}')


# Stwórz klasę Zawodnik posiadającą pola wzrost i masa, imie. Pola te mają być uzupełniane przy tworzeniu obiektu.
# stworz atrybut BMI który będzie tylko do odczytu
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.
# Wzrost jest atrybutem chronionym (__wzrost)
# Waga może być zmieniana ale też jako atrybut z wykorzystaniem dekoratora @property
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84




