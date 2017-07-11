"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/users/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
    3. Add as parameters an object of type dict representing the method type
        with it's key e.g. get or post, and the name of the action with
        it's value
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework import routers

from .views import AccountViewSet

router = routers.SimpleRouter()
router.register(prefix=r'^accounts', viewset=AccountViewSet)
urlpatterns = router.urls
