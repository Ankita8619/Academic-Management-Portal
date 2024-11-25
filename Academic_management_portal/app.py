from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER1'] = 'C:/Users/Lenovo/Downloads/Ankita/files_first' # Add path according to your folder
app.config['UPLOAD_FOLDER2'] = 'C:/Users/Lenovo/Downloads/Ankita/files_second' 
app.config['UPLOAD_FOLDER3'] = 'C:/Users/Lenovo/Downloads/Ankita/files_third' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    query = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()
    
@app.route('/submit_form', methods=['POST'])
def submit_form():
    user = User(fname=request.form.get('fname'), lname=request.form.get('lname'), email=request.form.get('email'), query=request.form.get('query'))
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/first_year')
def first_year():
    return render_template('first_year.html')

@app.route('/second_year')
def second_year():
    return render_template('second_year.html')

@app.route('/third_year')
def third_year():
    return render_template('third_year.html')

@app.route('/upload_file_first', methods=['GET','POST'])
def upload_file_first():
    print(1)
    if request.method == 'POST':
        print(2)
        if 'file' not in request.files:
            print(3)
            return 'No file part'
        file = request.files['file']
        print(4)
        if file.filename == '':
            print(5)
            return 'No selected file'
        if file:
            print(6)
            filename = os.path.join(app.config['UPLOAD_FOLDER1'], 'uploaded_file.xlsx')
            print(7)
            file.save(filename)
            print(8)
            return redirect(url_for('upload_file_first'))
        print(9)
    return render_template('first_year.html')
    
@app.route('/upload_file_second', methods=['GET','POST'])
def upload_file_second():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER2'], 'uploaded_file.xlsx')
            file.save(filename)
            return redirect(url_for('upload_file_second'))
    return render_template('second_year.html')
    
@app.route('/upload_file_third', methods=['GET','POST'])
def upload_file_third():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER3'], 'uploaded_file.xlsx')
            file.save(filename)
            return redirect(url_for('upload_file_third'))
    return render_template('third_year.html')

@app.route('/result_first')
def result_first():
    filename = os.path.join(app.config['UPLOAD_FOLDER1'], 'uploaded_file.xlsx')
    if not os.path.exists(filename):
        return 'No file uploaded'
    df = pd.read_excel(filename)
    return df.to_html()

@app.route('/result_second')
def result_second():
    filename = os.path.join(app.config['UPLOAD_FOLDER2'], 'uploaded_file.xlsx')
    if not os.path.exists(filename):
        return 'No file uploaded'
    df = pd.read_excel(filename)
    return df.to_html()

@app.route('/result_third')
def result_third():
    filename = os.path.join(app.config['UPLOAD_FOLDER3'], 'uploaded_file.xlsx')
    if not os.path.exists(filename):
        return 'No file uploaded'
    df = pd.read_excel(filename)
    return df.to_html()

if __name__ == '__main__':
    app.run(debug=True)
