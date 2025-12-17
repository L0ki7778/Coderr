from django.contrib import admin
from .models import offers, orders, reviews


class DetailsInline(admin.TabularInline):
    model = offers.Details
    extra=1

@admin.register(offers.Offers)
class OffersAdmin(admin.ModelAdmin):
    inlines=[DetailsInline]
    
admin.site.register(orders.Orders)

admin.site.register(reviews.Review)
