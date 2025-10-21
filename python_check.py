# 简单的Python环境检测脚本
print("Python检测开始...")

# 检测基本的Python版本信息
import sys
print(f"Python版本: {sys.version}")
print(f"Python路径: {sys.executable}")
print(f"系统路径: {sys.path}")

# 检测基本功能
try:
    # 基本数学运算
    result = 1 + 1
    print(f"基本运算测试: 1+1 = {result}")
    
    # 列表操作
    test_list = [1, 2, 3]
    test_list.append(4)
    print(f"列表操作测试: {test_list}")
    
    # 字符串操作
    test_str = "Hello"
    test_str += " Python"
    print(f"字符串操作测试: {test_str}")
    
    print("Python基本功能正常!")
except Exception as e:
    print(f"Python基本功能测试失败: {e}")

print("Python检测完成。")