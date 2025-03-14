from django.contrib import admin
from .models import tbl_application, tbl_bank, tbl_branch
# Register your models here.
admin.site.register(tbl_branch)
admin.site.register(tbl_bank)
admin.site.register(tbl_application)