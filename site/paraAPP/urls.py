from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("about_us", views.about_us),
    path("press", views.press),
    path("testemonies", views.testemonies),
    path("download", views.download),
    path("faq", views.faq),
    path("contact", views.contact),
]