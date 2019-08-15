from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

# Creating a task instance
app.config_from_object('celeryconfig')

# Defining a single task called add.
@app.task
def add(x, y):
    return x + y

# Calling task and storing result
result = add.delay(4, 4)
print(result)
