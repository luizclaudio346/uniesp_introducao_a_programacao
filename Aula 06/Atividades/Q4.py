#4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

number = int(input("Digite um número para obter a tabuada do mesmo: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")