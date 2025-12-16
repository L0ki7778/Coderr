from django.contrib import admin
from .models import offers


class DetailsInline(admin.TabularInline):
    model = offers.Details
    extra=1

@admin.register(offers.Offers)
class OffersAdmin(admin.ModelAdmin):
    inlines=[DetailsInline]