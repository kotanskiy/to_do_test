import random
import string

from main.models import Task


def random_string(length):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(length)])

def create_random_tasks(count):
    i = 0
    while i < count:
        Task(name=random_string(50),
             description=random_string(50)).save()
        i += 1

def remove_tasks():
    for task in Task.objects.all():
        task.delete()

