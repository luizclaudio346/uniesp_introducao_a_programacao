#3. Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
#A) O valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#B) O valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

Q=[]

while len(Q) <20:
    num=int(input("Digite Numeros Inteiros para adiciona-los na lista:"))
    if num in Q:
       print('Numero repetido, digite outro')
    
    elif num < 0:
        print("Digite apenas Numeros Positivos")
        
    else:
        Q.append(num)
        
menval=Q[0]
maval=Q[0]

for valor in Q:
    if valor > maval:
        maval=valor
        
print(f'O valor do maior elemento de Q é {maval} e seu índice é {Q.index(maval)}')

for valor in Q:
    if valor < menval:
        menval=valor

print(f'O valor do menor elemento de Q é {menval} e seu índice é {Q.index(menval)}')
