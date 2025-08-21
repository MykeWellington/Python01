import plotly.graph_objects as go

#Dados do grafico

valores_x = [1,2,3,4,5]
valores_y = [10,11,12,13,14]

#Criar grafico de linha
fig = go.Figure( 
    data=go.Scatter(
        x = valores_x,
        y = valores_y,
        mode = 'lines+markers',
        name = 'Linha 1')  )

#Adicionando o título e rotulo dos eixos
fig.update_layout(
    title = 'Grafico de linhas Interativas',
    xaxis_title = 'Eixo do X',
    yaxis_title = 'Eixo do Y'
)

#Exibe o gráfico criado

fig.show()