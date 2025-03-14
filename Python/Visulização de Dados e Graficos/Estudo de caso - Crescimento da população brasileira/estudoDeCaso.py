import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color="k", linestyle="--")
plt.title("Crescimento da População brasileira de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()
#plt.savefig("populacao_brasileira.png", dpi=300)
