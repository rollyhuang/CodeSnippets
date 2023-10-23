# Exception处理：getopt.GetoptError
# 在参数列表中没有找到所传递参数，或选项的需要的参数为空时会触发该异常。
# 异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。
# 在 arg_test2.py 中添加异常处理，检查此错误信息：

import sys
import getopt

def main(argv):
    input_file = ""
    output_file = ""
    try:
        opts, args = getopt.getopt(argv[1:], "hi:o", ["help", "input_file=", "output_file="])
    except getopt.GetoptError as e:
        print(e.msg)
        print(e.opt)
        sys.exit(2)

# 使用错误的格式选项传递参数执行脚本：
# python scripy_1.py -f
# 输出以下错误信息：
# option -f not recognized
# f
