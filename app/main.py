from flask import Flask, request, make_response, redirect, render_template, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    respose = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return respose


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
