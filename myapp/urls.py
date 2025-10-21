"""myapp URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section"),
    # 单页应用相关路由
    path("singlepage/", views.single_page_index, name="single_page_index"),
    path("sections/<str:section_id>/", views.get_section_content, name="get_section_content")
]