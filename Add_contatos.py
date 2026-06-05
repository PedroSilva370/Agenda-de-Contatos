#FUNÇÃO QUE ADICIONA OS CONTATOS
quant =  int(input("Quantos contatos deseja adicionar?: "))
dados_total = list()

for c in range(quant):
    lista_contato = list()
    print('=-'*20)
    nome = input("Qual o nome do contato?: ")
    tele = input("Qual o telefone do contato?: ")
    email = input("Qual o e-mail do contato?: ")
    print('=-' * 20)
    lista_contato.append(nome)
    lista_contato.append(tele)
    lista_contato.append(email)
    dados_total.append(lista_contato)

