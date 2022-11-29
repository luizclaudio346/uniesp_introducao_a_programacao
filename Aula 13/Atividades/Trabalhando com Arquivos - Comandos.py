#/ABRIR E LER UM ARQUIVO

with open('arquivo.txt', 'r') as file_object:
    conteudo = file_object.read()
    print(conteudo)

#/PATH (CAMINHO)

with open('path_file_sample\\meu_nome.txt') as file_object:
    conteudo = file_object.read()
    print(conteudo)

with open('./path_file_sample/meu_nome2.txt') as file_object:
    conteudo = file_object.read()
    print(conteudo)

#/CONSTRUINDO UM PATH

#Variável com (path + nome do arquivo)
path = './path_file_sample/'
file = 'welcome_to_the_jungle.txt'
filename = path + file

#/LEITURA DO ARQUIVO E IMPRIMINDO POR LINHA

# Exemplo 1 - Pulando linha
with open(filename) as file_object:
    for linha in file_object:
        print(linha)

# Exemplo 2 - Sem pular linha
with open(filename) as file_object:
    for linha in file_object:
        print(linha.rstrip())

#/LEITURA DE ARQUIVOS POR LINHA

file_name = './pasta/nome.txt'

with open(file_name) as file_object:
    linhas = file_object.readlines()

for linha in linhas:
    print(linha.rstrip())

#/ESCRITA EM ARQUIVOS

file_name = './path_file_sample/writing.txt'

with open(file_name, 'w') as file_object:
    file_object.write("Eu amo programar em Java!\n")
    file_object.write("Eu amo programar em SQL!\n")
    file_object.write("Eu amo programar em Python!\n")

file_name = './path_file_sample/writing.txt'

with open(file_name, 'a') as file_object:
    file_object.write("Eu amo programar em Kotlin! \n")
