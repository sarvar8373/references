from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('ad', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('account/logout/', views.logout_view, name='logout'),
    # path('adminpage/references', views.references, name='adminpage/references'),
    path('users/', views.users, name='users'),
    path('profile/', views.account_view, name='profile'),
    path('categories/manage_table_headers/<int:category_id>/', views.manage_table_headers, name='manage_table_headers'),
    path('adminpage/katalog', views.category_list, name='adminpage/katalog'),
    path('adminpage/create_category', views.create_category, name='create_category'),
    path(
        'categories/manage_table_rows/<int:category_id>/<int:header_id>/',
        views.manage_table_rows,
        name="manage_table_rows",
    ),
    path('references/<int:category_id>/', views.references_table, name='references_table'),
    path('adminpage/settings', views.settings, name='settings'),
    # path('adminpage/katalog', views.category_list, name='adminpage/katalog'),
]