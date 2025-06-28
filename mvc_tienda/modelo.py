import csv
import os

class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

# Ruta del archivo CSV
CSV_FILE = 'productos.csv'

# Cargar productos desde CSV al iniciar
def cargar_productos():
    productos = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                producto = Producto(row['nombre'], row['categoria'], float(row['precio']))
                productos.append(producto)
    return productos

# Lista de productos inicial
productos_db = cargar_productos()

def guardar_producto(producto):
    """Guarda un producto en la lista y actualiza el CSV"""
    productos_db.append(producto)
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['nombre', 'categoria', 'precio']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in productos_db:
            writer.writerow({'nombre': p.nombre, 'categoria': p.categoria, 'precio': p.precio})
    return True

def obtener_productos():
    """Devuelve la lista de productos"""
    return productos_db