from django.urls import path

from . import views

app_name = "restaurants"
urlpatterns = [
    path("", views.restaurant_list, name="index"),
    path("<int:restaurant_id>/", views.restaurant_detailed, name="detailed"),
    path("<int:restaurant_id>/menu", views.restaurant_menu, name="menu")

    # NEED THE ORDERS PAGE
]