import mysql.connector


conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password= '',
    database='usuarios'
)

cursor = conexao.cursor()

# Tabela de cadastro de cadastro
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cadastro (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45),
        email VARCHAR(45),
        senha VARCHAR(100),
        data_nascimento VARCHAR(45),
        cpf VARCHAR(11), 
        rg VARCHAR(20)
    )
""")


def criar(nome, email, senha, data_nascimento, cpf, rg):
        comando = f"INSERT INTO cadastro(nome, email, senha, data_nascimento, cpf, rg) VALUES ('{nome}', '{email}', '{senha}', '{data_nascimento}', '{cpf}', '{rg}')"
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
        

def buscar(tabela):

    cursor = conexao.cursor()
    comando_leitor = f"SELECT * FROM {tabela}"
    cursor.execute(comando_leitor)
    resultado = cursor.fetchall()
    return resultado


def checa_senha(parametro_json):
    comando_leitor = f"SELECT senha FROM cadastro WHERE email = '{parametro_json}'" 
    cursor.execute(comando_leitor)
    resultado = cursor.fetchone()
    return resultado



cursor.close
conexao.close
