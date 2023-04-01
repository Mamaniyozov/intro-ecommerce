from django.contrib import admin
from .models import (
    Company,
    Product,
    Category
)

mdls = [Company, Product, Category]

admin.site.register(mdls)