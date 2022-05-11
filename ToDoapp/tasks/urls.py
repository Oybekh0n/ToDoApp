
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<int:pk>', views.updateTask, name="update"),
    path('delete/<int:pk>', views.deleteTask, name='delete' ),
]