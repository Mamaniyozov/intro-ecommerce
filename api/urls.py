from django.urls import path
# import views
from .views import (
    ProductView,
)

urlpatterns = [
   path('products', ProductView.as_view()), 
   path('products/<int:id>', ProductView.as_view()),
   path('add_product/',ProductView.as_view()),
   path('updeta/',ProductView.as_view())
]
