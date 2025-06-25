from flask import Blueprint, render_template, request, redirect, session, url_for

auth_bp = Blueprint('auth', __name__)

# Simulación de usuarios
usuarios = {
    'admin': {'password': 'admin123', 'rol': 'admin'},
    'cliente': {'password': 'cliente123', 'rol': 'cliente'}
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        clave = request.form['password']

        if usuario in usuarios and usuarios[usuario]['password'] == clave:
            session['usuario'] = usuario
            session['rol'] = usuarios[usuario]['rol']
            if session['rol'] == 'admin':
                return redirect(url_for('admin.admin_home'))
            else:
                return redirect(url_for('auth.cliente_home'))
        return "Credenciales incorrectas"
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@auth_bp.route('/cliente')
def cliente_home():
    if 'rol' in session and session['rol'] == 'cliente':
        return render_template('cliente.html')
    return redirect(url_for('auth.login'))

    @auth_bp.route('/admin')
def admin_home():
    if 'rol' in session and session['rol'] == 'admin':
        return render_template('admin.html')
    return redirect(url_for('auth.login'))

