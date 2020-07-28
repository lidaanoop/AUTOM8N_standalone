from celery import Celery
import subprocess

app = Celery('autom8ntaskq', broker='redis://localhost:6379/0', backend="redis://localhost:6379/0")


@app.task
def displaycelery():
    # x = subprocess.call('sudo yum -y install nginx', shell=True,)
    x = subprocess.call('ansible-playbook autom8n.yml --extra-vars '{"version":"username","other_variable":"password","domainname":"domainname"}'', shell=True)
    return (x)
