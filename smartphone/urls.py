from django.urls import path
from .views import (
    phone,
    get_by_ram,
    get_by_rams,
    get_by_price
)

urlpatterns = [
    path('smartphones/<int:id>', phone),
    path('smartphones/', phone),
    path('get-by-ram/<int:ram>',get_by_ram),
    path('get-by-ram/',get_by_rams),
    path('get-by-price/',get_by_price)
]
