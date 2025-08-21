import pandas as pd

#Criar um dataframe com o pandas e inserir os dados
data = {
    'Nome':['Caio','Myke','Gustavo', 'João','Gabriel','Luis'],
    'Idade':[38,35,22,37,39,44],
    'Salario':[3564,9876,4862,3468,7469,3489]
}
df = pd.DataFrame(data)

#Exibindo o Dataframe
print('\n Dataframe ')
print(df)

#Selecionando uma coluna
print('\n Coluna de nome')
print(df['Nome'])

#Filtrando linhas (ex: idade menor que 30)
print('\n Pessoas com idade menoor que 30')
print(df[df['Idade'] < 30])

#Adicionando nova coluna
df['Imposto'] = df['Salario'] *0.18
print('\n Adicionando uma nova coluna "imposto"')
print(df)

#Calculando a média de salário
media_salarial = df['Salario'].mean()
print('\n Media do salario ')
print(media_salarial)

# salvar o dataframe em um arquivo csv

df.to_csv('equipe.csv', index=False)

