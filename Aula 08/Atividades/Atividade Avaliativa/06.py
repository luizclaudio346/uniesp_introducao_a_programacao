# 6.Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

def main():
    A = int(input("Digite o valor de A: "))
    fat = 1
    i = 2
    while i <= A:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é =" %A, fat)

main()