from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('add',views.addTodo,name='add'),
    path('complete/<todo_id>',views.completeTodo,name ='complete'),
    path('del',views.deletecompleted,name ='del'),
    path('delall',views.delall,name ='delall'),
]