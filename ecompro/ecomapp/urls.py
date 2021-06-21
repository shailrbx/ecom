from django.urls import path
from . import  views
app_name='ecomapp'
urlpatterns = [
    path('',views.AllprodCat,name='AllprodCat'),
    path('<slug:c_slug>/',views.AllprodCat,name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name="proDetail"),

    ]