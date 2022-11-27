import json

def calcul(calcul):
    try:
        result = eval(str(calcul))
    except:
        result = "Erreur"
    return result

def lambda_handler(event, context):

    str_cal = event["calc"]
    resultat = calcul(str_cal)
    return json.dumps({"result":resultat})