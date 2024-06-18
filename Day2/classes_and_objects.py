from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass



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
class Zawodnik:
    def __init__(self, wzrost: float, masa: float, imie: str):
        self.__wzrost = wzrost
        self._masa = masa
        self._imie = imie

    @property
    def BMI(self):
        return self._masa / (self.__wzrost ** 2)

    @property
    def waga(self):
        return self._masa

    @waga.setter
    def waga(self, value: float):
        self._masa = value

    def __str__(self):
        return f'Zawodnik: {self._imie}, o BMI={self.BMI:.3f}'


    @classmethod
    def create_from_string(cls, text:str):
        dane = text.strip().split(';')
        if len(dane) == 3:
            wzrost_cm, waga_lbs, imie = dane
            z = cls(wzrost=int(wzrost_cm) / 100, masa=int(waga_lbs) * 0.454, imie=imie)
            return z

    @staticmethod
    def nie_uzywam_atrybutow(info:str):
        print(info)

    # odczytali dane z pliku dane.txt
    # zbudowali sobie liste zawodnikow (jako obietky klasy) przy uzyciu  @classmethod
    @classmethod
    def create_from_file(cls, path_to_file: str):
        zawodnicy = []
        with open(path_to_file, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    zawodnicy.append(cls(masa=float(waga), wzrost=float(wzrost), imie=imie))
        return zawodnicy

    def __lt__(self, other):
        return self.BMI < other.BMI


z = Zawodnik(1.8, 80, "Jan")
print(z)

z2 = Zawodnik.create_from_string("176;150;Paweł")
print(z2)
z2.waga = 75
print(z2)
z2.nie_uzywam_atrybutow("Jakies inne informacje")


list_zawodnikow = Zawodnik.create_from_file("dane.txt")
print(list_zawodnikow[0])

# nowa_lista_posortowana = sorted(list_zawodnikow, key=lambda x: x.BMI)

# for z in nowa_lista_posortowana:
#     print(z)

list_zawodnikow.sort()

for z in list_zawodnikow:
    print(z)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        yield self.x
        yield self.y

    def __contains__(self, value):
        return value == self.x or value == self.y

    def __hash__(self):
        return hash((self.x, self.y))


v1 = Vector2D(3, 4)
v2 = Vector2D(5, 6)

print(repr(v1))
print(str(v2))

print(v1 == v2)  # __eq__
print(v1 + v2)  # __add__: Vector(8, 10)
print(v2 - v1)
print(v1 * 2)

print(len(v1))  # __len__: 2
print(v1[0], v1[1])  # __getitem__: 3 4

for coordinate in v2:  # __iter__
    print(coordinate)

print(5 in v2)  # __contains__

hash_value = hash(v1)  # __hash__
print(hash_value)

v1[0] = 15  # __setitem__
print(v1)

# v1()


# Napisz klase Timer która będzie mierzyła czas wykonania funkcji jako context menager.
# klasa ta w zaleznosci od zmiennej verbose bedzie wypisywała na ekran czas wykonania przy wyjsciu z contextu
# from timeit import default_timer as timer
timer_obj = timer
start = timer_obj()
# cos co mierzymy
end = timer_obj()
#def __enter__(self):
#def __exit__(self, *args):


with Timer(verbose=True) as t:
    # time.sleep(3)
    print("Moja bardzo długa funkcja")













# https://docs.python.org/3/library/dataclasses.html


# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     age: int
#
#
# person1 = Person('Jan', 'Kowalski', 30)
# person2 = Person('Anna', 'Nowak', 25)
#
# print(person1)
# print(person2)
#
# print(person1 == person2)


