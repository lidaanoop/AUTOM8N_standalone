from celery import Celery
import subprocess, json
from requests import get
from flask import Flask, render_template, request, redirect, session, url_for

app = Celery('autom8ntaskq', broker='redis://localhost:6379/0', backend="redis://localhost:6379/0")


@app.task
def displaycelery(username1,password,domainname):
    dictionary={
    "username": username1,
    "password": password,
    "domainname": domainname
    }
    json_object = json.dumps(dictionary, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        # x = subprocess.call('sudo yum -y install nginx', shell=True,)
        x = subprocess.call('ansible-playbook -i hosts plays/autom8n.yaml --extra-vars "@sample.json"', shell=True)

    return (x)

@app.task
def displaycelery1(username,domainname):
    dict ={
    "username": username,
    "domainname": domainname
    }
    json_object = json.dumps(dict, indent = 4)
    with open("sample1.json","w")as outfile:
        outfile.write(json_object)
    with open("sample1.json","r")as openfile:
        json_object = json.load(openfile)
        x = subprocess.call('ansible-playbook -i hosts plays/autom8n_user.yaml --extra-vars "@sample1.json"', shell=True)
    return(x)
