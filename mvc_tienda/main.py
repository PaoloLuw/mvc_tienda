from flask import Flask
from vista import mostrar_menu, formulario_agregar, mostrar_productos
from controlador import agregar_producto, listar_productos

app = Flask(__name__)

@app.route('/')
def index():
    return mostrar_menu()

@app.route('/agregar', methods=['GET'])
def formulario():
    return formulario_agregar()

@app.route('/agregar', methods=['POST'])
def procesar_agregar():
    return agregar_producto()

@app.route('/listar')
def listar():
    productos = listar_productos()
    return mostrar_productos(productos)

if __name__ == '__main__':
    app.run(debug=True)
