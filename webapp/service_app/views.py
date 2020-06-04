from flask import Blueprint
from flask import render_template

blueprint = Blueprint('service', __name__, template_folder='templates',)


@blueprint.route('/')
def service_apache():
    title = "service_name = apache2"
    return render_template('service_app/management_apache.html', title=title)


@blueprint.route('/asterisk')
def service_asterisk():
    title = "service_name = asterisk"
    return render_template('service_app/management_asterisk.html', title=title)
