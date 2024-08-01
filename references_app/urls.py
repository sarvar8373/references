from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="references_app"),
    path("soato/", views.soato, name="soato"),
    path("oked/", views.oked, name="oked"),
    path("okonx/", views.okonx, name="okonx"),
    path("opf/", views.opf, name="opf"),
    path("soogu/", views.soogu, name="soogu"),
    path("fs/", views.fs, name="fs"),
    path("doctype/", views.doctype, name="doctype"),
    path("country/", views.country, name="country"),
    path("nation/", views.nation, name="nation"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
]