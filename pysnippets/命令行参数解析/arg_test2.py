# 方法2：使用getopt模块
# getopt模块是专门处理命令行参数的模块，用于获取 命令行选项 和 参数。支持短选项模式(-)和长选项模式(--)。
# 该模块提供了两个方法及一个异常处理来解析命令行参数。
# getopt.getopt 方法
# getopt.getopt 方法用于解析命令行参数列表，其语法格式如下：getopt.getopt(args, options[, long_options])
#   args: 要解析的命令行参数列表，一般是sys.argv[1:]，需要过滤掉脚本名(sys.argv[0])
#   options: 以字符串的格式定义，options 后的冒号 “:” 表示如果设置该选项，必须有附加的参数，否则就不附加参数
#   long_options: 以列表的格式定义，long_options 后的等号 “=” 表示该选项必须有附加的参数，不带冒号表示该选项不附加参数
#   返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有 - 或 – 的参数
import sys
import getopt


def main(argv):
    input_file = ""
    output_file = ""
    # "hi:o:": 短格式分析串, h 后面没有冒号, 表示后面不带参数; i 和 o 后面带有冒号, 表示后面带参数
    # ["help", "input_file=", "output_file="]: 长格式分析串列表, help后面没有等号, 表示后面不带参数; input_file和output_file后面带冒号, 表示后面带参数
    # 返回值包括 `opts` 和 `args`, opts 是以元组为元素的列表, 每个元组的形式为: (选项, 附加参数)，如: ('-i', 'test.png');
    # args是个列表，其中的元素是那些不含'-'或'--'的参数
    opts, args = getopt.getopt(argv[1:], "hi:o:", ["help", "input_file=", "output_file="])

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('arg_test2.py -i <input_file> -o <output_file>')
            print('or: arg_test2.py --input_file=<input_file> --output_file=<output_file>')
            sys.exit()
        elif opt in ("-i", "--input_file"):
            input_file = arg
        elif opt in ("-o", "--output_file"):
            output_file = arg
    print('输入文件为：', input_file)
    print('输出文件为：', output_file)

    # 打印不含'-'或'--'的参数
    for i in range(0, len(args)):
        print('不含'-'或'--'的参数 %s 为：%s' % (i + 1, args[i]))
        
if __name__ == "__main__":
    main(sys.argv)

# 使用带有命令行选项的命令执行此脚本，以下两种方式是等价的：
# # 方式1
# python arg_test2.py -i test.png -o output.png OpenCV
# # 方式2
# python arg_test2.py --input_file test.png --output_file output.png OpenCV
# 输入文件为： test.png
# 输出文件为： output.png
# 不含'-'或'--'的参数 1 为：OpenCV
