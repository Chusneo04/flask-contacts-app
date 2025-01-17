from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import os



load_dotenv()



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hola Mundo'

@app.route('/add')
def add_contact():
    return 'ADD CONTACT'

@app.route('/edit')
def edit_contact():
    return 'EDIT CONTACT'

@app.route('/update')
def update_contact():
    return 'UPDATE CONTACT'

@app.route('/delete')
def delete_contact():
    return 'DELETE CONTACT'

if __name__ == '__main__':
    app.run(debug=True)