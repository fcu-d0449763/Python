from flask import session, render_template, url_for
from werkzeug.utils import redirect

from app.models import db

from functools import wraps
def init_ext(app):

    db.init_app(app)


def is_login(func):
    @wraps(func)
    def check(*args,**kwargs):
        try:
            session['user_id']
        except:
            return redirect(url_for('user.login'))

        return func(*args,**kwargs)
    return check

