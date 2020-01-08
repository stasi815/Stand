from django.contrib import admin

from .models import Auction, Item, Organization
# Register your models here.
admin.site.register(Auction)
admin.site.register(Item)
admin.site.register(Organization)