class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe.")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe.")

    def latir(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Luke", "Branco", False)
    print(c.nome)


#criar_cachorro()
c = Cachorro("Harley", "marrom")
c.latir()

print("Olá mundo!")
print("Olá mundo!")
del c
print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")
