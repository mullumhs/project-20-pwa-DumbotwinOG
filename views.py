from flask import render_template, request, redirect, url_for, flash
from models import db, Cards  # your SQLAlchemy model

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # Retrieve all cards from the database
        cards = Cards.query.all()
        return render_template('index.html', message='Card Inventory', cards=cards)

    @app.route('/add', methods=['POST'])
    def add_cards():
        new_card = Cards(
            card_name=request.form['card_name'],
            card_type=request.form['card_type'],
            attack_type=request.form['attack_type'],
            elixir_cost=int(request.form['elixir_cost']),
            card_rating=float(request.form['card_rating']),
            rarity=request.form['rarity']  # keep rarity as string
        )
        db.session.add(new_card)
        db.session.commit()

        flash(f'Card "{new_card.card_name}" added successfully!', 'success')
        return redirect(url_for('get_items'))

    @app.route('/update', methods=['POST'])
    def update_item():
        card = Cards.query.filter_by(card_name=request.form['card_name']).first()

        if card:
            # Update existing card
            card.card_type = request.form['card_type']
            card.attack_type = request.form['attack_type']
            card.elixir_cost = int(request.form['elixir_cost'])
            card.card_rating = float(request.form['card_rating'])
            card.rarity = request.form['rarity']
            db.session.commit()
            flash(f'Card "{card.card_name}" updated successfully!', 'info')
        else:
            # Create new card if not found
            new_card = Cards(
                card_name=request.form['card_name'],
                card_type=request.form['card_type'],
                attack_type=request.form['attack_type'],
                elixir_cost=int(request.form['elixir_cost']),
                card_rating=float(request.form['card_rating']),
                rarity=request.form['rarity']
            )
            db.session.add(new_card)
            db.session.commit()
            flash(f'New card "{new_card.card_name}" created successfully!', 'success')

        return redirect(url_for('get_items'))

    @app.route('/delete', methods=['POST'])
    def delete_item():
        card_id = request.form['id']
        card = Cards.query.get(card_id)

        if card:
            db.session.delete(card)
            db.session.commit()
            flash(f'Card "{card.card_name}" deleted successfully!', 'danger')
        else:
            flash('Card not found.', 'warning')

        return redirect(url_for('get_items'))
