# 由于未定义参数，因此不允许其他参数，接下来就添加一个参数：
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("first_argument", help="this is the string text in connection with first_argument")
args = parser.parse_args()
print(args.first_argument)
# add_argument() 方法用于指定程序将接受哪些命令行选项，此处添加了 first_argument 参数
# argparse 模块存储所有参数，将其名称与每个添加参数的名称相匹配——在此处为 first_argument 。为了获得参数值，需要使用 args.first_argument。
# 如果此脚本以下示方法执行，则输出为 10：
# python arg_test5.py 10
# 如果脚本在没有参数的情况下执行，则将输出以下信息：
# usage: arg_test5.py [-h] first_argument
# arg_test5.py: error: the following arguments are required: first_argument
# 如果使用 -h 选项执行脚本，输出将如下所示：
# usage: arg_test5.py [-h] first_argument

# positional arguments:
#   first_argument  this is the string text in connection with first_argument

# optional arguments:
#   -h, --help      show this help message and exit