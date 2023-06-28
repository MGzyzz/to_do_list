"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from To_do_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.views_all, name='home'),
    path('task/add', views.new_task, name='task-add'),
    path('task/<int:id>/', views.task_detail_view, name='task-detail'),
    path('task/<int:id>/edit', views.task_edit, name='task-edit')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)