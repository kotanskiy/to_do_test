from django.http import response
from django.shortcuts import render, render_to_response

from main.models import Task


def index(request):
    return render(request, 'main/index.html')

def create_task(request):
    if request.method == 'POST' and request.POST['name'] and request.POST['description']:
        task = Task(name=request.POST.get('name'), description=request.POST.get('description'))
        task.save()
        return response.HttpResponse('success')


def get_tasks(request):
    context = {
        'tasks': Task.objects.all().order_by('-id')
    }
    return render_to_response('main/list.html', context)

def search(request):
    text = request.GET.get('text')
    if len(text.strip()) > 3:
        context = {
            'tasks': Task.objects.filter(name__contains=text)
        }
        return render_to_response('main/search_results.html', context)