from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from posts.views import PostListView, PostModelViewSet, calculator, CalculatorAPIView

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('posts/', PostListView.as_view(), ),

    #path('calculator/', calculator, name = 'calculator-fbv'),
    path('calculator/', CalculatorAPIView.as_view(), name = 'calculator-cbv'),
]
 