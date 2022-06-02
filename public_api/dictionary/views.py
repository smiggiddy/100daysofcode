from flask import Blueprint, redirect, jsonify, render_template, request
from .api import *
import json 

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    """Homepage allows user to enter a word"""



    if request.method == 'POST':
        word = request.form.get('word')

        if word != "":

            result = get_definition(word)
            json_data = json.dumps(result)

            return render_template('index.html', definition=result, json_data=json_data)
        else:
            return render_template('index.html')


    return render_template('index.html')

