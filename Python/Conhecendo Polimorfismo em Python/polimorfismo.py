class Passaro:
    def voar(self):
        print("Voando")


class Pato(Passaro):
    def voar(self):
        print("Pato voando")


class Pinguim(Passaro):
    def voar(self):
        print("Pinguim não voa")


def plano_voo(obj):
    obj.voar()


p1 = Pato()
p2 = Pinguim()

plano_voo(p1)  
plano_voo(p2)
