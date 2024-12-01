from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, desc

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

@app.route('/carrinho-compras', methods=['GET', 'POST', 'PUT', 'DELETE'])
def carrinho():
    if request.method == 'GET':
        # Retorna o carrinho de compras do usuário atual 
        return 'Carrinho de compras com produto desejado'
    elif request.method == 'POST':
        # Adiciona um item ao carrinho de compras
        return 'Produto adicionado ao carrinho'
    elif request.method == 'PUT':
        # Atualiza a quantidade de um item no carrinho
        return 'Quantidade do produto atualizada no carrinho'
    elif request.method == 'DELETE':
        # Remove um item do carrinho de compras
        return 'Produto removido do carrinho'