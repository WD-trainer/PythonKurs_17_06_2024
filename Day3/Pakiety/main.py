import os

import pandas as pd
from numpy import zeros # import numpy as np

# from PodPakiet import functions
# from PodPakiet.functions import times3

from PodPakiet import times3


# stworzyli pakiet wypisywacz który będize zawiereał __init__.py - print z informacjami o pakiecie
# stworzy plik z pisacz, w nim napisz hello world i zaimportuj i wywołaj
# napiszcie dokumentacje dla hello world i wywołać dokumentacje tej funkcji z użyciem helpa


if __name__ == "__main__":
    print(os.getenv("PYTHONPATH"))

    print(zeros((3,3)))

    #print(f'3x3={functions.times3(3)}')

    print(f'3x3={times3(3)}')

    # print(times4(4))

