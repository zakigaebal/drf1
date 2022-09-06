from django.urls import path,include,re_path

app_name = 'mobile'
urlpatterns =[
    path('',include('rest_framework.urls',namespace='rest_framework_category')),
    ]
