from django.contrib import admin
from .models import Постачальники, Матеріали, Поставки

admin.site.register(Постачальники)
admin.site.register(Матеріали)
admin.site.register(Поставки)