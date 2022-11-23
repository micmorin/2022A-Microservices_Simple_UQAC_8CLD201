from flask import Flask, request, jsonify
import math

def calcul(calcul):
    #Fonction qui calcule le résultat d'un calcul simple
    if calcul.find("²") != -1:
        print(calcul)
        calcul = puissance(calcul)
        print(calcul)
    if calcul.find("√") != -1:
        calcul = racine(calcul)
    result = eval(str(calcul))
    return result

def puissance(calcul):
    x = calcul.replace("²", "**2")
    return x

def racine(calcul):
    y = calcul.replace("√", "math.sqrt")
    return y

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def index():
        print("index")
        #data = request.get_json()
        data = {"calc": "√(4*5²)²*√(9)"}

        str_cal = data["calc"]
        
        resultat = calcul(str_cal)

        return jsonify({"result":resultat})


    app.run(host='0.0.0.0', port=5000)