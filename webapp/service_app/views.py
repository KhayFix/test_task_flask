from flask import Blueprint, redirect, url_for, request
from flask import render_template

from webapp.service_app.forms import ServiceAppForm
from webapp.service_app.demon_control.service_management import service_running

blueprint = Blueprint('service', __name__, template_folder='templates', )


@blueprint.route('/')
def service_apache():
    title = "apache2"
    form = ServiceAppForm()

    output = service_running(command='status', name_app=title)
    if output == 0:
        service_state = True
    elif output == 3:
        service_state = False
    elif output == 4:
        service_state = None  # сервис не найден
    else:
        service_state = 'error'

    return render_template('service_app/management_apache.html', title=title,
                           service_state=service_state, form=form)


@blueprint.route('/process-service-apache', methods=['GET', 'POST'])
def process_service_apache():
    title = 'apache2'
    if request.method == 'POST':
        buttons_data = request.form.to_dict(flat=False)
        button_value = [value for value in buttons_data.values()][-1][0]

        output = service_running(command=f'{button_value.lower()}', name_app=title)
    return redirect(url_for('service.service_apache'))


@blueprint.route('/asterisk')
def service_asterisk():
    title = "Service_name = asterisk"
    return render_template('service_app/management_asterisk.html', title=title)
