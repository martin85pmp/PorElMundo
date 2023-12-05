from flask import Flask
from flask import render_template, request, redirect 
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

@app.route('/') #Le pasas como parámetro la url a la que estás accediendo
def index():
    return render_template('index.html') #y aca le pasas la url que queres que te muestre 

@app.route('/europa') 
def europa():
    return render_template('europa.html') 

@app.route('/asia')
def asia():
    return render_template('asia.html') 

@app.route('/oceania')
def oceania():
    return render_template('oceania.html') 

@app.route('/restodeamerica')
def restodeamerica():
    return render_template('restodeamerica.html') 

@app.route('/conversor')
def conversor():
    return render_template('conversor.html') 

@app.route('/contacto')
def contacto():
    return render_template('contacto.html') 

@app.route('/reserva')
def mostrarReserva():
    return render_template('reserva.html')

@app.route('/reserva/<int:id>', methods=['GET', 'POST'])
def reserva(id):
    
    sql = "SELECT * FROM `porElMundo`.`reservas` WHERE id=%s", (id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    reserva=cursor.fetchall()
    
    
    conn.commit()
    return render_template('reserva.html', reserva=reserva)

@app.route('/store', methods=['POST', 'GET'])
def storage():
    #Traemos los datos del formulario que se encuentra en script.js
    if request.method == 'POST':
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
        sql2="SELECT * FROM `porElMundo`.`reservas`"
        cursor.execute(sql2)
        reserva = cursor.fetchone()
        return render_template('reserva.html', reserva=reserva)
    else:
        return redirect('/')
    

@app.route('/edit/<int:id>')
def edit(id):
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM `porElMundo`.`reservas` WHERE id=%s", (id))
 reserva=cursor.fetchall()
 print("-------------------------")
 print(reserva)
 conn.commit()
 return render_template('edit.html', reserva=reserva)

@app.route('/destroy/<int:id>')
def destroy(id):
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute("DELETE FROM `porElMundo`.`reservas` WHERE id=%s", (id))
 conn.commit()
 return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['firstname']
    _apellido = request.form['lastname']
    _ciudad = request.form['city']
    _noches = request.form['night']
    _correo=request.form['email']
    _telefono=request.form['phone']
    _fecha=request.form['date']
    _genero=request.form['gender']
    id=request.form['id']
    sql = "UPDATE `porElMundo`.`reservas` SET `nombre`=%s, `apellido`=%s, `ciudad`=%s, `noches`=%s, `correo`=%s `telefono`=%s, `fecha`=%s, `genero`=NULL, WHERE id=%s;"
    datos=(_nombre,_apellido, _ciudad, _noches, _correo, _telefono, _fecha, id)
    conn = mysql.connect()
    cursor = conn.cursor()    
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

#Cuando haces un deploy en realidad no podes poner los datos así como están porque cualquiera podría acceder a la base de datos (si no fuera local). Se incluyen como variables que a su vez se importan de otro archivo que vos agregas al .gitignore
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'porElMundo'

mysql.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)