from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, HiddenField, RadioField
from wtforms.validators import DataRequired, Regexp

class DownloadForm(FlaskForm):
    url = StringField('url', validators=[DataRequired(), Regexp('^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', message="Invalid Youtube URL")])
    media_format = RadioField('Media', choices=[('video','Video'),('audio','Audio')], default='video')
    download_token = HiddenField('download_token')
    # recaptcha = RecaptchaField()
