# encoding: utf-8
import random

print("Bem vindo ao jogo de adivinhar o número!")
print("Adivinhe o número entre 1 e 100, você tem 10 tentativas")

while True:

    numeroSecreto = random.randint(1, 100)
    tentativas = 10

    while tentativas > 0:
        palpite = input("Digite um número: ")

        if not palpite.isdigit():
            print("Entrada inválida! Por favor digite um número entre 1 e 100")
            continue

        palpite = int(palpite)

        if palpite < 1 or palpite > 100:
            print("O número deve ser entre 1 e 100")
            continue
        
        tentativas -= 1

        if palpite == numeroSecreto:
            print(f"Parabêns, voce acertou! Ainda restavam {tentativas} tentativas")
            break
        elif palpite < numeroSecreto:
            print("O número é maior do que esse!")
        else:
            print("O número é menor do que esse!")

        print(f"Tentativas restantes: {tentativas}")

    else:
        print(f"Acabaram as tentativas, você perdeu! O número era: {numeroSecreto}")  

    jogarNovamente = input("Deseja jogar novamente? (s/n)").lower()

    if jogarNovamente != "s":
        print("Obrigado! Até a proxima...")
        break
