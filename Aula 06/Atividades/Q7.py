#7. Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
email = input("Digite o seu e-mail: ")

cadastro = nome, idade, email

lista = [cadastro]

for cadastro in lista:
    print(f"Nome:{nome}, Idade:{idade}, E-mail:{email}. Registrado com sucesso.")