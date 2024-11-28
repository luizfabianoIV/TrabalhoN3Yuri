from app import app
from model.user import *
from model.modelteste import*


with app.app_context():
    db.create_all()