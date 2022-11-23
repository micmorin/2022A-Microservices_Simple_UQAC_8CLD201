from flask import Flask, request, jsonify

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/")
    def index():
        data = request.get_json()
        calcl = data["calc"]


        resultat =0
        return jsonify({"result":resultat})


    app.run(host='0.0.0.0', port=5000)