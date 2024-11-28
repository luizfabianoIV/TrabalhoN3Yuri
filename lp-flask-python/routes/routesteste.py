from flask import request, jsonify
from sqlalchemy import asc, desc

from app import app
from model.user import User

@app.route('/inicial')
def paginainicial():
    return 'Bem vindo a tela inicial de um dos maiores sites de vendas de peça!'

@app.route('/pecas')
def categoria():
    return 'Categoria de peças disponivel a pronta entrega'

@app.route('/carrinho-compras')
def carrinho():
    return 'Carrinho de compras com produto desejado'

@app.route('pagamento')
def pagamento():
    return 'Opcões de pagamentos'