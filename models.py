from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Instead of text, use integer codes for categories
    card_name = db.Column(db.Integer, nullable=False)      # e.g., map names to IDs
    card_type = db.Column(db.Integer, nullable=False)      # e.g., 1 = troop, 2 = spell, 3 = building
    attack_type = db.Column(db.Integer, nullable=False)    # e.g., 0 = melee, 1 = ranged, 2 = splash
    elixir_cost = db.Column(db.Integer, nullable=False)    # numeric cost
    card_rating = db.Column(db.Float, nullable=False)           # numeric rating
    rarity = db.Column(db.Integer, nullable=False)         # e.g., 1 = common, 2 = rare, 3 = epic, 4 = legendary


