from celery import Celery
import subprocess, json

app = Celery('autom8ntaskq', broker='redis://localhost:6379/0', backend="redis://localhost:6379/0")


@app.task
def displaycelery():
    username1 = request.form['username']
    password = request.form['password']
    domainname = request.form['domainname']
    dictionary={
    "username":username1,
    "password": password,
    "domainname":domainname
    }
    json_object = json.dumps(dictionary, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    # x = subprocess.call('sudo yum -y install nginx', shell=True,)
    x = subprocess.call('ansible-playbook -i hosts autom8n.yaml --extra-vars @sample.json', shell=True)

    return (x)
