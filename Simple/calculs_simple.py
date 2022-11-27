import json

def calcul(calcul):
    try:
        result = eval(str(calcul))
    except:
        result = "Erreur"
    return result

def lambda_handler(event, context):

    str_userId = event["userID"]
    str_cal = event["calc"]
    resultat = calcul(str_cal)

    if str_userId == -1:
        return json.dumps({"result":"Unauthorized"}), 401
    else:
        if resultat == "Erreur":
            return json.dumps({"result":"Bad Request"}), 400
        else:
            return json.dumps({"result":resultat}), 200