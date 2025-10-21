"""学生信息相关视图"""

from django.shortcuts import render


def student_info(request):
    """展示学生信息的视图"""
    # 学生信息数据
    context = {
        'name': '吴水保',
        'student_id': '20231201005'
    }
    return render(request, 'myapp/student_info.html', context)