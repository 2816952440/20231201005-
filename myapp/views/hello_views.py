"""Hello World相关视图"""

from django.http import HttpResponse


def hello_world(request):
    """展示Hello World消息的视图"""
    return HttpResponse("<h1>Hello World!</h1><p>这是一个简单的Hello World应用。</p>")