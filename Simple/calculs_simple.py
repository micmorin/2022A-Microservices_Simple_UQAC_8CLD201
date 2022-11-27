import json
#import requests

def calcul(calcul):
    try:
        resultat = str(eval(str(calcul)))
    except:
        resultat = ""
    return resultat
    
def store(userID, calc):
    try:
        resultat = calcul(calc)
        if resultat != "":
            
            #### USE REQUESTS to send to DB and Act on response code HERE #####
            
            
            body = "{\"message\":\"OK\", \"result\":"+resultat+"}"
            status = 200
        else :
            body = "{\"message\":\"Calculation failed\", \"result\":\"\"}"
            status = 510
    except:
        body = "{\"message\":\"Storing failed\", \"result\":\"\"}"
        status = 520
    
    return [body, status]
    
def returnBuilder(body, status):
    return {
        "isBase64Encoded": 'true',
        "statusCode": status,
        "headers": {"content-type":"application/json"},
        "body": body}
    

def lambda_handler(event, context):

    body = json.loads(event["body"])
    userID = body["userID"]
    calc = body["calc"]
    [body, status] = store(userID, calc)
    return returnBuilder(body, status)
