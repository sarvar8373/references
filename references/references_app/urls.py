from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="references_app"),
    path("references/", views.reflists, name="references"),
    path("soato/", views.soato, name="soato"),
    path("oked/", views.oked, name="oked"),
    path("okonx/", views.okonx, name="okonx"),
    path("opf/", views.opf, name="opf"),
    path("soogu/", views.soogu, name="soogu"),
    path("fs/", views.fs, name="fs"),
    path("doctype/", views.doctype, name="doctype"),
    path("country/", views.country, name="country"),
    path("nation/", views.nation, name="nation"),
    path('category-search/', views.category_search, name='category_search'),
    path('import/', views.import_classifier, name='import_classifier'),
    path('adminpage/references', views.references, name='adminpage/references'),
    # path('categories/create/', views.category_create, name='category_create'),
    # path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    # path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

]