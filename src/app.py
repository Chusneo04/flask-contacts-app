from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from os import getenv


load_dotenv()




app = Flask(__name__)

app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = getenv('MYSQL_DB')
app.secret_key = getenv('SECRET_KEY')



mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from contacts')
    data = cursor.fetchall()
    print(data)
    return render_template('index.html', contacts=data)

@app.route('/add', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('USE flask_contacts_app')
        cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added Succesfully')

        return redirect(url_for('index'))
    return 'ADD CONTACT'

@app.route('/edit')
def edit_contact():
    return 'EDIT CONTACT'

@app.route('/update')
def update_contact():
    return 'UPDATE CONTACT'

@app.route('/delete/<id>')
def delete_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacts WHERE id= %s', (id))
    mysql.connection.commit()
    flash('Contacto borrado correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)