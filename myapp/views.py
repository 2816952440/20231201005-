from django.http import Http404, HttpResponse
from django.shortcuts import render

# 导入单页应用视图函数
from .views.singlepage_views import single_page_index, get_section_content

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

# 为保持向后兼容性，重新导出新的视图函数
single_page_index = single_page_index
get_section_content = get_section_content

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
