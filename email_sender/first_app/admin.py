from django.contrib import admin
from first_app.models import UserSignUp
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(UserSignUp)
class ViewAdmin(ImportExportModelAdmin):
    pass