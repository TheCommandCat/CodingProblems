from re import A
import numpy as np

b = np.zeros((8, 8), dtype=int)


def atn(letter):
    return ord(letter) - 65

def fctl(code):
    print(code)
    l = [i for i in code][0]
    n = [i for i in code][1]
    print(atn(l), int(n) - 1)
fctl('A2')