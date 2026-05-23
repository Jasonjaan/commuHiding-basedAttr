import sys, getopt
import networkx as nx
import lpanni
import generator
import sys
from datetime import datetime
import time
from datetime import datetime
import random
import Treeconstruct

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    def __str__(self):
        return f"TreeNode(value={self.value})"

# 步骤一：执行main.py拿到community1.dat(network.dat)
# 步骤二：拿目标社区

def generate_positive_random_numbers(n):
    # 生成n-1个大于0.1的随机数，并保留两位有效数字
    random_numbers = [round(random.uniform(0.2, 0.6), 2) for _ in range(n)]

    # # 为了确保总和为1，将最后一个随机数适当减小
    # last_random_number = round(random.uniform(0.1, sum(random_numbers)), 2)

    # 更新最后一个随机数，确保总和为1
    #random_numbers.append(last_random_number)

    return random_numbers

def main(argv):

    input_file_path = './output/community1.dat'
    output_file_path = 'subdate/subcommunity.txt'
    T_num=1000
    start_time1 = datetime.now()
    my_num = 1
    # 社区->数据，映射字典
    commDict = {}
    commDictKeyLen = {}
    commDictSortKey =[]
    T_str = str(T_num)
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # 逐行读取输入文件

        for line in input_file:
            # 这里可以根据你的条件进行选择
            # 选择包含特定关键字的行
            for str1 in line.split():
                if T_str==str1:
                    # 将符合条件的行写入输出文件
                    my_str = str(my_num)
                    output_file.write(my_str) # 社区
                    output_file.write(" ")
                    output_file.write(line) # 数据
                    lindData = line.split()
                    commDict[my_str] = lindData# key->值
                    l = len(line.split())
                    commDictKeyLen[l] = [] # todo:初始化操作
                    commDictKeyLen[l].append(my_str) # key->长度
                    commDictSortKey.append(l)
            my_num +=1
    print("commDict:",commDict)
    print("commDictKeyLen:",commDictKeyLen)
    print("commDictSortKey:",commDictSortKey)
    commDictSortKey.sort()
    commDictSortKey.reverse()
    #T社区情况
    commSortDict = {}
    for sortKey in commDictSortKey:
        for skk in commDictKeyLen[sortKey]:
            commSortDict[skk] = commDict[skk]
    #end_time1 = datetime.now()
    #timedif=end_time1 - start_time1
    print(f"从总社区中{input_file_path} 中选择目标节点的所有社区并写入 {output_file_path} 完成。")
    #print(f"取目标节点子社区时间为：{timedif.microseconds}微秒")
    print("所有社区总数：",my_num)
    # 构造树逻辑
    #     情况1：假如94中的全部成员是93中的子集，那么94作为93的孩子节点
    #     情况2：假如不是，则兄弟
    # 兄弟关系表
    root = TreeNode(T_num)
    print("root:",root.value)
    # print("root:",root.children)
    childDict = {} # k-父亲，v-孩子
    childYes = {} # k-社区，v-yes
    commKeyChild = {}
    commTList = []
    #T属性集
    commKeyTList = []
    # AttTWeight = []
    commKeyChild[T_num] = []
    for k in commSortDict:
        childYes[k] = "no"
        childDict[k] = ""
        commKeyChild[k] = []
        commKeyTList.append(k)
    for k,v in commSortDict.items():
        # 判断k是否是别人的孩子
        # 是：不构建为根节点的孩子
        # 否：构建为根节点的孩子
        isYes = childYes[k]
        if isYes != "yes":
            commKeyChild[T_num].append(k)
        print("todo:构建为根节点的孩子")
        for k2, v2 in commSortDict.items():
            if k == k2:
                continue
            # 判断k是否是k2的孩子
            # 是：continue
            if childDict[k2] == k:
                continue
            # 否：判断k2是否是k的孩子
            set1 = set(v)
            set2 = set(v2)
            is_subset = set2.issubset(set1)
            # 是：构建k的孩子
            if is_subset:
                childDict[k] == k2
                childYes[k2] = "yes"
                commKeyChild[k].append(k2)
                print("todo:构建为",k2,"为",k,"的孩子流程")
    # 最终结果
    #           1000
    #       11         167
    #   166
    #需要隐藏的社区为：
    commTList = commKeyTList
    commAttr = str(commTList[random.randint(0, len(commTList)-1)])
    #delT = '11'
    delTChild = commKeyChild[commAttr]
    print("delTChild:",delTChild)
    print("*T值:",T_num)
    print("*T社区情况:",commSortDict)
    print("*树关系:",commKeyChild)
    print("*T属性集:",commKeyTList)
    print("*随机削弱T属性:",commAttr)
    commKeyTList.remove(commAttr)
    for c in delTChild:
        commKeyTList.remove(c)
    print("*T属性集(削弱后):",commKeyTList)
    end_time1 = datetime.now()
    timedif = end_time1 - start_time1
    print(f"节点属性削弱时间：{timedif.microseconds}微秒")

    # 链接属性削弱
    start_time2 = datetime.now()
    input_file_path1 = './input/network.dat'
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
    print("目标节点所有边编号:",linkDict)
    #所有编号边进行构造属性集
    # input_file_path2 = './subdate/subcommunity.txt'
    # with open(input_file_path2, 'r') as input_file:
    for k, v in linkDict.items():
        #拿边中的另一个节点号查找
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
    print("构建所有链接的属性：",linkattrDict)
    #属性权重/随机属性权重设置
    for k,v in linkattrDict.items():
        key_to_check = k
        value_length = len(linkattrDict[key_to_check])
        random_numbers = generate_positive_random_numbers(value_length)
        for idx in random_numbers:
            linkweightdict.setdefault(key_to_check, []).append(idx)
    print("链接属性权值：",linkweightdict)

    #跑遗传算法，选择削弱所有百分之80的属性权重但是削弱属性条数最少

    #
    # hindE = str(commTList[random.randint(0, len(commTList) - 1)])
    # delT = '11'
    hindEChild = commKeyChild[commAttr]
    for link,attr in linkattrDict.items():

        key_to_modify = link
        value_to_remove = commAttr
        # 检查键是否存在，并且值是否在列表中
        if key_to_modify in linkattrDict and value_to_remove in linkattrDict[key_to_modify]:
            # 削弱特定值
            linkattrDict[key_to_modify].remove(value_to_remove)
        #     print(f"值 {value_to_remove} 已从键 {key_to_modify} 中削弱")
        # else:
        #     print(f"键 {key_to_modify} 或值 {value_to_remove} 不存在")
        for c in delTChild:
            key_to_modify = link
            value_to_remove = c
            # 检查键是否存在，并且值是否在列表中
            if key_to_modify in linkattrDict and value_to_remove in linkattrDict[key_to_modify]:
                # 删除特定值
                linkattrDict[key_to_modify].remove(value_to_remove)
            #     print(f"值 {value_to_remove} 已从键 {key_to_modify} 中削弱")
            # else:
            #     print(f"键 {key_to_modify} 或值 {value_to_remove} 不存在")

    print("*随机削弱T某个属性:", commAttr)
    #print("*削弱T特定属性:", commAttr)
    print("削弱链接属性后的所有链接的属性：", linkattrDict)
    end_time2 = datetime.now()
    dif_time2 = end_time2 - start_time2
    hide_time = end_time2 - start_time1
    print(f"链接属性削弱时间：{dif_time2.microseconds}微秒")
    print(f"目标用户隐藏总时间：{hide_time.microseconds}微秒")

if __name__ == '__main__':
    main(sys.argv[1:])