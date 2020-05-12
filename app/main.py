import os
from flask import Flask, request, render_template, url_for, redirect, send_from_directory, make_response
from forms import DownloadForm
from downloader import download_video, download_music

if not os.path.exists('./data'):
    os.makedirs('./data')

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
        media_format = form.media_format.data
        download_token = form.download_token.data

        if media_format == 'video':
            filename = download_video(url)
        else:
            filename = download_music(url)

        response = make_response(send_from_directory('/app/data', filename, as_attachment=True))
        response.set_cookie('download_token', download_token)
        return response

    return render_template('index.html', form=form, redirect_url=url_for('index'))


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
