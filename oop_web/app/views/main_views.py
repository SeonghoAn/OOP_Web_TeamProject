from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/unittest')
def test():
    return 'Hello!'

@bp.route('/')
def index():
    return redirect(url_for('article._list'))


