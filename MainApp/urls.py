
from django.contrib import admin
from django.urls import path, include
from microservice_lambda.views import *




urlpatterns = [

    path('admin/', admin.site.urls),

    # Microservice APIs
    path('products/', ProductViewAPI.as_view()),

    path('', APIListViewAPI, name='APIListViewAPI')

]
