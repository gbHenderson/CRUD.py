import time
import mysql.connector
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    database='cadastropessoas')
cursor = conexao.cursor()
consulta = "Select * from pessoasindex"
cursor.execute(consulta)
linhas = cursor.fetchall()
for lis in range(0, len(linhas)):
    print("{} - {}".format(linhas[lis][0], linhas[lis][1]))
if len(consulta) == 0:
    ordem = 1
else:
    ordem = int(len(linhas)) + 1
while True:
    print("\nOpções:")
    menu = input("[1] - Adicionar nome\n"
                 "[2] - Remover nome\n"
                 "[3] - Editar nome\n"
                 "[4] - Sair\n"
                 "Digite uma opção: ")
    if menu == '1':
        while True:
            pessoa = (input("\nDigite o nome de uma pessoa: ")).strip().title()
            comando = f'INSERT INTO pessoasindex (id, nome) VALUES ("{ordem}", "{pessoa}");'
            cursor.execute(comando)
            conexao.commit()
            ordem += 1
            print('Adicionando...')
            time.sleep(1.3)
            cont = (input('Deseja continuar?[S/N] ')).upper()[0]
            if cont == 'N':
                break
    if menu == '2':
        while True:
            indice_exclui = int(input('\nDigite o indice do nome que deseja excluir: '))
            apagar = f"delete from pessoasindex where id = '{indice_exclui}'"
            cursor.execute(apagar)
            conexao.commit()
            print('Apagando...')
            time.sleep(1.3)
            cont2 = 0
            for muda in range(indice_exclui, len(linhas) + 1):
                muda_index = f'update pessoasindex set id = "{muda - 1}" where id = "{muda}";'
                cursor.execute(muda_index)
                conexao.commit()
            print("\nNova lista:")
            consulta_nova = "Select * from pessoasindex"
            cursor.execute(consulta_nova)
            linhas_nova = cursor.fetchall()
            for lis_nova in range(0, len(linhas_nova)):
                print("{} - {}".format(linhas[lis_nova][0], linhas_nova[lis_nova][1]))
            cont2 = (input('Deseja continuar?[S/N] ')).upper()[0]
            if cont2 == 'N':
                break
    if menu == '3':
        while True:
            indice_edita = int(input('\nDigite o indice do nome que deseja editar: '))
            troca = str(input("Digite o nome atual: ")).title().strip()
            troca_nome = f'update pessoasindex set nome = "{troca}" where id = "{indice_edita}";'
            cursor.execute(troca_nome)
            conexao.commit()
            print('Editando...')
            time.sleep(1.3)
            print("\nNova lista:")
            consulta_nova = "Select * from pessoasindex"
            cursor.execute(consulta_nova)
            linhas_nova = cursor.fetchall()
            for lis_nova in range(0, len(linhas_nova)):
                print("{} - {}".format(linhas[lis_nova][0], linhas_nova[lis_nova][1]))
            cont3 = (input('Deseja continuar?[S/N] ')).upper()[0]
            if cont3 == "N":
                break
    if menu == '4':
        cursor.close()
        conexao.close()
        print("\nFinalizando programa...")
        time.sleep(1.5)
        print("Programa finalizado!")
        break
    print("\nAs pessoas cadastradas são: ")
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for lis in range(0, len(linhas)):
        print("{} - {}".format(linhas[lis][0], linhas[lis][1]))
