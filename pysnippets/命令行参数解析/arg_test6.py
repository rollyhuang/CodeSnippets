# 默认情况下，argparse 将提供的选项视为字符串
# 因此，如果参数不是字符串，则应使用 type 选项。使用 script_5.py 脚本，其中添加了两个参数，这两个参数是 int 类型：
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("first_number", help="first number to be added", type=int)
parser.add_argument("second_number", help="second number to be added", type=int)
args = parser.parse_args()
print("args: '{}'".format(args))
print("the sum is: '{}'".format(args.first_number + args.second_number))
args_dict = vars(parser.parse_args())
print("args_dict dictionary: '{}'".format(args_dict))
print("first argument from the dictionary: '{}'".format(args_dict["first_number"]))

# 在前面的示例中，通过调用 vars() 函数将参数存储在字典中：
# args_dict = vars(parser.parse_args())
# print("args_dict dictionary: '{}'".format(args_dict))
# print("first argument from the dictionary: '{}'".format(args_dict["first_number"]))
# 如果不带参数执行脚本：python arg_test6.py
# 则输出如下：
# usage: arg_test6.py [-h] first_number second_number
# arg_test6.py: error: the following arguments are required: first_number, second_number
# 如果我们使用 -h 选项执行脚本：python arg_test6.py --help
# 输出将如下所示：
# usage: arg_test6.py [-h] first_number second_number

# positional arguments:
#   first_number   first number to be added
#   second_number  second number to be added

# optional arguments:
#   -h, --help     show this help message and exit
# 如果此脚本以如下方式执行：python arg_test6.py 123 456
# 则输出如下：
# args: 'Namespace(first_number=123, second_number=456)'
# the sum is: '579'
# args_dict dictionary: '{'first_number': 123, 'second_number': 456}'
# first argument from the dictionary: '123'
