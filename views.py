from flask import render_template, request, redirect, url_for, flash
from models import db,Cards # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        return render_template('index.html', message='Displaying all items')



    @app.route('/add', methods=['POST'])
    def add_cards():
        if request.method == 'POST':
            new_cards = Cards(
                name=request.form['card_name'],
                card_type=request.form['card_type'],
                attack_type=request.form['attack_type'],
                elixir=int(request.form['elixir_cost']),
                rating=float(request.form['card_rating']),
                rarity=float(request.form['rarity'])        

            )
        db.session.add(new_cards)
        db.session.commit()

        return render_template('index.html', message='Item added successfully')



    @app.route('/update', methods=['POST'])
    def update_item():
        
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')