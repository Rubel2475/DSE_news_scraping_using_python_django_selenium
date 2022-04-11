from django.contrib import admin

# Register your models here.

from .models import userInput, Contact

admin.site.register(userInput)
admin.site.register(Contact)