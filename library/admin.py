from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

#admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
#admin.site.register(Review)
@admin.register(Book)
class  ViewAdmin(ImportExportModelAdmin):
    pass