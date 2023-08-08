"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django_distill import distill_path

from bootstrap3.views import index as bootstrap_3_preview
from bootstrap4.views import index as bootstrap_4_preview
from bulma.views import index as bulma_preview
from django_rendering.views import index as django_rendering_preview
from test_project.views import index

urlpatterns = [
    # index alias so that http://127.0.0.1:8000/ works
    path("", index),
    # use `crispy-test-project` prefix so the views work with github pages
    distill_path("crispy-test-project/", index, name="main-index", distill_file="index.html"),
    distill_path(
        "crispy-test-project/django",
        django_rendering_preview,
        name="django_rendering.views.index",
        distill_file="django.html",
    ),
    distill_path(
        "crispy-test-project/bootstrap3",
        bootstrap_3_preview,
        name="bootstrap3.views.index",
        distill_file="bootstrap3.html",
    ),
    distill_path(
        "crispy-test-project/bootstrap4",
        bootstrap_4_preview,
        name="bootstrap4.views.index",
        distill_file="bootstrap4.html",
    ),
    distill_path("crispy-test-project/bulma", bulma_preview, name="bulma.views.index", distill_file="bulma.html"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
