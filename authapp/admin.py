from django.contrib import admin
from .models import UserData
from .models import AddMovie,Comment

# Register your models here.
admin.site.register(UserData)
admin.site.register(AddMovie)
admin.site.register(Comment)
