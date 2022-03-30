"""
 * Project name(项目名称)：Python_fileinput模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 19:58
 * Version(版本): 1.0
 * Description(描述)：
 fileinput 模块中 input() 该函数的语法格式如下：
fileinput.input（files="filename1, filename2, ...", inplace=False, backup='', bufsize=0, mode='r', openhook=None）
此函数会返回一个 FileInput 对象，它可以理解为是将多个指定文件合并之后的文件对象。其中，各个参数的含义如下：
files：多个文件的路径列表；
inplace：用于指定是否将标准输出的结果写回到文件，此参数默认值为 False；
backup：用于指定备份文件的扩展名；
bufsize：指定缓冲区的大小，默认为 0；
mode：打开文件的格式，默认为 r（只读格式）；
openhook：控制文件的打开方式，例如编码格式等。

函数名	功能描述
fileinput.filename()	返回当前正在读取的文件名称。
fileinput.fileno()	返回当前正在读取文件的文件描述符。
fileinput.lineno()	返回当前读取了多少行。
fileinput.filelineno()	返回当前正在读取的内容位于当前文件中的行号。
fileinput.isfirstline()	判断当前读取的内容在当前文件中是否位于第 1 行。
fileinput.nextfile()	关闭当前正在读取的文件，并开始读取下一个文件。
fileinput.close()	关闭 FileInput 对象。
 """
import fileinput

if __name__ == '__main__':
    list1 = []
    for i in range(1, 41):
        filename = "file" + str(i) + ".txt"
        list1.append(filename)
    print(list1)
    fileout = open("out.txt", "w", encoding="utf-8")
    for fileline in fileinput.input(files=list1):
        print(fileline, end="")
        # 返回当前正在读取的文件的名称。在读取第一行之前，返回 None。
        print(fileinput.filename())
        # 返回当前文件的文件号。当前没有打开文件时，返回 -1。
        print(fileinput.fileno())
        # 返回刚刚读取的行的累积行号。在读取第一行之前，返回 0。在读取最后一个文件的最后一行之后，返回该行的行号。
        print(fileinput.lineno())
        # 返回当前文件中的行号。在读取第一行之前，返回 0。在读取最后一个文件的最后一行之后，返回文件中该行的行号。
        print(fileinput.filelineno())
        # 返回 true 刚刚读取的行是其文件的第一行，否则返回 false。
        print(fileinput.isfirstline())
        # 关闭当前文件，以便下一次迭代将读取下一个文件的第一行（如果有）；
        # 未从文件中读取的行将不计入累积行数。在读取下一个文件的第一行之前，文件名不会更改。
        # 在读取第一行之前，此功能无效；它不能用于跳过第一个文件。读取最后一个文件的最后一行后，此函数无效。
        # fileinput.nextfile()
        # 关闭序列。
        # fileinput.close()
        fileout.write(fileline)
    fileout.close()
