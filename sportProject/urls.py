from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from sportApp                       import views
from sportApp                       import views as viewsProduct

urlpatterns = [
    path('login/',                       TokenObtainPairView.as_view()),
    path('refresh/',                     TokenRefreshView.as_view()),
    path('user/',                        views.UserCreateView.as_view()),
    path('user/<int:pk>/',               views.UserDetailView.as_view()),
    path('productos/',                   viewsProduct.product_api_view),
    path('busquedad_productos/<int:pk>', viewsProduct.product_detail_view),
    ]
    