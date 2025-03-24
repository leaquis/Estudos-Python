# encoding: utf-8
import random

print("Adivinhe qual é o número correto!")


def escolha_da_dificuldade():
    dificuldade = int(input("Escolha a dificuldade: 1-Fácil(0 a 10) 2-Médio(0 a 20) 3-Difícil(0 a 50) 4-Super Difícil(0 a 100)"))
    if dificuldade == 1:
        n = 10
        return n
    elif dificuldade == 2:
        n = 20
        return n
    elif dificuldade == 3:
        n = 50
        return n
    elif dificuldade == 4:
        n = 100
        return n
    else:
        print("Dificuldade Inválida! Escolha uma opção de 1 a 4!")
        escolha_da_dificuldade()


rangeDeNumeros = escolha_da_dificuldade()

palpite = int(input("Qual é o seu palpite? "))
numero = random.randint(0, rangeDeNumeros)
erros = 0

if palpite == numero:
    print("Parabéns, você acertou de primeira!!")
else:
    while palpite != numero:
        palpite = int(input("Você errou! Qual é o seu novo palpite? "))
        erros += 1
    print("Parabéns, você acertou!!")
    print(f"Quantidade de erros: {erros}")
