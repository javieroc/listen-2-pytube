from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class DownloadForm(FlaskForm):
    url = StringField('url', validators=[DataRequired()])
    download_token = HiddenField('download_token')
    # recaptcha = RecaptchaField()
