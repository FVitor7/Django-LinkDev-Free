from django.contrib import admin
from core.models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_create')
    list_filter = ('user', 'date_create',)


admin.site.register(Link, LinkAdmin)
