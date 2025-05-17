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

print(vendas_df.loc[5, 'Produto'])
