from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

app.config_from_object('celeryconfig.py')

@app.task
def add(x, y):
    return x + y
