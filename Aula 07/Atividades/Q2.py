#2. Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

idade = int(input("Digite seu ano de nascimento:"))

if idade < 2006:
    print("Você estar apto para votar este ano. Caso não tenha Título de Eleitor ou necessita de ajuda referente ao mesmo, entre no Site do Tse. https://www.tse.jus.br/eleitor/titulo-de-eleitor/tudo-sobre-titulo-de-eleitor/")
elif idade >= 2007:
    print("Você não estar apto para votar este ano, em decorrência de seu ano de nascimento, aguarde a idade mínima de 16 anos.")