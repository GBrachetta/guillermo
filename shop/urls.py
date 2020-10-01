from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path("<int:cd_id>/", views.cd_detail, name="cd_detail"),
    path("add/", views.add_cd, name="add_cd"),
    path("edit/<int:cd_id>/", views.edit_cd, name="edit_cd"),
]
