from django.contrib import admin
from django.urls import path, include
from myapp.views import table_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', table_view, name='home'),
    path('myapp/', include('myapp.urls', namespace='myapp')),
]
