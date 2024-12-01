from app import db

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    data_venda = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String, default='Pendente')
    produtos = db.relationship('ItemVenda', back_populates='venda')

    def __repr__(self):
        return f"<Venda(id={self.id}, total={self.total})>"