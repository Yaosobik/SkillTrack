from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def grades():
    return render_template('glavnaya.html')

@app.route('/sign')
def sign_in():
    return render_template('sign.html')

@app.route('/registration')
def registration():
    return render_template('registr.html')

if __name__ == "__main__":
    app.run(debug=True)