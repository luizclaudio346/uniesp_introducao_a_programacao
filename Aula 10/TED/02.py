# 2) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

import random
from turtle import rt

numero =int(input('digite um número: '))
vetor = []

for i in range(30):
    t = random.randint(0,10)
    vetor.append((t))
rt = vetor.count(numero)
print(vetor)
print(rt)