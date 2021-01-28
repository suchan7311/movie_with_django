
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('searchMovie/',views.searchMovie,name="searchMovie"),
    path('searchReview/',views.searchReview,name="searchReview"),
    path('createReview/',views.createReview,name="createReview")
]
