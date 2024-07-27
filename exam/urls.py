from django.urls import path
from exam import views
#code here

urlpatterns = [
    path('testpaper',views.testpaper),
    path('result',views.result),
    path('template_tags',views.template_tags),
]

