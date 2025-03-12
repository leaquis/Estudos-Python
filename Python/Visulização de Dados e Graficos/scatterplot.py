import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 9, 4]
z = [200, 300, 70, 90, 240]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)

plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.plot(x, y, color="#000000", linestyle= "--")
plt.legend()
#plt.show()
plt.savefig("imagem/figura1.png", dpi=300)
