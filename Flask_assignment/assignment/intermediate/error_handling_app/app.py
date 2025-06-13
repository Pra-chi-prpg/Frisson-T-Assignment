from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/error')
def error():
    return 1 / 0

# Custom 404 Error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Custom 500 Error
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True,port=5004)
