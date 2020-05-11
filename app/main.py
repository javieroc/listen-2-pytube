from flask import Flask, request, render_template, url_for, redirect
from forms import DownloadForm
from downloader import download

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
# app.config['RECAPTCHA_PUBLIC_KEY'] = 'recaptchapublickey'
# app.config['RECAPTCHA_PRIVATE_KEY'] = 'recaptchaprivatekey'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DownloadForm(request.form)

    if request.method == 'POST' and form.validate():
        url = form.url.data
        data = download(url)
        app.logger.debug(data)
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
