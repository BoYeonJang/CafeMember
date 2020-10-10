from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template(
        'index.html'
    )


@bp.route('/login')
def login():
    return render_template(
        'login.html'
    )


@bp.route('/register')
def register():
    return render_template(
        'register.html'
    )


@bp.route('/find')
def find():
    return render_template(
        'find.html'
    )


@bp.route('/logout')
def logout():
    return render_template(
        'logout.html'
    )


@bp.route('/allView')
def allView():
    return render_template(
        'allView.html'
    )
