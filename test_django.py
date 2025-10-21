print("Django项目测试")
try:
    import django
    print(f"Django版本: {django.__version__}")
except ImportError:
    print("Django未安装")