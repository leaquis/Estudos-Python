class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)    


aluno1 = Estudante("Giovani", 12345)
aluno2 = Estudante("Roberta", 67890)
mostrar_valores(aluno1, aluno2)

aluno1.matricula = 54321
aluno2.nome = "Roberta Ramos"
mostrar_valores(aluno1, aluno2)

Estudante.escola = "DIO - Digital Innovation One"
mostrar_valores(aluno1, aluno2)
