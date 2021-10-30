import time
import numpy as np
from sympy import *
from sympy.core import symbol


x = Symbol('x')
c = 0
teta = 0.618
contagem = 0

equacao = expand(input('Digite aqui a expressão: '))
iteracao = int(input("Digite aqui o número de iterações: "))

def iter(a1, b1):
    
    global lambda0
    lambda0 = b1 - teta * (b1 - a1)
    global flambda0
    flambda0 = equacao.subs(x, lambda0)
    
def iter2(a1, b1):
    global mi
    mi = a1 + teta * (b1 - a1)
    global fmi 
    fmi = equacao.subs(x, mi)
    

global a1
global b1
a1 = int(input("Digite aqui o primeiro intervalo: "))
b1 = int(input("Digite aqui o segundo intervalo: "))

while c <= iteracao:
    global lambda0
    lambda0 = b1 - teta * (b1 - a1)
    global flambda0
    flambda0 = equacao.subs(x, lambda0)

    global mi
    mi = a1 + teta * (b1 - a1)
    global fmi 
    fmi = equacao.subs(x, mi)
   
    if fmi > flambda0:
        a1 = a1 
        b1 = mi
        lambda0 = b1 - teta * (b1 - a1)
        flambda0 = equacao.subs(x, lambda0)
        mi = a1 + teta * (b1 - a1)
        fmi = equacao.subs(x, mi)
        c = c + 1
    else:
        a1 = lambda0
        b1 = b1
        lambda0 = b1 - teta * (b1 - a1)
        flambda0 = equacao.subs(x, lambda0)
        mi = a1 + teta * (b1 - a1) 
        fmi = equacao.subs(x, mi)
        c = c + 1

wki = (mi + lambda0)/2
print("O número máximo de iterações foi alcançado, o algoritmo retorna {} ".format(wki))