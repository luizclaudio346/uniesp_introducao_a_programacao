#1. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

Quantidade = int(input("Olá, Bom dia, quantas maçãs você deseja?"))

maçãs = 1.30

dúzia = 1.00

if Quantidade < 12:
    print(f"Tá bom, Custará R${maçãs * Quantidade:.2f}")
elif Quantidade >= 12:
    print(f"Tá bom, Custará R${dúzia * Quantidade:.2f}")
else:
    print("maçãs!")
