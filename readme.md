# Sistema de Registro de Productos (MVC)

## Descripción

Aplicación web para registrar y listar productos (nombre, categoría, precio) implementada en Python con Flask, siguiendo el patrón MVC (Modelo-Vista-Controlador). Los datos se persisten en un archivo `productos.csv`, inicializado con ejemplos (e.g., "Laptop,Electrónica,434.3"). El diseño está inspirado en la página de Grok, con un estilo oscuro, tipografía moderna, y responsividad.

## Estructura del Proyecto

```
📦mvc_tienda
 ┣ 📂static
 ┃ ┗ 📜style.css              # Estilos CSS inspirados en Grok
 ┣ 📂templates
 ┃ ┣ 📜agregar_producto.html  # Formulario para agregar productos
 ┃ ┣ 📜index.html             # Menú principal
 ┃ ┗ 📜listar_productos.html  # Lista de productos en tabla
 ┣ 📜controlador.py           # Lógica de negocio (agregar/listar)
 ┣ 📜main.py                  # Configuración de Flask y rutas
 ┣ 📜modelo.py                # Clase Producto y manejo de CSV
 ┣ 📜productos.csv            # Almacenamiento de datos
 ┗ 📜vista.py                 # Renderizado de plantillas HTML
```

## Requisitos

- Python 3.8+
- Flask (`pip install flask`)

## Instalación

1. Clona o descarga el proyecto en `D:\Sly_Codes\Sly_Python\mvc_tienda`.

2. Instala Flask:

   ```bash
   pip install flask
   ```

## Ejecución

1. Navega al directorio del proyecto:

   ```bash
   cd D:\Sly_Codes\Sly_Python\mvc_tienda
   ```

2. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

3. Abre un navegador y visita `http://127.0.0.1:5000/`.

## Uso

- **Menú principal**: Accede a "Agregar Producto" o "Listar Productos".
- **Agregar Producto**: Ingresa nombre, categoría, y precio en el formulario.
- **Listar Productos**: Visualiza los productos almacenados en `productos.csv`.

## Datos Iniciales

El archivo `productos.csv` incluye ejemplos:

```
nombre,categoria,precio
Laptop,Electrónica,434.3
Smartphone,Electrónica,599.99
Mesa,Muebles,120.5
Silla,Muebles,45.75
Audífonos,Accesorios,29.99
```

## Notas

- Asegúrate de que `productos.csv` tenga permisos de escritura.
- El diseño es responsivo y usa la tipografía Inter (Google Fonts).

## Autor

# \[Tu Nombre Completo\]\\

## Código: \[Tu Código\]\\

### Fecha: 28 de junio de 2025