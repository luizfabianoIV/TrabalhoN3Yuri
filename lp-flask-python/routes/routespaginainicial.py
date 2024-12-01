from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, desc

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

@app.route('/inicial', methods=['GET'])
def paginainicial():
    return 'Bem vindo a tela inicial de um dos maiores sites de vendas de peça!'

