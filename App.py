from flask import Flask
from API.Data import api_data
from Core import Core

app = Flask("office-du-tourisme")

app.register_blueprint(api_data)

@app.route(rule="/", methods=["GET"])
def ping():
    return "OK", 200

if __name__ == "__main__":
    Core()
    app.run(debug=True, host="0.0.0.0", port=5000)