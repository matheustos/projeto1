from flask import Flask, request, jsonify, redirect, url_for
import bcrypt
import models
import hashlib

app = Flask(__name__)

# Função para criar hash de senha com salting
def criar_hash_senha(senha):
    salt = bcrypt.gensalt()  # Gera um novo salt
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), salt)  # Gera o hash da senha
    return hashed_senha.decode('utf-8')

# Função para verificar se uma senha corresponde a um hash
def verificar_senha(senha, hashed_senha):
    return bcrypt.checkpw(senha.encode('utf-8'), hashed_senha.encode('utf-8'))


@app.route('/cadastro', methods = ['POST'])
def cadastro_user():
    dados = request.get_json()
    # Criar hash de senha
    hashed_senha = criar_hash_senha(dados['senha'])

    try:
        models.criar(nome=dados['nome'], email=dados['email'], senha=hashed_senha, data_nascimento=dados['data_nascimento'], cpf=dados['cpf'], rg=dados['rg'])
        return jsonify({"message": "Usuário cadastrado com sucesso!"})
    except:
        return jsonify({"message": "Erro ao casdastrar usuário"})
    
@app.route('/login', methods = ['POST'])
def login():
    dados_login = request.get_json()
  
    try:
        resultado = models.checa_senha(parametro_json=dados_login['email'])
        
    except:
        return jsonify({"message": "Email inválido!"})
    else:
        senha = $2b$12$.
        # Decodificar a senha criptografada do banco de dados
        senha_criptografada_bytes = senha.encode()
        if bcrypt.checkpw(dados_login['senha'].encode(), senha_criptografada_bytes):
            return "Senha correta"
        else:
            return "Senha incorreta!"



if __name__ == '__main__':
    app.run(debug=True)
