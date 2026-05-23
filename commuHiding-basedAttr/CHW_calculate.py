import sys, getopt
import networkx as nx
import sys
from datetime import datetime
import time
from datetime import datetime
import random
import Treeconstruct

def main(argv):
    input_file_path = './date/community.dat'
    output_file_path = './date/chwcommunity.dat'
    target = 1000
    T_num = 749
    target_str = str(target)
    commDict = {}
    commDictKeyLen = {}
    commDictSortKey = []
    T_str = str(T_num)
    my_num = 1
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # 逐行读取输入文件

        for line in input_file:
            # 这里可以根据你的条件进行选择
            # 选择包含特定关键字的行
            for str1 in line.split():
                if T_str == str1:
                    # 将符合条件的行写入输出文件
                    my_str = str(my_num)
                    output_file.write(my_str)  # 社区
                    output_file.write(" ")
                    output_file.write(line)  # 数据
                    lindData = line.split()
                    commDict[my_str] = lindData  # key->值
                    l = len(line.split())
                    commDictKeyLen[l] = []  # todo:初始化操作
                    commDictKeyLen[l].append(my_str)  # key->长度
                    commDictSortKey.append(l)
            my_num += 1

    commSortDict = {}
    for sortKey in commDictSortKey:
        for skk in commDictKeyLen[sortKey]:
            commSortDict[skk] = commDict[skk]
    input_file_path1 = './date/network.dat'
    #目标节点所有边编号
    linkDict = {}
    #编号对应的属性
    linkattrDict = {}
    linkweightdict = {}
    #对所有边进行编号
    with open(input_file_path1, 'r') as input_file:
        count = 1
        for line in input_file:
            # 这里可以根据你的条件进行选择
            # 选择包含特定关键字的行
            for str2 in line.split():
                if T_str == str2:
                    linedate = line.split()
                    linkDict[count] = linedate
                    count +=1
    print("B类节点: ", T_num)
    print("节点边:", linkDict)
    print("节点边数量", count - 1)

    B_B = linkDict

    for k, v in linkDict.items():
        # 拿边中的另一个节点号查找
        for value in v:
            if value == T_str:
                continue
            else:
                for k1, v1 in commSortDict.items():
                    for vv1 in v1:
                        if value == vv1:
                            # kk1 = str(k1)
                            key_to_check = k
                            # linkattrDict[k].append(k1)
                            linkattrDict.setdefault(key_to_check, []).append(k1)
    print("构建所有链接的属性：", linkattrDict)

    for k, v in linkattrDict.items():
        key_to_check = k
        value_length = len(linkattrDict[key_to_check])
        random_numbers = generate_positive_random_numbers(value_length)
        for idx in random_numbers:
            linkweightdict.setdefault(key_to_check, []).append(idx)
    print("链接属性权值：", linkweightdict)
    L_Q = linkweightdict

    CHW_value = CHW(B_B, L_Q, target)
    print("节点受影响程度CHW：", CHW_value)

def generate_positive_random_numbers(n):
    # 生成n-1个大于0.1的随机数，并保留两位有效数字
    random_numbers = [round(random.uniform(0.2, 0.6), 2) for _ in range(n)]

    # # 为了确保总和为1，将最后一个随机数适当减小
    # last_random_number = round(random.uniform(0.1, sum(random_numbers)), 2)

    # 更新最后一个随机数，确保总和为1
    #random_numbers.append(last_random_number)

    return random_numbers

def CHW(BS, SQ, tt):
    crr = 0.0
    sum = 0.0
    id = 0
    T = str(tt)
    for index, value in BS.items():
        for v in value:
            if v == T :
                id = index
    for key in SQ:
        if key == id:
            crr_value = SQ[key][0]
            crr = float(crr_value)
        string_number = SQ[key][0]
        float_number = float(string_number)
        sum += float_number
    # for k,v in SQ.items():
    #     if id == k :
    #         crr = v
    #     float_number = float(v)
    #     sum += float_number
    chw = crr/sum
    return chw

if __name__ == '__main__':
    main(sys.argv[1:])
