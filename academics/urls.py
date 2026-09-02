from django.urls import path

from . import views


urlpatterns = [
    # Course URLs
    path('', views.course_list, name='course_list'),
    path('add/', views.course_create, name='course_create'),
    path('edit/<int:id>/', views.course_update, name='course_update'),
    path('delete/<int:id>/', views.course_delete, name='course_delete'),

    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.subject_create, name='subject_create'),
    path('subjects/edit/<int:id>/', views.subject_update, name='subject_update'),
    path('subjects/delete/<int:id>/', views.subject_delete, name='subject_delete'),
]