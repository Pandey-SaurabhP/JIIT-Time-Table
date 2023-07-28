from flask import Flask, request, jsonify
from flask_cors import CORS
from extract import getBatchDetails, loadData

app = Flask(__name__)
CORS(app)

data = loadData()

@app.route('/', methods=['POST'])
def get_data():
    try:
        key = request.get_json()

        print(key)

        batchData = getBatchDetails(data, key)

        return jsonify((batchData))

    except Exception as e:
        return jsonify(("Aloha"))

if __name__ == '__main__':
    app.run(debug=True)

