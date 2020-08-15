from django.contrib import admin
from .models import *

@admin.register(SoccerField)
class SoccerFieldAdmin(admin.ModelAdmin):
    #readonly_fields = ('getValue')
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    pass