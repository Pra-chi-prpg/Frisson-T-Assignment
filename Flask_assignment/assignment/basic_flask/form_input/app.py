from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Hello, {name}!Your email is {email}"
    return render_template('index.html')

if __name__ == ('__main__'):
    app.run(debug=True)
