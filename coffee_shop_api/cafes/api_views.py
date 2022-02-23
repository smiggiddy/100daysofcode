from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from random import choice
from .models import Cafe
from . import db

API_KEY = "TopSecretAPIKey"

api_views = Blueprint('api_views', __name__)


@api_views.route("/")
def home():
    return render_template("index.html")


@api_views.route("/random")
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)

    return jsonify(cafe=random_cafe.to_dict()     
    )


@api_views.route("/all")
def all_cafes():
    all_cafes = db.session.query(Cafe).all()

    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes] )


@api_views.route("/search")
def search_location():
    location = request.args.get('loc')
    try:
        location_result = Cafe.query.filter_by(location=location).first()
        return jsonify(cafe=location_result.to_dict())
    except:
        return jsonify(error={'NotFound': 'Location Not Found'})


## HTTP POST - Create Record
@api_views.route("/add", methods=['POST', 'GET'])
def add_cafe():
    if request.method == 'POST':
        new_cafe = Cafe(
            name = request.form.get('name'),
            map_url = request.form['map_url'],
            img_url = request.form['img_url'],
            location = request.form['location'],
            seats = request.form['seats'],
            has_toilet = bool(request.form['has_toilet']),
            has_wifi = bool(request.form['has_wifi']),
            has_sockets = bool(request.form['has_sockets']),
            can_take_calls = bool(request.form['can_take_calls']),
            coffee_price = request.form['coffee_price']

        )
        db.session.add(new_cafe)
        db.session.commit()
        if bool(request.form['from_web']):
            return  redirect(url_for('views.home'))

        return jsonify(response={'success': 'Added New Cafe to Database'}), 200
    else:
        return jsonify(response={'Error': 'No GET requests for this page'}), 404


## HTTP PUT/PATCH - Update Record
@api_views.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_cafe(cafe_id):
    try:
        cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()
        coffee_price = request.args.get('coffee_price')
        cafe_to_update.coffee_price = coffee_price
        db.session.commit()
        return jsonify(response={'Updated Cafe': 'Updated price for cafe'}), 200
    except Exception as ex:
        return jsonify(response={'Error': f'Something went wrong! ID {cafe_id} does not exist!'}), 404


## HTTP DELETE - Delete Record
@api_views.route("/report-closed/<cafe_id>", methods=['DELETE'])
def closed_cafe(cafe_id):
    api_key = request.args.get('api-key')

    if api_key == API_KEY:
        try:
            cafe_to_delete = Cafe.query.filter_by(id=cafe_id).first()
            print(cafe_to_delete)
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={'Deleted': f'Cafe: {cafe_to_delete.name} removed from database'}), 200
        except:
            return jsonify(response={'Error': f'Something went wrong! Cafe does not exist!'}), 404
    else:
         return jsonify(response={'Error': 'You do not have access for this resrouce'}), 403









