"""inteliruta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from rides import views as rides_views
from rest_framework import routers

router = routers.DefaultRouter()

router.register("my-vehicles", rides_views.MyVehiclesViewSet)
router.register("my-offers", rides_views.MyOffersViewSet)
router.register("offers", rides_views.OffersViewSet)
router.register("my-demands", rides_views.MyDemandsViewSet)
router.register("demands", rides_views.DemandsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^mobile/accounts/signup-facebook', accounts_views.SignUpFacebookMobile.as_view()),
    url(r'^', include(router.urls)),

]
