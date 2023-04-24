from flask import Flask, request, jsonify, redirect, url_for
import models
import hashlib

app = Flask(__name__)


@app.route('/cadastro', methods = ['POST'])
def cadastro_user():
    dados = request.get_json()

    try:
        models.criar(nome=dados['nome'], email=dados['email'], senha='teste', data_nascimento=dados['data_nascimento'], cpf=dados['cpf'], rg=dados['rg'])
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
    


if __name__ == '__main__':
    app.run(debug=True)
