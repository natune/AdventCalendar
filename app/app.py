from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
