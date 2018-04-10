from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about/')      # About Page
def about():
    return render_template("about.html")

@app.route('/')      # Homepage
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)