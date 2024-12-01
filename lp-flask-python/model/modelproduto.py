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