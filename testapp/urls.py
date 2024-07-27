from django.urls import path
from testapp import views

#code here

urlpatterns = [
    path('hello',views.greeting),
    path('about',views.about),
    path('contact',views.contact),
    path('customtags',views.custom_tags),
    path('filter',views.custom_filter),
]
