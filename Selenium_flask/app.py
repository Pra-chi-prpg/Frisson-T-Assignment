from flask import Flask, jsonify
import sys
import os
backend_path = os.path.join(os.path.dirname(__file__), 'Backend(Selenium Script)')
print("BACKEND PATH:", backend_path)

sys.path.append(backend_path)
from main import scrape_it_companies  

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    output_csv, data = scrape_it_companies()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

