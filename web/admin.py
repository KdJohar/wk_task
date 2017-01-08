from django.contrib import admin
from .models import Categories, SubCategories, Product
# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Product)