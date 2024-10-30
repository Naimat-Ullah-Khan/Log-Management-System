from django.contrib import admin
from logs.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id" ,"name","price"]

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ["log_type","message","created_at"]
