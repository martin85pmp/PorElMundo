from flask import Flask
from flask import render_template, request, redirect 
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

@app.route('/')
def europa():
    return render_template('europa.html')

@app.route('/reserva/<int:id>')
def mostrarReserva():
    sql = "SELECT * FROM `porElMundo`.`reservas` WHERE id=%s", (id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    reservas=cursor.fetchall()
    conn.commit()
    return render_template('reserva.html', reservas=reservas)

@app.route('/store', methods=['POST'])
def storage():
    #Traemos los datos del formulario que se encuentra en script.js
    _nombre=request.form['firstname']
    _apellido = request.form['lastname']
    _ciudad = request.form['city']
    _noches = request.form['night']
    _correo=request.form['email']
    _telefono=request.form['phone']
    _fecha=request.form['date']
    _genero=request.form['gender']
    
    sql = "INSERT INTO `porElMundo`.`reservas` (`id`, `nombre`, `apellido`, `correo`, `telefono`, `ciudad`, `noches`, `fecha`, `genero`, `precio`) VALUES (NULL, %s,%s, %s,%s,%s,%s,%s,%s, NULL);"
    datos=(_nombre,_apellido, _correo, _telefono, _ciudad, _noches, _fecha, _genero)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return render_template('reserva.html')

@app.route('/edit/<int:id>')
def edit(id):
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM `porElMundo`.`reservas` WHERE id=%s", (id))
 reservas=cursor.fetchall()
 conn.commit()
 return render_template('edit.html', reservas=reservas)

@app.route('/destroy/<int:id>')
def destroy(id):
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute("DELETE FROM `porElMundo`.`reservas` WHERE id=%s", (id))
 conn.commit()
 return redirect('/')

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'porElMundo'

mysql.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)