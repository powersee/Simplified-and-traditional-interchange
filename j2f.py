from langconv import *
import sys
import os

# print(sys.version)
# print(sys.version_info)

path ="文本所放的那个文件夹的绝对路径"

# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line

#保存转换完后的文件
def save2file(result):
    with open(path+"/"+file,'w') as d:
        #for en in result:
            d.write(result)
            d.close

if __name__ == '__main__':
    for file in os.listdir(path):
            with open(path+"/"+file,'r',encoding='utf-8',errors='ignore') as f:
                string = f.read()
                f.close()
                result = chs_to_cht(string)
                # 如果要繁转简，就把上面这一行的 chs_to_cht 改为 cht_to_chs
                save2file(result)
print("done")
