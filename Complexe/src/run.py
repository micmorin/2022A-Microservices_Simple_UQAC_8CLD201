from flask import Flask, request, jsonify
import math

def calcul(calcul):
    try:
        if calcul.find("²") != -1:
            calcul = puissance(calcul)
        if calcul.find("√") != -1:
            calcul = racine(calcul)
        result = eval(str(calcul))

        point = str(result).find(".")
        result = str(result)
        if point != -1:
            if result[point+1] == "0" :
                if ((point+1) == (len(result)-1)):
                    try:
                        result = result[:point]
                    except:
                        pass
    except:
        result = "Erreur"
    return result

def puissance(calcul):
    x = calcul.replace("²", "**2")
    return x

def racine(calcul):
    y = calcul.replace("√", "math.sqrt")
    return y

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", methods=['POST'])
    def index():
        data = request.get_json()
        str_userId = data["userID"]
        str_cal = data["calc"]
        resultat = calcul(str_cal)

        if str_userId == -1:
            return jsonify({"result":"Unauthorized"}), 401
        else:
            if resultat != "":
                return jsonify({"result":resultat}), 200
            else:
                return jsonify({"result":"Calculation failed"}), 400


    app.run(host='0.0.0.0', port=5000)