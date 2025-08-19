import requests, json

nome = input('Qual nome deseja buscar?: ')

resposta = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')

dados = json.loads(resposta.text)

print(dados[0]['res'][0])