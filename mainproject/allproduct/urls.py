from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'laptop',Laptopview)
router.register(r'tag',Tagview),
router.register(r'review',Reviewview)
router.register(r'product',ProductView,basename = 'product')
# router.register(r'product/<id>/',ProductDetailApi)
urlpatterns=[
    path('',include(router.urls)),
    path('productfrontend/',productfrontend , name='productfrontend'),
    path('productdetailfrontend/<int:product_id>/', productdetailfrontend, name='productdetailfrontend')  # Updated parameter name
]