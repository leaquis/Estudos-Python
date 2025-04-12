# gerenciador de tarefas

import os
import json
import csv
from datetime import datetime


# função para carregar tarefas
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []


# Exibe todas as tarefas
def listar_tarefas(tarefas):
    print("\nTarefas Pendentes: ")
    tarefas_pendentes = [t for t in tarefas if not t['pronta']]
    tarefas_pendentes = sorted(tarefas_pendentes, key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    for tarefa in tarefas_pendentes:
        data_obj = datetime.strptime(tarefa['data'], '%d/%m/%Y')
        status_atrasado = " [ATRASADA]" if data_obj.date() < datetime.now().date() else ""
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}, Data: {tarefa['data']}{status_atrasado}")
    
    print("\nTarefas Concluídas: ")
    tarefas_concluidas = [t for t in tarefas if t['pronta']]
    tarefas_concluidas = sorted(tarefas_concluidas, key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    for tarefa in tarefas_concluidas:
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}, Data: {tarefa['data']}")


# Escreve no arquivo e salva as tarefas
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


# gerar id
def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1]['id'] + 1
    else:
        return 1


# adicionar tarefas
def adicionar_tarefa(tarefas):
    print("Adicionar nova tarefa")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_input = input("Data de conclusão (dd/mm/aaaa): ")
    try:
        data_obj = datetime.strptime(data_input, '%d/%m/%Y')
        data = data_obj.strftime('%d/%m/%Y')
        if data_obj.date() < datetime.now().date():
            print("Data de conclusão não pode ser no passado.")
            return
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa.")
        return

    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'data': data,
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


# pesquisar tarefa
def pesquisar_tarefas(tarefas):
    termo = input("Digite o termo de pesquisa: ").lower()
    resultados = [t for t in tarefas if termo in t['titulo'].lower() or termo in t['descricao'].lower()]
    if resultados:
        print(f"\nTarefas que contêm '{termo}': ")
        for tarefa in resultados:
            status = "Concluida" if tarefa['pronta'] else "Pendente"
            print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Status: {status}, Data: {tarefa['data']}")
    else:
        print("Nenhuma tarefa encontrada com o termo especificado.")


# ordenar tarefas
def ordenar_tarefas(tarefas):
    tarefas.sort(key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    salvar_tarefas(tarefas)
    print("Tarefas ordenadas por data de conclusão com sucesso!")


# editar tarefas
def editar_tarefas(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa que você deseja concluir: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                print(f"Editar Tarefa ID {id_tarefa}: ")
                novo_titulo = input(f"Novo Título (atual: {tarefa['titulo']}): ") or tarefa['titulo']
                nova_descricao = input(f"Nova Descrição (atual: {tarefa['descricao']}): ") or tarefa['descricao']
                nova_data = input(f"Nova Data (atual: {tarefa['data']}, formato dd/mm/aaaa): ") or tarefa['data']
                try:
                    data_obj = datetime.strptime(nova_data, '%d/%m/%Y')
                    if data_obj.date() < datetime.now().date():
                        print("Data de conclusão não pode ser no passado")
                        return
                    tarefa['data'] = data_obj.strftime('%d/%m/%Y')
                except ValueError:
                    print("Data em formato inválido. Utilize dd/mm/aaaa.")
                    return
                tarefa['titulo'] = novo_titulo
                tarefa['descricao'] = nova_descricao
                salvar_tarefas(tarefas)
                print("Tarefa editada com sucesso!")
                return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")


# exportar para csv
def exportar_tarefas(tarefas):
    try:
        with open('tarefas_exportadas.csv', 'w', newline='') as arquivo_csv:
            campos = ['ID', 'Título', 'Descrição', 'Data de Conclusão', 'Concluída']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor.writeheader()
            for tarefa in tarefas:
                escritor.writerow({
                    'ID': tarefa['id'],
                    'Título': tarefa['titulo'],
                    'Descrição': tarefa['descricao'],
                    'Data de Conclusão': tarefa['data'],
                    'Pronta': 'True' if tarefa['pronta'] else 'False'
                })
        print("Tarefas exportadas com sucesso para 'tarefas_exportadas.csv'.")
    except Exception as e:
        print(f"Ocorreu um erro ao exportar as tarefas: {e}")


# importar tarefas de um CSV
def importar_tarefas(tarefas):
    nome_arquivo = input("Digite o nome do arquivo CSV para importar: ")
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                try:
                    tarefa = {
                        'id': gerar_id(tarefas),
                        'titulo': linha['Titulo'],
                        'descricao': linha['Descricao'],
                        'data': linha['Data de Conclusao'],
                        'pronta': True if linha['Pronta'].lower() == 'sim' else False
                    }
                    tarefas.append(tarefa)
                except KeyError:
                    print("Formato de arquivo inválido. Certifique-se de que o CSV contém as colunas corretas.")
                    return
        salvar_tarefas(tarefas)
        print(f"Tarefas importadas com sucesso do arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao importar as tarefas: {e}")


# menu principal
def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Pesquisar Tarefas")
    print("6. Ordenar Tarefas")
    print("7. Editar Tarefas")
    print("8. Exportar Tarefas para CSV")
    print("9. Importar Tarefas de CSV")
    print("10. Sair")
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
            pesquisar_tarefas(tarefas)
        elif opcao == '6':
            ordenar_tarefas(tarefas)
        elif opcao == '7':
            editar_tarefas(tarefas)
        elif opcao == '8':
            exportar_tarefas(tarefas)
        elif opcao == '9':
            importar_tarefas(tarefas)
        elif opcao == '10':
            print("Encerrando programa")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    main()
