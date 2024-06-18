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
    def licz_czas_i_loguj(fun):
        @functools.wraps(fun)
        def wewnetrzna(*args, **kwargs):
            print(f'Argumenty {args}')
            print(f'Key-word arguments {kwargs}')
            poczatek = datetime.now()
            value = fun(*args, **kwargs)
            koniec = datetime.now()
            print(f'wywolanie trwalo {koniec - poczatek}')
            return value

        return wewnetrzna



    @licz_czas_i_loguj
    def opakuj_mnie_z_parametrami(x, napis_do_wypisania):
        """
        Ta funkcja spi przez x sekund a nastpenie wypisuje wiadomosc

        Parameters
        ----------
        x : int
        napis_do_wypisania

        Returns zawsze zwraca 0
        -------

        """
        for i in range(x):
            time.sleep(1)
        print(f"Robie ciekawe rzeczy w Pythonie {napis_do_wypisania}")
        return 0

    returned_value = opakuj_mnie_z_parametrami(x=1, napis_do_wypisania="jestem cool")


    print(opakuj_mnie_z_parametrami.__name__)
    #help(opakuj_mnie_z_parametrami)
    print(opakuj_mnie_z_parametrami.__doc__)


    def sleeper(sleep_time:float):
        def sleeper_decorator(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                time.sleep(sleep_time)
                returned_value = func(*args, **kwargs)
                return returned_value

            return inner

        return sleeper_decorator


    @sleeper(sleep_time=0.5)
    def slow_add(a: float, b: float) -> float:
        return a + b


    print(f'Wynik dodawania 2+2=')
    print(f'{slow_add(2, 2)}')

    # Stwórz dekorator, który sprawdza, czy użytkownik ma odpowiednie uprawnienia do wywołania funkcji. Jeśli nie, wyświetli komunikat o braku dostępu.

    user1 = {'name': 'Jan', 'permission': 'admin'}
    user2 = {'name': 'Anna', 'permission': 'user'}


    def check_permissions(required_permission):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(user, *args, **kwargs):
                if user.get('permission') == required_permission:
                    return func(user, *args, **kwargs)
                else:
                    print("Brak uprawnień do wykonania tej funkcji")

            return wrapper

        return decorator

    @check_permissions('user')
    def user_function(user):
        print("Witaj, użytkowniku!")


    @check_permissions('admin')
    def admin_function(user):
        print("Witaj, adminie!")


    admin_function(user1)  # Output: Witaj, adminie!
    admin_function(user2)  # Output: Brak uprawnień do wykonania tej funkcji
    user_function(user2)  # Output: Witaj, użytkowniku!
    user_function(user1)  # Output: Brak uprawnień do wykonania tej funkcji


    def count_calls(func):
        @functools.wraps(func)
        def wrapper_count_calls(*args, **kwargs):
            wrapper_count_calls.num_calls += 1
            print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}()")
            return func(*args, **kwargs)

        wrapper_count_calls.num_calls = 0
        return wrapper_count_calls


    @count_calls
    def hello():
        print("Hello world")

    hello()
    hello()
    hello()
    hello()


    # napisac dekorator cache ktory bedzie zapmietywał wynik wykonania danej funkcji i wypisac na ekran kiedy korzystamy z cachu
    def cache(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = args + tuple(kwargs.values())
            if cache_key not in wrapper.cache_dict:
                wrapper.cache_dict[cache_key] = func(*args, **kwargs)
                return wrapper.cache_dict[cache_key]
            else:
                print("Using cached value")
                return wrapper.cache_dict[cache_key]

        wrapper.cache_dict = {}
        return wrapper


    @cache
    def mnozenie(a:float, b:float) -> float:
        print(f'Wynik: {a * b}')
        return a * b


    mnozenie(2,2)
    mnozenie(2, 2)

    mnozenie(2, 3)
    mnozenie(3,2)

    mnozenie(b=3, a=2)


    def add_method_decorator(cls):
        # Define a new method to be added
        def new_method(self):
            return "This is a new method"

        # Add the new method to the class
        cls.new_method = new_method
        return cls


    # Apply the decorator to the class
    @add_method_decorator
    class MyClass:
        def __init__(self, value):
            self.value = value

        def display_value(self):
            return f"The value is {self.value}"


    # Create an instance of the class
    instance = MyClass(10)
    # Call the original method
    print(instance.display_value())  # Output: The value is 10
    # Call the new method added by the decorator
    print(instance.new_method())  # Output: This is a new method
