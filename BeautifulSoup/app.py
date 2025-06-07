
from flask import Flask, request, jsonify
from main import download_images  

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/scrape-images', methods=['GET','POST'])
def scrape_images():
    query = request.args.get('query', default='vbbsss', type=str)
    downloaded = download_images(query)
    return jsonify({
        "status": "success",
        "query": query,
        "images_downloaded": downloaded

    })


if __name__ == '__main__':
    app.run(debug=True)
