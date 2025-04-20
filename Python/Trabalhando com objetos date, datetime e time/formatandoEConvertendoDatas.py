from datetime import datetime

data_atual = datetime.now()
data_string = '2023-07-20 15:30'
mascaraPTBR = "%d/%m/%Y %a"
mascaraEN = "%Y-%m-%d %H:%M"

# Formatando data e hora
print(data_atual.strftime(mascaraPTBR))

data_convertida = datetime.strptime(data_string, mascaraEN)
print(data_convertida)
print(type(data_convertida))
