from connection_db import connect_bd
from security import *
import time
import os
import webbrowser


connection = connect_bd()

def insert(connection):

    cursor = connection.cursor()

    nome_produto = input("Informe o nome do produto: ")
    valor = float(input("Informe o valor do produto: "))

    query = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}" , "R${valor}")'

    cursor.execute(query)  # Roda o comando
    connection.commit()  # Edita o banco de dados

    cursor.close()
    connection.close()

def delete(connection):

    cursor = connection.cursor()

    idVendas = int(input("Informe PELO ID o item que deseja deletar: "))

    query = f'DELETE FROM vendas WHERE idVendas = {idVendas}'

  
    cursor.execute(query)  # Roda o comando
    connection.commit()  # Edita o banco de dados

    cursor.close()
    connection.close()

def update(connection):

    cursor = connection.cursor()

    opcao = input("Deseja alterar o NOME ou VALOR do produto? ").lower()
    idVendas = int(input("Informe QUAL O ID do produto que deseja alterar: "))

    if (opcao == 'nome'):
        nome_produto = input("Informe o novo nome do produto: ")

        query = f'UPDATE vendas SET nome_produto = "{nome_produto}" WHERE idVendas = {idVendas}'

    elif (opcao == 'valor'):
        valor = int(input("Informe o novo valor do produto: "))

        query = f'UPDATE vendas SET valor = "{valor}" WHERE idVendas = {idVendas}'

    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()

def read(connection):
    
    cursor = connection.cursor()
    print("Lendo a base de dados...")

    print()
    print("TABELA (vendas) disponível para consulta... ")
    tabela = input("Informe em qual tabela deseja realizar a pesquisa: ")
    

    query = f'SELECT * FROM {tabela}'

    cursor.execute(query)

    resultado = cursor.fetchall() #Ler o banco de dados
    
    print()
    print(resultado) if resultado else print("Nenhum resultado encontrado para a consulta.")

    
    option = input("Deseja adicionar um novo produto? SIM ou NAO? ")

    match option:

        case "sim":
            os.system('cls')
            insert(connection)

        case "nao":
            print("Deixando o programa.... até mais!")

    

    time.sleep(30)

def open_info_dev():
    try:
        webbrowser.open("https://www.linkedin.com/in/renanolv/")
        # Operador ternário - simplifica IF
        print("ABRINDO LINKEDIN DO DESENVOLVEDOR ...") if open else print(" ERRO ...")
    
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o LinkedIn: {e}")

def main(): 

    print(" ________________________________________________________")
    print(" _                                                     _ ")
    print(" _    INSERIR NOVO PRODUTO                    (1)      _ ")
    print(" _    VISUALIZAR PRODUTOS                     (2)      _ ")
    print(" _    ATUALIZAR PRODUTO                       (3)      _ ")
    print(" _    DELETAR PRODUTO                         (4)      _ ")
    print(" _    INFORMAÇÕES DO DESENVOLVEDOR            (5)      _ ")
    print(" -    SAIR                                    (6)      _")
    print(" _______________________________________________________ ")

    print()
    option = int(input("Informe uma das opções do CRUD acima: "))


    match option: 

        case 1:
            print()
            print("Você escolheu a opção de inserir um produto na base de dados... ")
            insert(connection)

        case 2:
            read(connection)

        case 3:
            update(connection)

        case 4:
            delete(connection)

        case 5: 
            open_info_dev()

        case 6:
            print("Você resolveu nos deixar... Até breve!")
    
main()
