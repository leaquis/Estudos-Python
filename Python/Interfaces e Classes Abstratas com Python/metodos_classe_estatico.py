class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# p = Pessoa("Giovani", 27)
# print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1997, 12, 21, "Giovani")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(27))
print(Pessoa.e_maior_idade(7))
