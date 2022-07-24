from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/payeer_1706208548.txt')
def payeer_1706208548():
    return render_template('payeer_1706208548.txt')


if __name__ == '__main__':
    app.run(debug=True)
