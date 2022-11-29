#Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu dicionário.

dic={
    'Primeiro_nome': 'Luiz Claudio',
    'Sobrenome': 'da Silva Aguiar Filho',
    'Idade': '18',
    'Cidade':'João Pessoa'
}

for info in dic.items():
    print(info)