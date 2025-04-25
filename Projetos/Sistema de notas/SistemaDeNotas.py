# Sistema de gerenciamento de notas de alunos

def menu():
    print("=== Sistema de gerenciamento de notas ===")
    print("1- Cadastrar aluno")
    print("2- Inserir notas")
    print("3- Exibir relatorio")
    print("4- Sair")
    return input("Escolha uma opção: ")


def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")

    if nome.strip() == "":
        print("Nome não pode ser vazio.")
        return
    if nome in alunos:
        print("Aluno já existe.")
        return
    
    alunos[nome] = []

    print(f"Aluno {nome} cadastrado")


def inserir_notas(alunos):
    nome = input("Digite o nome do aluno: ")

    if nome not in alunos:
        print("O aluno não foi encontrado.")
        return
    
    print(f"Digite as notas do aluno {nome}. O número deve ser de 0 a 10, digite fim para encerrar")

    while True:
        nota = input(f"Nota {len(alunos[nome]) + 1}: ")

        if nota.lower() == 'fim':
            break

        try:
            nota = float(nota)

            if 0 <= nota <= 10:
                alunos[nome].append(nota)
                print(f"Nota {nota} inserida no aluno {nome}")
            else:
                print("A nota deve ser entre 0 e 10!")
        except ValueError:
            print("Entrada inválida, tente novamente.")


def calcular_media_e_status(notas):
    if not notas:
        return 0, "Sem notas"
    
    media = sum(notas) / len(notas)

    status = "Aprovado" if media >= 6 else "Reprovado"

    return media, status


def exibir_relatorio(alunos):
    if not alunos:
        print("Não há alunos cadastrados.")
        return
     
    print("=== Relatorio alunos ===")
    for nome, notas in alunos.items():
        media, status = calcular_media_e_status(notas)
        print(f"Aluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media}")
        print(f"Status: {status}")
        print("-" * 30)


def main():

    alunos = {}

    while True:
        opcao = menu()
        if opcao == '1':
            cadastrar_aluno(alunos)
        elif opcao == '2':
            inserir_notas(alunos)
        elif opcao == '3':
            exibir_relatorio(alunos)
        elif opcao == '4':
            print("Saindo do sistema!")
            break
        else:
            print("Opção inválida, escolha outra opção!")


if __name__ == '__main__':
    main()
