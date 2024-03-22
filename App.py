from flask import Flask
from API.Data import api_data

app = Flask("office-du-tourisme")

app.register_blueprint(api_data)

if __name__ == "__main__":
    app.run(debug=True)