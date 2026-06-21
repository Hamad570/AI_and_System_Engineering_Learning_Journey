from django.urls import path
from . import views

urlpatterns=[path('students/',views.studentviews.as_view(),name='student-list'),
            path("students/<int:pk>/delete/", views.studentdelete.as_view(), name='delete-student'),
            path("students/<int:pk>/",views.studentupdate.as_view(),name='student-update')
            ]