import pandas as pd

# Função para carrega um arquivo do excel
def carregarArquivoCsv(caminhoArquivo):
    try:
        #carrega os dados do arquivo xlsx em um dataframe df = Data Frame
        df = pd.read_csv(caminhoArquivo)
        print('Arquivo carregado com sucesso!')
        #print(df.head())
        return df
    except Exception as errinho:
        print(f'Erro {errinho}')

def salvarArquivoCsv(df, caminhoSaida):
    df.to_csv(caminhoSaida, index=False)
    print(f'Arquivo salvo com sucesso em: {caminhoSaida}.') 
    
def salvarArquivoXlsx(df, caminhoSaida):
    df.to_excel(caminhoSaida, index = False)
    print(f'Arquivo salvo com sucesso em {caminhoSaida}')
    
    
# Definindo o local onde está o arquivo a ser carregado
localArquivo = 'C:/Users/mykew/OneDrive/Área de Trabalho/Python_Myke/base.csv'



df = carregarArquivoCsv(localArquivo)    

df['Nova coluna'] = df['Vendas'] * 2
#print(df.head())

#df['media aritimetica'] = (df['TV'] + df['Radio'] + df['Jornal']) / 3

df['media aritimetica'] = df[['TV', 'Radio', 'Jornal']].mean(axis=1)

#print(df.head())
caminhoSaida = 'C:/Users/mykew/OneDrive/Área de Trabalho/Python_Myke/novo_arquivo.csv'
#salvarArquivoCsv(df, caminhoSaida)

tipo = input('Deseja exportar para:\n [1] Excel\n[2] CSV? \n: ')
nome = input('Qual o nome do novo arquivo?')
caminhoPrincipal = 'C:/Users/mykew/OneDrive/Área de Trabalho/Python_Myke/'

if tipo == '1':
    salvarArquivoXlsx(df, f'{caminhoPrincipal}{nome}.xlsx')
    
    
elif tipo == '2': 
    salvarArquivoCsv(df, f'{caminhoPrincipal}{nome}.csv')
   
    
else:
    print('Tipo inválido, escolha entre CSV e Excel.')
    
    
