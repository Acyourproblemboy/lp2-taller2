from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint

# cargamos todos los datos de la base de datos a una variable global
conexion = sqlite3.connect('prueba.sqlite3')
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()
cursor.execute("""
select * from productos
""")
productos = [ dict (producto) for producto in cursor.fetchall() ]
cursor.close()
conexion.close()

# aplicación
app = Flask(__name__)

# rutas para mostrar la lista de productos en las plantillas
@app.route('/')
def ruta_raiz():
  return render_template('index.html', productos=productos)
  
#ruta para mostrar detalles de un solo producto
@app.route('/producto/<int:pid>')
def ruta_producto(pid):
  for producto in productos:
    if pid == producto['id']:
      return render_template('producto.html', producto=producto)
  return redirect('/')
  
# programa principal
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
