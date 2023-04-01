from django.contrib import admin
from .models import (
    Company,
    Product
)

mdls = [Company, Product]

admin.site.register(mdls)