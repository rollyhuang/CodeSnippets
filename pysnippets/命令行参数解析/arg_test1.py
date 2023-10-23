# 方法1：使用内置模块sys.argv
import sys
print("正在运行的脚本名称: '{}'".format(sys.argv[0])) # 列表中的第一个元素是脚本的完整路径(或脚本名称——取决于具体操作系统)
print("脚本的参数数量: '{}'".format(len(sys.argv))) # 返回命令行参数的个数
print("脚本的参数: '{}'".format(str(sys.argv))) # 返回包含所有命令行参数的列表(list)
