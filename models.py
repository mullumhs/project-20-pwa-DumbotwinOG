from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Cards(db.Model):
    card_name = db.Column(db.Integer, primary_key=True)
    card_rarity = db.Column(db.Text)
    card_rating = db.Column(db.Integer, nullable=False)
    elixir_cost = db.Column(db.Integer, nullable=False)
    card_type = db.Column(db.Boolean, default=False)
    attack_type = db.Column(db.DateTime, default=datetime.utcnow)

