#6. Seja criativo ao desenvolver este programa.

#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

Guests_list = ["Denzel Washington","Nicolas Cage","Samuel L. Jackson","Anne Hathaway","Bruce Willis"]

#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.

for name in Guests_list:
    print(f"{name}, I am pleased to invite you for a chat and then for dinner, at my residence, Nove Ipanema, at Rua Prudente de Morais, 564. Friday, July 10, at 6:00 p.m.")

#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.

print("Due to his schedule, Bruce Willis can´'t come to my dinner.")

#d. Modifique sua lista, substitua os desistentes por novos convidados.

Guests_list = ["Denzel Washington","Nicolas Cage","Samuel L. Jackson","Anne Hathaway","Sandra Bullock"]

#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

for name in Guests_list:
    print(f"{name}, I am pleased to invite you for a chat and then for dinner, at my residence, Nove Ipanema, at Rua Prudente de Morais, 564. Friday, July 10, at 6:00 p.m.")
