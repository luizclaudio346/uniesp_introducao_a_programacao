cadastros = []

botão = 1000
while botão != 0:
    print("Digite 1 para cadastrar um novo usuário")
    print("Digite 2 para imprimir todos os usuários")
    print("Digite 0 para sair")
    botão = int(input("Digite a opção desejada:"))
    
    if botão == 1:
        # Entrada dos dados
        nome = input("Digite o nome:")
        idade = input("Digite a idade:")
        email = input("Digite seu email:")
        #Folha de cadastro 
        dados = [nome, idade, email]
        #Guardando a folha na pasta
        cadastros.append(dados)

    
    elif botão == 2:

        for p in cadastros:
            print(p)
            

    elif botão == 0:
        print("Obrigado por acessar este software!")

    else:
        print("Digite um número válido!")
