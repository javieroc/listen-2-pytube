from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired

class DownloadForm(FlaskForm):
    url = StringField('url', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
