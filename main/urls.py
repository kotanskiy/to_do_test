from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update_tasks$', views.get_tasks, name='update_tasks'),
    url(r'^create_task$', views.create_task, name='create_task'),
    url(r'^search$', views.search, name='search'),
]