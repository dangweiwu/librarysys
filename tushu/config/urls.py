"""tushu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
# from django.contrib import admin
from django.urls import path
# from django.http import HttpResponse
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from users.views import Work, UserViewSet, BorrowView, Circulate,phone
from books.views import BooksView
from news.views import NewsView

router = DefaultRouter()
# router.register(r'user', UserViewSet, base_name="user")


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title="图书馆", authentication_classes=[],
                                    permission_classes=[])),
    path('xadmin/', xadmin.site.urls),
    # rest登陆
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    # drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    path('login/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),

    path('work/', Work.as_view()),
    path('user/', UserViewSet.as_view()),
    path('book/', BooksView.as_view()),
    path('borrow/', BorrowView.as_view()),
    path('circulate/', Circulate.as_view()),
    path('news/', NewsView.as_view()),
    path('phone/',phone),


]
