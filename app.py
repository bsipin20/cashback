import os
import csv
from cashback import main
from flask import Flask, flash, request, redirect, url_for,render_template,jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory

from flask import Flask

#from cashback.creditcards import amex,discover

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/briansipin/dev/cashback/uploads'
ALLOWED_EXTENSIONS = set(['qfx'])
#txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        filename = secure_filename(file.filename)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_ = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            categories = main.run(file_)
            #results = main.calc_cashback(categories)
            report =main.calc_all(categories)
            return jsonify(detailed_report=report)
            #redirect(url_for('report',results=results))
    render_template('enter.html')
#    return '''
#    <!doctype html>
#    <title>CashBack App</title>
#    <h1>Upload Bank Statement (QFX format only)</h1>
#    <form method=post enctype=multipart/form-data>
#      <input type=file name=file>
#      <input type=submit value=Upload>
#    </form>
#    '''

@app.route('/report')
def report(results):
    #render_template('results.html',title='Report',cashbackscore = resutls)
    render_template('results.html',title='Report',cashbackscore = results)

if __name__ == "__main__":
    app.run(port=8000,debug=True)

