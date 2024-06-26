from django.urls import path
from . import views

urlpatterns = [
    path("ratings/",views.ratingForm,name="ratings"),
    path('view/',views.viewRatings,name='view'),
    path('success/',views.success,name='success'),
    path('',views.loginPage,name='login'),
]
