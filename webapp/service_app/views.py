import subprocess
from flask import Blueprint, redirect, url_for, request
from flask import render_template

blueprint = Blueprint('service', __name__, template_folder='templates', )


@blueprint.route('/', methods=['GET', 'POST'])
def service_apache():
    title = "apache2"
    output = subprocess.check_output(['ps', '-A'])
    if title in str(output):
        service_state = True  # приложение запущенно
    else:
        service_state = False

    # return redirect(url_for('service.service_apache'))
    return render_template('service_app/management_apache.html', title=title, service_state=service_state)


@blueprint.route('/asterisk')
def service_asterisk():
    title = "service_name = asterisk"
    return render_template('service_app/management_asterisk.html', title=title)
