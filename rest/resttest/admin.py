from django.contrib import admin
from .models import Article,Publication
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list = [id,'name']
admin.site.register(Article)
admin.site.register(Publication)
