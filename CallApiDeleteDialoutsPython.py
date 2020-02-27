import requests
import json

def RunDeleteDialOuts ():
    dataResponseDelete = DeleteDialOuts()
    if allDialOuts['status'] == 'error':
        if dataResponseDelete['errorCode'] == 10011:
            allDialOuts1 = requests.post(urlList, headers=headers, json={'token':tokenEnter}).json()
            print(allDialOuts1['result'][0]['id'])
            jsonRequest = {'token':tokenEnter, 'dialoutid':allDialOuts1['result'][0]['id']}
            CompleteDialOuts()
            DeleteDialOuts()

def DeleteDialOuts():
	allDialOuts1 = requests.post(urlList, headers=headers, json={'token':tokenEnter}).json()
	jsonRequest = {'token':tokenEnter, 'dialoutid':allDialOuts1['result'][0]['id']}
	responseDelete = requests.post(urlDel, headers=headers, json=jsonRequest)
	dataResponseDelete = responseDelete.json()
    return (dataResponseDelete)
    
def CompleteDialOuts():
    requests.post(urlComplete, headers=headers, json=jsonRequest)

def CheckToken():
	if allDialOuts['status'] == 'error':
		if allDialOuts['errorCode'] == 10002:
			print ("Invalid token!")
			exit()

urlDel = 'https://callapi.gravitel.ru/api/v1/deletedialout'
urlList = 'https://callapi.gravitel.ru/api/v1/listdialouts'
urlComplete = 'https://callapi.gravitel.ru/api/v1/completedialout'

counts = 1;
headers = {'Content-Type':'application/json'}
tokenEnter = input("Enter token CallApi: ")
allDialOuts = requests.post(urlList, headers=headers, json={'token':tokenEnter}).json()
CheckToken()

counts = int(input("Enter how many auto-dialing to remove: "))

jsonRequest = {'token':tokenEnter, 'dialoutid':allDialOuts['result'][0]['id']}

while (counts > 0):
	RunDeleteDialOuts()
	counts -= 1
