from flask import Blueprint, render_template, session, redirect, url_for

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_home():
    if 'rol' in session and session['rol'] == 'admin':
        return render_template('admin.html')
    return redirect(url_for('auth.login'))
