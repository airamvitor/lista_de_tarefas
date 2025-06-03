# inicialização de variáveis
lista_de_tarefas = []
continuar = True
print("bem-vinde a sua lista de tarefas!")
print("-" * 50)
# cabeçalho do programa

def adicionar_tarefa(lista_de_tarefas, tarefa):
    # adiciona nova tarefa a uma lista pré-existente
    lista_de_tarefas.append(tarefa)
    print("tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
     # exibe lista de tarefas numerada
     print("*" * 50)
     print(f"{' ' * 20} lista de tarefas")
     print("-" * 50)
     n = 1
     for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n = n + 1
     print("-" * 50)   

def deletar_tarefa(lista_de_tarefas, tarefa):
    # deleta tarefa de uma lista pré-existente a partir do número dela
    lista_de_tarefas.pop(tarefa - 1)
    return lista_de_tarefas

def exbir_menu():
    # exibe menu com opções pro úsuario escolher
    print("Escolha uma opção:\n"
          "1 - Inserir nova tarefa\n"
          "2 - lista de tarefas\n"
          "3 - deletar tarefa\n" 
          "4 - sair"
          )
    print("-" * 50)
    
# loop principal
while continuar: 
    exbir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
         listar_tarefas (lista_de_tarefas)
    elif opcao == "3":
        # a validação verifica se o valor é numérico, se é menor ou maior que 0.
        tarefa = input('insira o numero da tarefa que deseja deletar: ')
        if  not tarefa.isnumeric():
            print("número inválido! tente novamente!")
        if int(tarefa) > len(lista_de_tarefas):
            print("número inválido! tente novamente!")
        elif int(tarefa) <= 0:
            print("número inválido! tente novamente.")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4":
        continuar = False  
    else:
        print("Opção inválida! Tente novamente.")
    print('\n') 
