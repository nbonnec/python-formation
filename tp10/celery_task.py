from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost//', backend='redis://localhost:6379/0')


@app.task
def hello():
    return 'hello world'
