from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view(
        {
            'get': 'list', # get method points to list func
            'post': 'create'
        }
    )),
    path('products/<str:pk>', ProductViewSet.as_view(
        {
            'get': 'retrieve', # get method points to list func
            'put': 'update',
            'delete':'destroy'
        }
    )),
    path('user', UserAPIView.as_view())
]
