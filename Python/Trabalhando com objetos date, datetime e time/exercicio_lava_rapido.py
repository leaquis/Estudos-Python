from datetime import datetime, timedelta


def menu():
    print("Qual é o tamanho do seu carro?")
    print("Digite 'P' para pequeno, 'M' para médio e 'G' para grande")
    print("Digite 'Sair' caso queira sair do programa")
    return input("")


def calculo_tempo(tempo):
    data_atual = datetime.now()
    data_estimada = data_atual + timedelta(minutes=tempo)
    print(f"O carro chegou: {data_atual}, a data estimada para estar pronto é: {data_estimada}")


def main():
    while True:
        opcao = menu()

        if opcao.lower() == 'p':
            tempo = 30
            calculo_tempo(tempo)
            break
        elif opcao.lower() == 'm':
            tempo = 60
            calculo_tempo(tempo)
            break
        elif opcao.lower() == 'g':
            tempo = 90
            calculo_tempo(tempo)
            break
        elif opcao.lower() == 'sair':
            print("Encerrando programa")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    main()
