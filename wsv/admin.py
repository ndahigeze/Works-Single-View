from django.contrib import admin

# Register your models here.
from wsv.models import WorkMetadata, Contributor

admin.site.register(WorkMetadata)

admin.site.register(Contributor)
