"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter

from crawler.views import CrawlerDataViewSet, CrawlerMapDataViewSet

router = DefaultRouter()

"""クローラーデータ一覧"""
router.register("dates", CrawlerDataViewSet, base_name="dates")
"""マップ表示データ用"""
router.register("mapdata", CrawlerMapDataViewSet, base_name="mapdata")

urlpatterns = [
    path('admin/', admin.site.urls),
    # drfのドキュメント
    url(r'docs/', include_docs_urls(title="ドキュメント")),
    path('', include(router.urls)),
]
