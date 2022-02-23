from flask import Blueprint, redirect, render_template, request, url_for
from matplotlib.pyplot import title
from .models import Cafe
from . import db
import requests

views = Blueprint('views', __name__)
API_KEY = "TopSecretAPIKey"

@views.route('/')
def home():
    """Function returns basic homepage for coffee site"""
    all_cafes = db.session.query(Cafe).all() 
    sum_shops = len(all_cafes)

    # group cafes in 3's
    cafe_list = [all_cafes[x:x+3] for x in range(0, len(all_cafes), 3)]



    title = f"{sum_shops} Coffee Shop"
    

    return render_template('base.html', title=title, cafes=cafe_list)


@views.route('/add', methods=['GET'])
def add():
    """Function adds cafe and sends results to api"""
    
    return render_template('form.html')
    
    
@views.route('/delete-cafe', methods=['GET','POST'])
def delete_cafe():
    """function deletes cafe by ID"""

    if request.method == 'POST':
        cafe_name = request.form.get("cafe_name")
        cafe_to_delete = Cafe.query.filter_by(name=cafe_name).first()

        id = cafe_to_delete.id

        params = {
            'cafe_id': str(id),
            'api-key': API_KEY,
        }


        r = requests.delete(url=f"http://localhost:5000{url_for('api_views.closed_cafe', cafe_id=id)}", params=params)

        return redirect(url_for('views.home'))



    return render_template('form.html')