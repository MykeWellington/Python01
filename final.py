import pandas as pd
import numpy as np

#Criar dados com numpy
nomes = ['Caio', 'Myke', 'Gustavo', 'Luis', 'Gabriel', 'João' ]

idades = np.random.randint(20,50, size=len(nomes))
salarios = np.random.randint(3000,10000, size=len(nomes))

#Criar dataframe com o pandas

df = pd.DataFrame({
    'Nome': nomes,
    'Idade': idades,
    'Salario': salarios
})
print('\n 📈 Dataframe gerado')
print(df)

#Adicionar nova coluna de imposto calculado
df ['Imposto'] = df ['Salario'] * 0.14
print('\n Adicionando uma nova coluna calculando imposto')
print(df)

#Usando as funções do numpy no dataframe
print('\n Idade media do grupo')
print(np.mean(df['Idade']))

#Média salarial do grupo
print('\n Media salarial do grupo')
print(np.mean(df['Salario']))

#Filtrar com pandas pessoas com salario acima da média
media_salarial = np.mean(df['Salario'])
print('\n Pessoas com salário acima da media')
print(df[df['Salario'] > media_salarial])

#Estatisticas resumidas
print('\n Resumo estatistico (pandas)')
print(df.describe())

