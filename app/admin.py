from django.contrib import admin
from app.models import CodeTestItem


# Register your models here.
class CodeTestAdmin(admin.ModelAdmin):
    list_display = ['source_code', 'test_code']


admin.site.register(CodeTestItem, CodeTestAdmin)
