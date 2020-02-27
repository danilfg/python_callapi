import requests
import json

def RunDeleteDialOuts (idDialouts):
    dataResponseDelete = DeleteDialOuts(idDialouts, urlDel, headers, token)
    if dataResponseDelete['errorCode'] == 10011:
        CompleteDialOuts(idDialouts, urlComplete, headers, token)
        dataResponseDelete = DeleteDialOuts(idDialouts, urlDel, headers, token)
	if dataResponseDelete['errorCode'] == 10002
		print ("Invalid token!")
		exit()

def DeleteDialOuts(idDialouts, urlDel, headers, token):
    jsonRequest = {'token':tokenEnter, 'dialoutid':idDialouts}
    responseDelete = requests.post(urlDel, headers=headers, json=jsonRequest)
    dataResponseDelete = responseDelete.json()
    return (dataResponseDelete)

def CompleteDialOuts(idDialouts, urlComplete, headers, token):
    jsonRequest = {'token':tokenEnter, 'dialoutid':idDialouts}
    responseComplete = requests.post(urlComplete, headers=headers, json=jsonRequest)
    dataResponseComplete = responseComplete.json()
    return (dataResponseComplete)

urlDel = 'https://callapi.gravitel.ru/api/v1/deletedialout'
urlList = 'https://callapi.gravitel.ru/api/v1/listdialouts'
urlComplete = 'https://callapi.gravitel.ru/api/v1/completedialout'

headers = {'Content-Type':'application/json'}

tokenEnter = input("Please enter token CallApi: ")
token = {'token':tokenEnter}

response = requests.post(urlList, headers=headers, json=token)
dataResponse = response.json()

idDialouts = dataResponse['result'][0]['id']

RunDeleteDialOuts(idDialouts)
