from flask import Blueprint, render_template, request, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@main_bp.route('/servicios')
def servicios():
    return render_template('servicios.html')

@main_bp.route('/noticias')
def noticias():
    return render_template('noticias.html')

@main_bp.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        print(f"Mensaje de {nombre} ({correo}): {mensaje}")
        return redirect(url_for('main.contacto'))
    return render_template('contacto.html')
