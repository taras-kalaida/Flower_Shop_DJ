from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(Composition)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Season)
admin.site.register(Specification)
