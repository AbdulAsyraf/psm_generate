import requests
import pandas as pd
import model

username = "user2"

def new_model():
    combined_data = model.getData(username)
    send = combined_data.to_json(orient='split')
    stuff = {'username': username}

    res = requests.post('http://localhost:5000/learn', data = stuff, json = send)
    if res.ok:
        print(res.text)

def predict():
    combined_data = model.getData(username)
    send = combined_data.to_json(orient='split')
    stuff = {'username': username}

    res = requests.post('http://localhost:5000/predict', data = stuff, json = send)
    if res.ok:
        print(res.json())

def test():
    combined_data = model.getData(username)
    send = combined_data.to_json(orient='split')
    stuff = {'username': username}
    print(stuff)
    res = requests.post('http://localhost:5000/test', data = stuff, json = send)
    if res.ok:
        print(res.text)

test()

