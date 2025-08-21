import sqlite3 

#conectar ao banco de dados (ou criar um novo, caso não exista)
def conectarBanco():
    conexao = sqlite3.connect('C:/Users/mykew/OneDrive/Área de Trabalho/Python_Myke/bancodedados.db')
    return conexao

#Criar uma tabela
def criarTabela():
    conexao = conectarBanco()#abre a conexão
    cursor = conexao.cursor()# cria um cursor para executar os comandos sql
    
    #Cria a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
                   ''')
    conexao.commit()
    conexao.close()
    
def inserirUsuario(nome, idade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES(?, ?)
                   ''', (nome, idade))
    conexao.commit()
    conexao.close()
    
def listarUsuarios():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
                   ''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print (usuario)
    conexao.close()

def atualizarUsuario (id, novoNome, novaIdade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, idade = ?
        WHERE id = ?
                   ''',(novoNome, novaIdade, id))
    conexao.commit()
    conexao.close()
    
def excluirUsuario (id):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios
        WHERE id = ?                   
                   
                   ''', (id,))
    conexao.commit()
    conexao.close()
    
    
# exemplos de uso das funçoes crud

# criar tabela:
criarTabela()

#inserir dados no banco de dados:
#inserirUsuario('Myke', 35)
#inserirUsuario('Caio', 38)
#inserirUsuario('Gabriel', 30)
#inserirUsuario('Gustavo', 22)
#inserirUsuario('Joao', 47)
#inserirUsuario('Luis', 30)


# Listar todos os usuario cadastrados no banco
print('Usuários antes de atualizar')
listarUsuarios()
print("------------------------------------------")

# atualizar idade e nome de um usuários

atualizarUsuario(1, 'Enzo', 20)
atualizarUsuario(2, 'Valentina', 60)

# Excluir o usuário de id 6
excluirUsuario(6)

print('Usuários depois da atualização')
listarUsuarios()
print('------------------------------------')


