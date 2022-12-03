from django.urls import path
from .views import post_list, post_atributes


app_name = "cv_blog"
urlpatterns = [
    path('', post_list, name = 'post_list'),
    path('<slug:get_slug>', post_atributes, name = 'post_atributes'),
]