from flask import Flask, redirect, render_template, request, url_for
from numpy import asarray
from PIL import Image
import os
import pandas as pd
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './day-91/static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'image_picker'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_hex_codes(file):
    """Returns list of dominant 10 image hex codes in image"""
    rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r, g, b)

    return [ rgb2hex(*file[i, i, :]) for i in range(file.shape[0])]


def common_colors(colors):
    """Returns 10 most common color's hex code"""
    pd_colors = pd.Series(colors)

    top_10_colors = pd_colors.value_counts(ascending=False)[:10] 
    return pd.Series.to_list(top_10_colors.index)



@app.route('/', methods=['GET', 'POST'])
def home():
    """Function allows user to upload an image and returns hex codes"""

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(url_for('home'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            img_upload = Image.open(f'./day-91/static/uploads/{filename}')
            img_array = asarray(img_upload)
            img_hex_codes = get_hex_codes(img_array)


            top_10_hex_codes = common_colors(img_hex_codes)

            return render_template('hex.html', hex_codes=top_10_hex_codes, filename=filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


### Notes

# https://stackoverflow.com/questions/41500637/how-to-extract-r-g-b-values-with-numpy-into-seperate-arrays
