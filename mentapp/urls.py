from django.urls import path
from .views import *

urlpatterns = [
    path('', startpage, name="startpage"),
    path('new-post',new_post, name="newpost"),



]
