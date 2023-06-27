from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Offers)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Address)