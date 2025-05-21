import pandas as pd

# dataframe = pd.DataFrame()

venda = {'data': ['2023-01-01', '2023-01-02', '2023-01-03'],
         'valor': [500, 300, 300],
         'produto': ['feijao', 'arroz', 'batata'],
         'quantidade': [50, 70, 30]}

# vendas_dv = pd.DataFrame(venda)
# print(vendas_dv)

vendas_df = pd.read_excel('Vendas.xlsx')
# print(vendas_df)
# print(vendas_df.head(10))
# print(vendas_df.shape)
# print(vendas_df.describe())

produtos = vendas_df[['Produto', 'ID Loja']]
# print(produtos)

# print(vendas_df.loc[1])
# print(vendas_df.loc[1:5])

# print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['Data', 'Produto', 'Quantidade']])

# print(vendas_df.loc[5, 'Produto'])

# vendas_df["Comissão"] = vendas_df['Valor Final'] * 0.05
# vendas_df["Imposto"] = 0
# vendas_df.loc[:, "Imposto"] = 0
# vendas_df.loc[3, "Imposto"] = 5
# print(vendas_df)

vendas_dez_df = pd.read_excel("Vendas - Dez.xlsx")
# print(vendas_dez_df)

# vendas_df = vendas_df.append(vendas_dez_df)
# print(vendas_df)

# vendas_df = vendas_df.drop('Imposto', axis=1)

# deletar linhas com valores vazios
# vendas_df = vendas_df.dropna(how='all')

# preencher com a média da coluna
# vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())

# preencher com o ultimo valor
# vendas_df = vendas_df.ffill()

# value counts
# transacoes_loja =  vendasdf['ID Loja'].value_counts()
# print(transacoes_loja)

# groupby
# faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()

# gerentes_df = pd.read_excel('Gerentes.xlsx')
# vendas_df = pd.merge(vendas_df, gerentes_df, on='ID Loja', how='left')
