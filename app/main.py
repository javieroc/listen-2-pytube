from flask import Flask, render_template
from forms import DownloadForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
# app.config['RECAPTCHA_PUBLIC_KEY'] = 'recaptchapublickey'
# app.config['RECAPTCHA_PRIVATE_KEY'] = 'recaptchaprivatekey'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    form = DownloadForm()
    return render_template('index.html', form=form)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
