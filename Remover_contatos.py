import csv
import os

recebe = str(input("Deseja excluir algum contato já existente: ")).lower().strip()
cont_exclu = list()
cont_presente = list()
if recebe[0] == "s":
    num = int(input("Digite o numero de pessoas que deseja excluir: "))
    for i in range(num):
        print("-="*20)
        nome = input("Qual o nome do contato que deseja excluir: ")
        cont_exclu.append(nome)
        print("-=" * 20)

print(cont_exclu)
def excluir():
    with open("Contatos.csv", "r", encoding='utf-8') as leitura, open("Contatos.csv", "r", encoding='utf-8', newline="") as escrita:
        leitura_csv =  csv.reader(leitura, delimiter=";")
        for c in leitura_csv:
            for a in range(len(cont_exclu)):
                if c[0] ==  cont_exclu[a]:
                    cont_presente.append(cont_exclu[a])

excluir()
print(cont_presente)

