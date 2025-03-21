nome = input("Digite o seu nome: ")

vogal1 = "a"
vogal2 = "i"

if vogal1 in nome:
    print("Seu nome contem a vogal A")
else:
    print("Seu nome nao contem a vogal A")

if vogal2 not in nome:
    print("Seu nome nao contem a vogal I")
else:
    print("Seu nome contem a vogal I")
