from huey.contrib.djhuey import task
from time import sleep

@task()
def add_numbers(a,b):
    result = a+b
    sleep(10)
    return result