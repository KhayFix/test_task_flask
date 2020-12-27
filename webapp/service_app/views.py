from datetime import datetime

from flask import Blueprint, redirect, url_for, request
from flask import render_template
from sqlalchemy.orm.exc import NoResultFound

from webapp.db import db
from webapp.service_app.forms import ServiceAppForm
from webapp.service_app.demon_control.service_management import service_app
from webapp.service_app.models import CheckboxState

blueprint = Blueprint('service', __name__, template_folder='templates', )


@blueprint.route('/')
def service_apache():
    """
    service_running возвращает такие значение 0, 3, 4, False.

    0 - сервис работает.
    3 - сервис не работает
    4 - сервис не найден в системе.
    False - ошибка.
    """
    title = "apache2"
    form = ServiceAppForm()
    checkbox = CheckboxState.query.filter_by(id=1).first()  # Получаем состояние чекбокса из базы данных.
    # В базе данных храниться последнее состояние чекбокса.
    output = service_app.running(command='status', name_app=title)

    return render_template('service_app/management_apache.html', title=title,
                           service_state=output, form=form, chk=checkbox)


@blueprint.route('/process-service-apache', methods=['GET', 'POST'])
def process_service_apache():
    title = 'apache2'
    if request.method == 'POST':
        buttons_data = request.form.to_dict()
        button_value = [value for value in buttons_data.values()][-1]

        service_app.running(command=f'{button_value.lower()}', name_app=title)
    return redirect(url_for('service.service_apache'))


@blueprint.route('/state-checkbox', methods=["POST"])
def state_checkbox():
    if request.method == "POST":
        state_chk: bool = request.json['chk']
        try:
            # chk = db.session.query(CheckboxState).filter_by(id=1).one()
            chk = CheckboxState.query.filter_by(id=1).one()
            chk.bool_state = state_chk
            chk.press_time = datetime.now()

        except NoResultFound:
            chk = CheckboxState(bool_state=state_chk)
            db.session.add(chk)

        db.session.commit()
    return redirect(False)


@blueprint.route('/asterisk')
def service_asterisk():
    title = "Service_name = asterisk"
    return render_template('service_app/management_asterisk.html', title=title)
