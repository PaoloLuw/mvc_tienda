from flask import render_template

def mostrar_menu():
    """Muestra la página principal con el menú"""
    return render_template('index.html')

def mostrar_productos(productos):
    """Muestra la lista de productos"""
    return render_template('listar_productos.html', productos=productos)

def formulario_agregar():
    """Muestra el formulario para agregar un producto"""
    return render_template('agregar_producto.html')