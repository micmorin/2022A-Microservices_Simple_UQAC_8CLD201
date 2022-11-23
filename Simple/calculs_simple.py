from flask import Flask, request, jsonify

def calcul(calcul):
    try:
        result = eval(str(calcul))
    except:
        result = "Erreur"
    return result

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def index():
        #data = request.get_json()
        data = {"calc": "8/0"}
        str_cal = data["calc"]
        resultat = calcul(str_cal)
        return jsonify({"result":resultat})

    app.run(host='0.0.0.0', port=5000)