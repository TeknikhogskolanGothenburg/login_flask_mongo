from flask import Blueprint, render_template
from flask_login import login_required

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/')
@login_required
def profile():
    return render_template('profile.html')