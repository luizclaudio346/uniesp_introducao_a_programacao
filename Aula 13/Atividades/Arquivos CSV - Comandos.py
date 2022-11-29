#/LEITURA DE ARQUIVO CSV

import csv

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#/ESCRITA DE ARQUIVO CSV

import csv

with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(algum_interável)
