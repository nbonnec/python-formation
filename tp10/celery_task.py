from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost//')


@app.task
def hello():
    return 'hello world'
