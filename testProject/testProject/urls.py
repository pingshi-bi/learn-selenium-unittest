"""testProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views import static
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import testAction

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', testAction.login),
    path('dologin/', testAction.dologin),
    path('logout/', testAction.logout),
    path('addUser/', testAction.addUser),
    path('rand_code/', testAction.auth_code_port),
    path('mainpage/', testAction.homepage),
    path('create_order/', testAction.orderAdd),
    path('commit_order/', testAction.orderAddCommit),
    path('commit_order1/', testAction.orderAddCommit1),
    path('list_order/', testAction.orderList),
    path('info_order/', testAction.orderInfo),
    path('orderQueryApi/', testAction.orderQueryApi),
    path('fileUpload/', testAction.upload),
]
