"""单页应用相关视图"""

from django.shortcuts import render
from django.http import JsonResponse


def single_page_index(request):
    """单页应用首页"""
    return render(request, 'singlepage/index.html')


def get_section_content(request, section_id):
    """获取指定部分的内容"""
    # 各部分内容
    section_contents = {
        '1': "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed lacinia quam. Sed vitae mattis metus, vel gravida ante.",
        '2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisl eget aliquam ultricies.",
        '3': "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae."
    }
    
    # 返回指定部分的内容，如果不存在则返回默认内容
    content = section_contents.get(section_id, "内容不存在")
    return JsonResponse({'content': content})