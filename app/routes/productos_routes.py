# app/routes/productos_routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.modelos import Producto, Categoria

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos')
def listar_productos():
    productos = Producto.query.all()
    return render_template('productos/listar.html', productos=productos)

@productos_bp.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        categoria_id = int(request.form['categoria_id'])

        nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock, categoria_id=categoria_id)
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('productos.listar_productos'))
    
    categorias = Categoria.query.all()
    return render_template('productos/crear.html', categorias=categorias)

@productos_bp.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        producto.stock = int(request.form['stock'])
        producto.categoria_id = int(request.form['categoria_id'])
        db.session.commit()
        return redirect(url_for('productos.listar_productos'))
    
    categorias = Categoria.query.all()
    return render_template('productos/editar.html', producto=producto, categorias=categorias)

@productos_bp.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos.listar_productos'))
