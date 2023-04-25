from flask import Flask, request, jsonify, redirect, url_for
import models
from hashlib import sha256

app = Flask(__name__)


@app.route('/cadastro', methods = ['POST'])
def cadastro_user():
    dados = request.get_json()
    senha = dados['senha']
    hash_senha = sha256(senha.encode('utf-8')) # hash de senha 
    senha_armazenar = hash_senha.hexdigest() # armazena hash no bd

    try:
        models.criar(nome=dados['nome'], email=dados['email'], senha=senha_armazenar, data_nascimento=dados['data_nascimento'], cpf=dados['cpf'], rg=dados['rg'])
        return jsonify({"message": "Usuário cadastrado com sucesso!"})
    except:
        return jsonify({"message": "Erro ao casdastrar usuário"})
    
@app.route('/login', methods = ['POST'])
def login():
    dados_login = request.get_json()
    email = dados_login['email']
    senha = dados_login['senha']
    hash_senha_login = sha256(senha.encode('utf-8')).hexdigest() # criptografa senha passada no login para comparar com a que está no bd
  
    resultado = models.checa_senha(parametro_json=email)   
    senha_armazenada = resultado[0]

    if hash_senha_login == senha_armazenada:
        return jsonify({"message": "Senha válida"})
    else:
        return jsonify({"message": "Senha inválida"})
    


if __name__ == '__main__':
    app.run(debug=True)
