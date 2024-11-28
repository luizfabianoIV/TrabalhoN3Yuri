from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    imagem = db.Column(db.String)

    def __repr__(self):
        return f"<Produto(nome={self.nome}, preco={self.preco})>"

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'estoque': self.estoque,
            'categoria': self.categoria,
            'imagem': self.imagem
        }

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    data_compra = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String, default='Pendente')
    produtos = db.relationship('ItemCompra', back_populates='compra')

    def __repr__(self):
        return f"<Compra(id={self.id}, total={self.total})>"

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    data_venda = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String, default='Pendente')
    produtos = db.relationship('ItemVenda', back_populates='venda')

    def __repr__(self):
        return f"<Venda(id={self.id}, total={self.total})>"
