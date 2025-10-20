"""myapp URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_info, name='student_info'),  # 根路径访问学生信息页面
]