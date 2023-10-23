# argparse标准库
# 当程序中使用采用复杂参数或多个文件名时，推荐使用 Python 的 argparse 库，它以系统的方式处理命令行参数，从而可以编写用户友好的命令行程序
# Python 标准库 argparse 同样也是用于解析命令行参数的模块。
# 首先，由程序确定所需的参数，然后，argparse 将这些参数解析为 sys.argv。此外，argparse 会生成帮助和使用信息提示，并在提供无效参数时发出错误。

import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

# 不带参数运行此脚本不会向 stdout 显示任何内容。但是，如果使用 --help 或 -h 选项，将得到脚本的使用信息提示：
# usage: arg_test4.py [-h]
# optional arguments:
# -h, --help show this help message and exit
# 指定其他参数会导致错误，例如使用如下命令：
# arg_test4.py -i
# 则会报导致错误：
# usage: scripy_3.py [-h]
# argparse_minimal.py: error: unrecognized arguments: -i