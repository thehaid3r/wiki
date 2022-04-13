from django.urls import path

from . import views

urlpatterns = [
    path("edit/<str:title>",views.edit,name="edit"),
    path("wiki/<str:title>",views.wiki,name="wiki"),
    path("random/",views.random,name="random"),
    path("newentry",views.new_entry,name="new_entry"),
    path("searchbar",views.searchbar,name="searchbar"),
    path("notfound/", views.notfound, name="notfound"),
    path("", views.index, name="index")
]
