from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField
from wtforms.validators import DataRequired


class ServiceAppForm(FlaskForm):
    checkbox = BooleanField('Включить сервис', validators=[DataRequired()], default=True,
                            render_kw={'onchange': "$('#checkbox').on('change', function () {"
                                                   "if ( $('#checkbox').prop('checked') ) {"
                                                   "$('.btn').attr('disabled', false);} else {"
                                                   "$('.btn').attr('disabled', true);}});",
                                       }
                            )

    submit_start = SubmitField('Start', render_kw={'class': 'btn btn-secondary btn-sm'})
    submit_stop = SubmitField('Stop', render_kw={'class': 'btn btn-secondary btn-sm'})
    submit_restart = SubmitField('Restart', render_kw={'class': 'btn btn-secondary btn-sm'})
