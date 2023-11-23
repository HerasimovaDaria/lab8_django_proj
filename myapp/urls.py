from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('table/', views.table_view, name='table_view'),
]
