# gerenciador de tarefas

import os
import json


# função para carregar tarefas
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    return []


# Exibe todas as tarefas
def listar_tarefas(tarefas):
    print("Tarefas: ")
    for tarefa in tarefas:
        status = "Concluida" if tarefa['pronta'] else "Pendente"
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}, Status: {status}")


# Escreve no arquivo e salva as tarefas
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


# gerar id
def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1]['id'] + 1


# adicionar tarefas
def adicionar_tarefa(tarefas):
    print("Adicionar nova tarefa")
    titulo = input("Título: ")
    descricao = input("Descrição: ")

    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'pronta': False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")


# concluir tarefa
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa que você deseja concluir: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['pronta']:
                    print("A tarefa já esta concluida.")
                else:
                    tarefa['pronta'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluida com sucesso!")
                return
        print("Tarefa não encontrada")
    except ValueError:
        print("ID inválido")


# remover tarefa
def excluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa que você deseja remover: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                tarefas.remove(tarefa)
                salvar_tarefas(tarefas)
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa não encontrada")
    except ValueError:
        print("ID inválido")


# menu principal
def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")


# Loop das açoes
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            excluir_tarefa(tarefas)
        elif opcao == '5':
            print("Encerrando programa")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    main()
