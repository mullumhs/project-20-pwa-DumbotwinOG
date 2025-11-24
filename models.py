from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), nullable=False)   # <-- use card_name
    card_type = db.Column(db.String(50), nullable=False)
    attack_type = db.Column(db.String(50), nullable=False)
    elixir_cost = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    rarity = db.Column(db.String(50), nullable=False)       # <-- string if you want text like "Epic"


