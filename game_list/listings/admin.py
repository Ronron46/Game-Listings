from django.contrib import admin
from listings.models import Game



class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'developpeur')

admin.site.register(Game,GameAdmin)

# Register your models here.
