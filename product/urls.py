from django.urls import path
from product import views
app_name='product'

urlpatterns=[
 path('<slug:prodid>',views.product,name='product'),
 ]
