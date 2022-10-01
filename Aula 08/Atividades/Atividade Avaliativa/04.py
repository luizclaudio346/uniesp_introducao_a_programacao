#4.O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a 	condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.

massa = float (input ("Diga seu peso em quilograma:"))
altura = float (input("Diga a sua altura em metros:"))
imc = (massa/(altura**2))

if imc <18.5:
    print (f"Seu IMC é de {imc:.2f}")
    print ("Abaixo do peso ideal, procure um especialista")
elif 18.5< imc <24.99:
    print (f"Seu IMC é de {imc:.2f}")
    print ("Peso Normal")
elif 25< imc <30.00:
    print (f"Seu IMC é de {imc:.2f}")
    print ("Sobrepeso, procure um especialista")
else:
    print (f"Seu IMC é de {imc:.2f}")
    print ("Obesidade, procure um especialista")