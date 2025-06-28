from modelo import Producto, guardar_producto, obtener_productos
from flask import request, redirect, url_for, render_template

def agregar_producto():
    """Procesa los datos del formulario y guarda un producto"""
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        try:
            precio = float(request.form['precio'])
            if nombre and categoria and precio >= 0:
                producto = Producto(nombre, categoria, precio)
                guardar_producto(producto)
                return redirect(url_for('listar'))
            else:
                return render_template('agregar_producto.html', error="Todos los campos son obligatorios y el precio debe ser positivo")
        except ValueError:
            return render_template('agregar_producto.html', error="El precio debe ser un número válido")
    return redirect(url_for('formulario'))

def listar_productos():
    """Obtiene los productos del modelo y los pasa a la vista"""
    productos = obtener_productos()
    return productos
