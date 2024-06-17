import operator
import random
import os
import re
from collections import defaultdict


if __name__ == '__main__':
    slownik = {}
    slownik2 = dict()

    info = {
        "LG123": "Telewizor 60' z HD Ready, wejściem na internety ifiltrem reklam",
        "SONY666": "Piekielnie dobry telewizor",
        "SZAJSUNG999": "Telewizor świetnie nadający się do zakrycia dziury w ścianie(i niczego więcej)"
    }

    print(info)
    print(info["LG123"])
    print(info.keys())
    print(info.values())

    for i in info:
        print(f'i = {i}')
        print(f'info[i] = {info[i]}')

    for key in info.keys():
        print(info[key])

    if "LG123" in info:
        print("Mamy LG")
    else:
        print("niet :(")

    info["KLUCZ"] = "WARTOŚĆ"

    for i in info:
        print(f'i = {i}')
        print(f'info[i] = {info[i]}')


    people = {}

    with open("dane.txt", "r") as file:
        for line in file:
            line_splited = line.rstrip().split(';')
            people[line_splited[0]] = (line_splited[1], line_splited[2])

    #print(people)

    for key, value in people.items():
        print(f"Key: {key}: value: {value}")

    # wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a
    # druga przypisane do nich wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

    ustawienia = {}

    with open("ustawienia.txt", "r") as file:
        for line in file:
            line = line.strip().split(';')
            if len(line) == 2:
                key, value = line
                ustawienia[key] = value

    for key, value in ustawienia.items():
        print(f'Klucz: {key}, wartosc: {value}')


    studenci = {
    1001: {'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 21, 'oceny': [4, 3, 5, 4]},
    1002: {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 22, 'oceny': [5, 5, 4, 5]},
    1003: {'imie': 'Marek', 'nazwisko': 'Zielinski', 'wiek': 23, 'oceny': [3, 4, 2, 3]},
    1004: {'imie': 'Zofia', 'nazwisko': 'Wiśniewska', 'wiek': 20, 'oceny': [4, 4, 4, 4]},
    1005: {'imie': 'Krzysztof', 'nazwisko': 'Wojcik', 'wiek': 24, 'oceny': [2, 3, 2, 3]}
    }

    list_of_names = [studenci[id]['imie'] for id in studenci]
    print(list_of_names)

    #  Oblicz średnią ocenę dla każdego studenta i dodaj ją do ich słownika
    for id in studenci:
        oceny = studenci[id]['oceny']
        srednia = sum(oceny) / len(oceny)
        studenci[id]['srednia_ocen'] = srednia

    print(studenci)

    nazwiska = ['Kowalski', 'Nowak', 'Zielinski', 'Wiśniewska', 'Wojcik']
    dlugosci_nazwisk = {nazwisko: len(nazwisko) for nazwisko in nazwiska if len(nazwisko) > 6}
    print(dlugosci_nazwisk)

    #  Znajdź studentów, którzy mają średnią ocenę powyżej 4.0
    studenci_pow_4 = {id: dane for id, dane in studenci.items() if dane['srednia_ocen'] > 4.0}
    print("Studenci ze średnią oceną powyżej 4.0:", studenci_pow_4)


    # lambda argumenty : wyrażenie
    p = lambda argumenty: print(argumenty)
    p("moj napis")

    # Tak nie robić !!! to juz za duzo na lambde
    calculate = lambda x, y: x + y if x > y else x - y
    print(calculate(5, 10))

    # lepiej tak
    def calculate(x, y):
        if x > y:
            return x + y
        else:
            return x - y


    liczby = [1, 2, 3, 4, 5]
    powers = list(map(lambda x: x ** 2, liczby))
    print(powers)

    #########

    najgorszy_student = min(studenci.items(), key=lambda item: item[1]['srednia_ocen'])
    studenci.pop(najgorszy_student[0])
    print("Studenci po usunięciu najgorszego:", studenci)


    employees = [{"name": "John", "salary": 50000}, {"name": "Jane", "salary": 55000}, {"name": "Jim", "salary": 60000}]
    highest_salary_employee = max(employees, key=lambda x: x["salary"])
    print(highest_salary_employee)

    # Posortuj studentów według nazwiska - sorted
    studenci_posortowani = dict(sorted(studenci.items(), key=lambda item: item[1]['nazwisko']))
    print("Studenci posortowani według nazwiska:", studenci_posortowani)


    ############### Sets - zbiory / zestawy
    list1 = [1, 2, 3, 4, 5, 5]
    list2 = [4, 5, 6, 7, 8]

    # Convert lists into sets
    set1 = set(list1)
    set2 = set(list2)

    print(list1)
    print(set1)

    # Perform set operations
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1 = set1.difference(set2)
    difference_set2 = set2.difference(set1)
    symmetric_difference_set = set1.symmetric_difference(set2)

    # Display the results
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference of Set 1 - Set 2:", difference_set1)
    print("Difference of Set 2 - Set 1:", difference_set2)
    print("Symmetric Difference:", symmetric_difference_set)



    ##### default dict

    nazwa_pliku = 'text.txt'
    wystapienia = {}
    # Defining the dict
    wystapienia2 = defaultdict(int)  # from collections import defaultdict

    with open(nazwa_pliku, "r", encoding='utf-8') as plik:
        for linia in plik:
            linia_wyczyszczona = re.sub(r'\W+', ' ', linia)
            slowa = linia_wyczyszczona.lower().split()
            for slowo in slowa:
                if slowo in wystapienia:  # https://www.geeksforgeeks.org/defaultdict-in-python/
                    wystapienia[slowo] += 1
                else:
                    wystapienia[slowo] = 1

                wystapienia2[slowo] += 1

    print(wystapienia)

    posortowane_wystapienia = sorted(wystapienia.items(), key=lambda x: x[1], reverse=True)
    print(posortowane_wystapienia)