from django.contrib import admin

from .models import Navbar, Footer, Link


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'department']


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'department']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'url']

