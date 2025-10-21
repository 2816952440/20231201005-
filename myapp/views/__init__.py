"""视图模块包初始化文件"""

from .student_views import student_info
from .hello_views import hello_world
from .singlepage_views import single_page_index, get_section_content

__all__ = ['student_info', 'hello_world', 'single_page_index', 'get_section_content']