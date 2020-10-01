from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path("<int:cd_id>/", views.cd_detail, name="cd_detail"),
]
