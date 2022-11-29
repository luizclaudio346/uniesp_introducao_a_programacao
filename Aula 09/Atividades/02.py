#Use um dicionário para armazenar os números favoritos de algumas pessoas. Esoclha cinco colegas, e pergunte quais seus número favoritos. Use seus nomes para serem as chaves de cada número favorito. Ao final, exiba o nome de cada pessoas e seu número favorito.


nfav = {"Luiz": 19, "Lucas": 10, "Gabriela": 13, "Diego": 17, "Matheus": 8}

for r,s in nfav.items():
    print(f'O número preferido de {r} é {s}.')