#/CENÁRIO

#Situação Problema 
###Lembra da API da aula passada? Vamos utilizá-la para programar nossa folga para estes próximos dias. Precisamos receber o tempo, nas localidades de Pipa-RN, Maragogi-AL, Baía Formosa-PB, Praia dos Carneiros-PE. 
# Vamos aprender como podemos fazer isso?


#/CRIANDO UM JSON

import json
# Defini-se os dados
x = [1, 'simple', 'list']
# Comando de saída do JSON
json.dumps(x)
# Salvando em um arquivo
json.dump(x, arquivo)

#/CARREGAR (LER) UM ARQUIVO JSON

x = json.load(arquivo)

