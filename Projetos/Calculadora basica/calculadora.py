# -*- coding: utf-8 -*-

print ("---CALCULADORA BÁSICA---")

sair = False

while sair == False:

	n1 = input("Digite o primeiro número: ")
	n1 = int(n1)
	operador = input("Digite o operador(+ - / *): ")
	n2 = input("Digite o segundo número: ")
	n2 = int(n2)

	if operador == "+":
		operacao = n1 + n2
		print("Resultado: ")
		print(operacao)

	if operador == "-":
		operacao = n1 - n2
		print("Resultado: ")
		print(operacao)

	if operador == "/":
		operacao = n1 / n2
		print("Resultado: ")
		print(operacao)

	if operador == "*":
		operacao = n1 * n2
		print("Resultado: ")
		print(operacao)

	teste = input("Deseja sair (s/n):")
	if teste == "s":
		sair = True
