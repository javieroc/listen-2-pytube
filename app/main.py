from flask import Flask, request, render_template, url_for, redirect, send_from_directory
from forms import DownloadForm
from downloader import download

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DownloadForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        url = form.url.data
        app.logger.debug(url)
        filename = download(url)
        app.logger.debug(filename)
        return send_from_directory('/app/data', filename, as_attachment=True)# and redirect(url_for('index'))

    return render_template('index.html', form=form, redirect_url=url_for('index'))


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
