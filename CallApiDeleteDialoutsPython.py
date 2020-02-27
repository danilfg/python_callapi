import requests
import json


def RunDeleteDialOuts():
    responseDelete = DeleteDialOuts()
    if responseDelete['status'] == 'error':
        if responseDelete['errorCode'] == 10011:
            allDialOuts1 = requests.post(urlList, headers=headers, json={'token': tokenEnter}).json()
            jsonRequest = {'token': tokenEnter, 'dialoutid': allDialOuts1['result'][0]['id']}
            CompleteDialOuts()
            DeleteDialOuts()


def DeleteDialOuts():
    allDialOuts = requests.post(urlList, headers=headers, json={'token': tokenEnter}).json()
    jsonDeleteDial = {'token': tokenEnter, 'dialoutid': allDialOuts['result'][0]['id']}
    responseDelete = requests.post(urlDel, headers=headers, json=jsonDeleteDial).json()
    return (responseDelete)


def CompleteDialOuts():
    listForCompleteDial = requests.post(urlList, headers=headers, json={'token': tokenEnter}).json()
    jsonCompleteDial = {'token': tokenEnter, 'dialoutid': listForCompleteDial['result'][0]['id']}
    requests.post(urlComplete, headers=headers, json=jsonCompleteDial)


def CheckToken():
    forCheckToken = requests.post(urlList, headers=headers, json={'token': tokenEnter}).json()
    if forCheckToken['status'] == 'error':
        print("May be invalid token!")
        exit()


urlDel = 'https://callapi.gravitel.ru/api/v1/deletedialout'
urlList = 'https://callapi.gravitel.ru/api/v1/listdialouts'
urlComplete = 'https://callapi.gravitel.ru/api/v1/completedialout'

headers = {'Content-Type': 'application/json'}
tokenEnter = input("Enter token CallApi: ")

CheckToken()

counts = int(input("Enter how many auto-dialing to remove: "))
num = counts
while (counts > 0):
    RunDeleteDialOuts()
    counts -= 1
print("Delete: ", num, "autodials")
