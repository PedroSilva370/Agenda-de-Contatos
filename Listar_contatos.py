import Add_contatos
import csv
import os

dados_contato = Add_contatos.dados_total
lista_coluna_1 = ["Numero de contato","Contato", "Telefone", "E-mail"]
def armazena():
    with open("Contatos.csv", "a", newline='', encoding='utf-8') as objeto_de_arquivo:
        objeto_csv = csv.writer(objeto_de_arquivo, delimiter=";")
        for contato in dados_contato:
            objeto_csv.writerow([contato[0], contato[1], contato[2]])

def leitura():
    with open("Contatos.csv", "r", newline='', encoding='utf-8') as objeto_de_leitura:
        objeto_csv_leitura = csv.reader(objeto_de_leitura, delimiter=";")
        for linha, conteudo in enumerate(objeto_csv_leitura):
            if linha == 0:
                continue
            print("-="*20)
            print(f"Contato: {conteudo[0]}")
            print(f"Telefone: {conteudo[1]}")
            print(f"E-mail: {conteudo[2]}")
            print("-=" * 20)

armazena()