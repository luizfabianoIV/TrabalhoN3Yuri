from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, desc

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

@app.route('/pagamento', methods=['GET', 'POST'])
def pagamento():
    if request.method == 'GET':
        return 'Opções de pagamentos'
    elif request.method == 'POST':
        # Processa o pagamento
        return 'Pagamento realizado com sucesso'

if __name__ == '__main__':
    app.run(debug=True)