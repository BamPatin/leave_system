from django.urls import path
from leave_app import views

urlpatterns = [
    path('', views.home),
    path('formleave',views.formleave),
    path('status',views.status),
    path('approve',views.approve),
    path('success',views.success),
    path('unsuccess',views.unsuccess),

]
