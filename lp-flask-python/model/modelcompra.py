from app import db

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    data_compra = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String, default='Pendente')
    produtos = db.relationship('ItemCompra', back_populates='compra')

    def __repr__(self):
        return f"<Compra(id={self.id}, total={self.total})>"