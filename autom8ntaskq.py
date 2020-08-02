from celery import Celery
import subprocess, json
from requests import get
from flask import Flask, render_template, request, redirect, session, url_for

app = Celery('autom8ntaskq', broker='redis://localhost:6379/0', backend="redis://localhost:6379/0")


@app.task
def displaycelery():
    dictionary={
    "username": " +username1+ ",
    "password": "+password+",
    "domainname": "+domainname+"
    }
    json_object = json.dumps(dictionary, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    # x = subprocess.call('sudo yum -y install nginx', shell=True,)
    x = subprocess.call('ansible-playbook -i hosts autom8n.yaml --extra-vars sample.json', shell=True)

    return (x)
