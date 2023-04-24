from flask import Flask, request, jsonify, redirect, url_for
import models
import hashlib

app = Flask(__name__)


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
        pass


if __name__ == '__main__':
    app.run(debug=True)
