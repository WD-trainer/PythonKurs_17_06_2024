from collections.abc import Iterator

from classes_and_objects import Zawodnik


class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


for e in IncrementIterator(10):
    print(e)

lista = [1,2,3,4]

suma = 0
for element in lista:
    suma += element


# uzupełnic klase lista zwodnikow o metody __iter__ oraz __next__
class ListaZawodnikow(Iterator):
    def __init__(self, path: str):
        self.zawodnicy = []
        with open(path, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    self.zawodnicy.append(Zawodnik(masa=float(waga), wzrost=float(wzrost), imie=imie))
        self.index = 0

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.index == len(self.zawodnicy):
            raise StopIteration
        self.index += 1
        return self.zawodnicy[self.index - 1]


nasza_lista = ListaZawodnikow("dane.txt")
for z in nasza_lista:
    print(z)



class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))


class TreeIterator:
    def __init__(self, root):
        self.stack = [root] if root else []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)

        return node.value


iterator = TreeIterator(tree)

for value in iterator:
    print(value)


nasza_lista = ListaZawodnikow("dane.txt")
zawodnik = next(nasza_lista)
print(zawodnik)


class MiesiaceIterator:
    def __init__(self):
        self.miesiace = [
            "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.miesiace):
            miesiac = self.miesiace[self.indeks]
            self.indeks += 1
            return miesiac
        else:
            raise StopIteration

    def restart(self):
        self.indeks = 0


# Użycie iteratora
miesiace_iterator = MiesiaceIterator()
next(miesiace_iterator)
next(miesiace_iterator)
next(miesiace_iterator)
#miesiace_iterator.restart()

print("Miesiące:")
for i in range(12):
    print(next(miesiace_iterator))
