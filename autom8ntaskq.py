from celery import Celery

app = Celery('autom8ntaskq', broker='redis://localhost:6379/0')

@app.task
def displaycelery(x):
    return(x)