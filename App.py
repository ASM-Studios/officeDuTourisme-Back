from flask import Flask
from API.Data import api_data
from Core import Core
from flask_cors import CORS

app = Flask("office-du-tourisme")

CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(api_data)

@app.route(rule="/", methods=["GET"])
def ping():
    return "OK", 200

if __name__ == "__main__":
    Core()
    app.run(debug=True, host="0.0.0.0", port=5000)
