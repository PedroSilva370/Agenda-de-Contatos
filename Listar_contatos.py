import Add_contatos
import csv
import os

dados_contato = Add_contatos.dados_total
lista_coluna_1 = ["Numero de contato","Contato", "Telefone", "E-mail"]
def armazena():
    with open("Contatos.csv", "a", newline='', encoding='utf-8') as objeto_de_arquivo:
        objeto_csv = csv.writer(objeto_de_arquivo, delimiter=";")
        objeto_csv.writerow(lista_coluna_1)
        for indice,contato in enumerate(dados_contato):
            objeto_csv.writerow([indice, contato[0], contato[1], contato[2]])

armazena()
