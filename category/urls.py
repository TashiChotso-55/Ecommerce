from django.urls import path
from category import views
app_name='category'

urlpatterns=[
 path('',views.getAllCat,name='category'),
 path('<slug:catname>',views.prodByCat,name='products_by_category'),
 ]
