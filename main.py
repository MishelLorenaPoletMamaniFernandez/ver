from flask import Flask, render_template, request, redirect, url_for, session
from forms.login_form import LoginForm

app = Flask(__name__)
app.secret_key = 'miclave123'  # Necesario para usar sesiones

# ---------- DATOS SIMULADOS SIN BASE DE DATOS ----------
usuarios = {
    'admin': {'password': 'admin123', 'rol': 'admin'},
    'cliente': {'password': 'cliente123', 'rol': 'cliente'}
}

productos = [
    {"id": 1, "nombre": "Cerveza Artesanal", "precio": 20},
    {"id": 2, "nombre": "Agua Mineral", "precio": 10},
    {"id": 3, "nombre": "Jugo Natural", "precio": 15},
]

compra_actual = {
    "cliente": "usuario_demo",
    "productos": [productos[0], productos[2]],
    "total": productos[0]["precio"] + productos[2]["precio"]
}
# -------------------------------------------------------

# --- DATOS PARA ADMINISTRACIÓN (simulados) ---

# Productos
productos_admin = [
    {"id": 1, "nombre": "Cerveza Artesanal", "precio": 20, "stock": 100},
    {"id": 2, "nombre": "Agua Mineral", "precio": 10, "stock": 200},
    {"id": 3, "nombre": "Jugo Natural", "precio": 15, "stock": 150},
]

# Empleados y cargos
empleados = [
    {"nombre": "Juan Pérez", "cargo": "Repartidor"},
    {"nombre": "Ana Gómez", "cargo": "Vendedora"},
    {"nombre": "Carlos Ruiz", "cargo": "Supervisor"},
]

# Distribución
distribuciones = [
    {"zona": "Zona Sur", "vehiculo": "Camión 1", "responsable": "Juan Pérez"},
    {"zona": "Centro", "vehiculo": "Camión 2", "responsable": "Ana Gómez"},
]

# Ventas (facturas)
ventas = [
    {"cliente": "cliente1", "productos": [productos_admin[0], productos_admin[2]], "total": 35},
    {"cliente": "cliente2", "productos": [productos_admin[1]], "total": 10}
]

# ---------- RUTAS PÚBLICAS ----------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        print(f"Mensaje recibido de {nombre} ({correo}): {mensaje}")
        return redirect(url_for('contacto'))
    return render_template('contacto.html')
# ------------------------------------

# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = form.username.data
        clave = form.password.data

        if usuario in usuarios and usuarios[usuario]['password'] == clave:
            session['usuario'] = usuario
            session['rol'] = usuarios[usuario]['rol']
            if session['rol'] == 'admin':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('cliente'))
        else:
            return "Usuario o contraseña incorrectos"
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
# -----------------------
# ---------- ADMIN ----------
@app.route('/admin')
def admin():
    if 'rol' in session and session['rol'] == 'admin':
        return render_template('admin.html')
    return redirect(url_for('login'))
# ---------------------------

@app.route('/admin/productos')
def admin_productos():
    if session.get('rol') == 'admin':
        return render_template('admin_productos.html', productos=productos_admin)
    return redirect(url_for('login'))

@app.route('/admin/empleados')
def admin_empleados():
    if session.get('rol') == 'admin':
        return render_template('admin_empleados.html', empleados=empleados)
    return redirect(url_for('login'))

@app.route('/admin/distribucion')
def admin_distribucion():
    if session.get('rol') == 'admin':
        return render_template('admin_distribucion.html', distribuciones=distribuciones)
    return redirect(url_for('login'))

@app.route('/admin/ventas')
def admin_ventas():
    if session.get('rol') == 'admin':
        return render_template('admin_ventas.html', ventas=ventas)
    return redirect(url_for('login'))

# ---------- CLIENTE Y PRODUCTOS ----------
@app.route('/cliente')
def cliente():
    if 'rol' in session and session['rol'] == 'cliente':
        return render_template('cliente.html')
    return redirect(url_for('login'))

@app.route('/cliente/productos')
def ver_productos():
    if 'rol' in session and session['rol'] == 'cliente':
        return render_template('productos.html', productos=productos)
    return redirect(url_for('login'))

@app.route('/cliente/factura')
def ver_factura():
    if 'rol' in session and session['rol'] == 'cliente':
        return render_template('factura.html', compra=compra_actual)
    return redirect(url_for('login'))

@app.route('/cliente/detalle-compra')
def detalle_compra():
    if 'rol' in session and session['rol'] == 'cliente':
        return render_template('detalle_compra.html', productos=compra_actual["productos"])
    return redirect(url_for('login'))
# ------------------------------------------

# app.py (en la raíz del proyecto)
if __name__ == '__main__':
    app.run(debug=True)


