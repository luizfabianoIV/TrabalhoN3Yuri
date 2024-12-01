from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, desc

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from model import Produto

@app.route('/inicial', methods=['GET'])
def paginainicial():
    return 'Bem vindo a tela inicial de um dos maiores sites de vendas de peça!'

@app.route('/pecas', methods=['GET'])
def categoria():
    query_params = request.args

    page = query_params.get('page', default=0, type=int)
    limit = query_params.get('limit', default=10, type=int)
    offset = page * limit

    filter = {}
    ignored_fields = ['page', 'limit', 'sort_by', 'sort_direction']
    for field, value in query_params.items():
        if field not in ignored_fields:
            filter[field] = value

    sort_by = query_params.get('sort_by', default='id', type=str)
    sort_direction = query_params.get('sort_direction', default='asc', type=str)

    order_by = asc(sort_by) if sort_direction == 'asc' else desc(sort_by)

    produtos = Produto.query.filter_by(**filter).order_by(order_by).offset(offset).limit(limit).all()
    if not produtos:
        return jsonify([]), 200

    status_code = 206 if len(produtos) == limit else 200

    result = [produto.to_dict() for produto in produtos]

    return jsonify(result), status_code

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

@app.route('/pagamento', methods=['GET', 'POST'])
def pagamento():
    if request.method == 'GET':
        return 'Opções de pagamentos'
    elif request.method == 'POST':
        # Processa o pagamento
        return 'Pagamento realizado com sucesso'

if __name__ == '__main__':
    app.run(debug=True)
