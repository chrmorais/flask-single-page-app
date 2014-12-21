from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        value_one = int(request.form['number-one'])
        value_two = int(request.form['number-two'])
        total = value_one + value_two
        # passing in an argument called 'String'
        # this is part of jinja templating
        return render_template('index.html', value=total)
    return render_template('index.html' )
        


@app.route("/name")
def name():
    return render_template('name.html')


if __name__ == "__main__":
    app.run(debug=True)
