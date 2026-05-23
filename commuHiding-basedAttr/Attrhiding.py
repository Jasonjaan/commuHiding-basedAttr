import sys, getopt
import networkx as nx
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
    # def __str__(self):
    #     return f"TreeNode(value={self.value})"


def main(argv):

    input_file_path = './date/community.dat'
    output_file_path = './date/subcommunity.dat'
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
    # commTList = commKeyTList
    # commAttr = str(commTList[random.randint(0, len(commTList)-1)])
    commAttr = '169'
    #delT = '11'
    delTChild = commKeyChild[commAttr]
    print("delTChild:",delTChild)
    print("*T值:",T_num)
    print("*T社区情况:",commSortDict)
    print("*树关系:",commKeyChild)
    S_G = commKeyChild
    print("*T属性集:",commKeyTList)
    print("*削弱节点T属性:",commAttr)
    TT = commAttr
    commKeyTList.remove(commAttr)
    for c in delTChild:
        commKeyTList.remove(c)
    print("*T属性集(削弱后):",commKeyTList)
    end_time1 = datetime.now()
    timedif = end_time1 - start_time1
    len_of_target_community = len(S_G[TT])

    # 链接属性
    start_time2 = datetime.now()
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
    print("目标节点所有边编号:",linkDict)
    B_B = linkDict
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
    B_S = linkattrDict
    #属性权重/随机属性权重设置
    for k,v in linkattrDict.items():
        key_to_check = k
        value_length = len(linkattrDict[key_to_check])
        random_numbers = generate_positive_random_numbers(value_length)
        for idx in random_numbers:
            linkweightdict.setdefault(key_to_check, []).append(idx)
    print("链接属性权值：",linkweightdict)
    S_Q = linkweightdict
    print("*削弱节点T属性:", commAttr)
    #print("*削弱T特定属性:", commAttr)
    print("削弱链接属性后的所有链接的属性：", linkattrDict)
    end_time2 = datetime.now()
    dif_time2 = end_time2 - start_time2
    hide_time = end_time2 - start_time1
    print(f"链接属性削弱时间：{dif_time2.microseconds}微秒")
    print(f"目标用户隐藏总时间：{hide_time.microseconds}微秒")

    # 遗传算法
    #bestRst = genetic_algorithm(TT, B_B, B_S, S_Q, S_G)
    bestRst = {}
    enhance = {}
    # 遗传算法迭代次数
    Tcount=10
    Tindex=0
    maxvalue = 0.0
    while Tindex < Tcount:
        idxRst,enhance = genetic_algorithm(TT, B_B, B_S, S_Q, S_G)
        weiRst = rst_weighall(B_S, S_Q, idxRst)
        if weiRst > maxvalue:
            maxvalue = weiRst
            bestRst.clear()
            bestRst = idxRst
        Tindex += 1
    print("最佳染色体：", bestRst)
    print("最佳染色体增强属性：",enhance)

    #隐藏效果
    rstqz = {}
    hidattqz = 0.0
    allattqz = 0.0
    for key in bestRst:
        rstal = bestRst[key]
        #rstqz[key] = 0
        sum = 0
        for rstV in rstal:#表示边的编号
            target_key = rstV
            values_list = B_S.get(target_key, [])
            target_value = key
            if target_value in values_list:
                index = values_list.index(target_value)
                value = S_Q.get(target_key, [])
                # 如果是可迭代的，检查索引是否在范围内
                if 0 <= index < len(value):
                    # 获取第i个元素
                    result = value[index]
                    hidattqz += result
        # rstqz[key].append(sum)
    # for key in bestRst:
    #     rstList = bestRst[key]
    #     rstqz[key] = []
    #     for index, value in enumerate(rstList):
    #         sumQZ = 0
    #         for v in value:
    #             bsV = B_S[v]
    #             ttIndex = bsV.index(TT)
    #             sqV = S_Q[v]
    #             vQZ = sqV[ttIndex]
    #             sumQZ += vQZ
    #         rstqz[key].append(sumQZ)
    # for ke in rstqz:
    #     string_number = rstqz[ke][0]
    #     float_number = float(string_number)
    #     hidattqz += float_number
    for kk2 in bestRst:
        vv = kk2
        for x1 in B_S:
            kkk = x1
            # va_arr = B_S[x1]
            values1_list = B_S.get(kkk, [])
            if vv in values1_list:
                posit = values1_list.index(vv)
                value2_list = S_Q.get(kkk,[])
                if 0 <= posit < len(value2_list):
                    # 获取第i个元素
                    result = value2_list[posit]
                    allattqz += result
    print("hidattqz",hidattqz)
    print("allattqz", allattqz)
    # effect = hidattqz/allattqz
    # 削弱
    print("B_S削弱前：",B_S)
    for key in  bestRst:
        rst = bestRst[key]
        for r in rst:
            B_S[r].remove(key)
    print("B_S削弱后：",B_S)

    print("*削弱节点T属性:", commAttr)
    # print("*削弱T特定属性:", commAttr)
    print("削弱链接属性后的所有链接的属性：", linkattrDict)
    end_time2 = datetime.now()
    dif_time2 = end_time2 - start_time2
    hide_time = end_time2 - start_time1

    print("目标社区存在子社区数量",len_of_target_community)
    print(f"节点属性削弱时间：{timedif.microseconds}微秒")
    print("遗传算法迭代次数:", Tcount)
    print(f"链接属性削弱时间：{dif_time2.microseconds}微秒")
    print(f"目标用户隐藏总时间：{hide_time.microseconds}微秒")

    # print("隐藏效果:",effect)

def generate_positive_random_numbers(n):
    # 生成n-1个大于0.1的随机数，并保留两位有效数字
    random_numbers = [round(random.uniform(0.2, 0.6), 2) for _ in range(n)]

    # # 为了确保总和为1，将最后一个随机数适当减小
    # last_random_number = round(random.uniform(0.1, sum(random_numbers)), 2)

    # 更新最后一个随机数，确保总和为1
    #random_numbers.append(last_random_number)

    return random_numbers

def genetic_algorithm(TT,B_B,B_S,S_Q,S_G):
    print("TT:",TT)
    print("B_B：目标节点所有边编号:",B_B)
    print("B_S：构建所有链接的属性:",B_S)
    print("S_Q：链接属性权值:",S_Q)
    print("S_G：树关系:",S_G)

    # 分析TT里有几个子社区和其他社区（S_G=>target,not_target）
    target = S_G[TT]
    target.append(TT)
    not_target = []
    for key in S_G:
        sgV = S_G[key]
        for v in sgV:
            if v in target:
                continue
            if v in not_target:
                continue
            not_target.append(v)

    print("target：目标子社区:",target)
    print("not_target：非目标子社区:",not_target)

    # 建立种群（B_S,target,not_target => target_dna,not_target_dna）
    target_dna = {}
    not_target_dna = {}
    for key in B_S:
        bsV = B_S[key]
        for tv in target:
            tv = str(tv)
            if tv in bsV:
                if tv not in target_dna:
                    target_dna[tv] = []
                if key not in target_dna[tv]:
                    target_dna[tv].append(key)
        for tv in not_target:
            tv = str(tv)
            if tv in bsV:
                if tv not in not_target_dna:
                    not_target_dna[tv] = []
                if key not in not_target_dna[tv]:
                    not_target_dna[tv].append(key)
    print("target_dna：目标DNA:", target_dna)
    print("not_target_dna：非目标DNA:", not_target_dna)

    # 建立染色体（target_dna,not_target_dna => target_rst,not_target_rst）
    targetRandLen,notTargetRandLen = 0.5,0.2 # 初始化随机染色体长度概率！！！
    rstCount = 50 # 初始化染色体条数！！！
    print("染色体数量：", rstCount)
    target_rst,not_target_rst={},{}
    for t in target_dna:
        target_rst[t] = []
    for t in not_target_dna:
        not_target_rst[t] = []
    for key in target_dna:
        counter = 1
        keyDna = target_dna[key]
        realRstLen = int(len(keyDna)*targetRandLen)
        while counter < rstCount:
            arr = random.sample(keyDna, realRstLen)
            target_rst[key].append(arr)
            counter += 1
    for key in not_target_dna:
        counter = 1
        keyDna = not_target_dna[key]
        realRstLen = int(len(keyDna)*notTargetRandLen)
        while counter < rstCount:
            arr = random.sample(keyDna, realRstLen)
            not_target_rst[key].append(arr)
            counter += 1
    print("target_rst：目标染色体:", target_rst)
    print("not_target_rst：非目标染色体:", not_target_rst)

    # 染色体交叉变异（target_rst => target_rst)
    randChangeRstCount,randChangeRstDataCount = 2,2 # 初始化需要随机交叉的染色体数量数和交换值数量！！！
    for key in target_rst:
        rst = target_rst[key]
        if len(rst) < 2: # randChangeRstCount < 2 不做操作
            continue
        randIndex = random.sample(range(0, randChangeRstCount),randChangeRstCount) # 需要变异的染色体、染色体需要交换值的位置
        needBreak = 0
        for index in randIndex:
            if len(rst[index]) < 2: #  randChangeRstDataCount < 2不做操作
                needBreak = 1
                break
        if needBreak == 1:
            break
        print("染色体变异前：",rst)
        for i1 in  randIndex:
            for i2 in randIndex:
                rstI1 = rst[i2][i1]
                rstI2 = rst[i1][i1]
                if rstI1 in rst[i1]:
                    continue
                if rstI2 in rst[i2]:
                    continue
                rst[i1][i1],rst[i2][i1] = rstI1,rstI2
        print("染色体变异后：",rst)
        target_rst[key] = rst

    # 拿染色体适应度 （SQ,BS,target_rst,target_dns => target_qz,target_dna_qz）
    target_rst_qz,target_dna_qz={},{}
    for key in target_rst:
        rstList = target_rst[key]
        target_rst_qz[key] = []
        for index, value in enumerate(rstList):
            sumQZ = 0
            for v in value:
                bsV = B_S[v]
                ttIndex = bsV.index(TT)
                sqV= S_Q[v]
                vQZ = sqV[ttIndex]
                sumQZ += vQZ
            target_rst_qz[key].append(sumQZ)
    print("target_rst_qz：目标染色体权值:", target_rst_qz)
    # 取最优染色体（target_rst,target_rst_qz => target_best_rst）
    target_best_rst = {}
    for key in  target_rst_qz:
        rstQzV = target_rst_qz[key]
        rst = target_rst[key]
        sortRstQzV = sorted(rstQzV)
        maxRstQZIndex = rstQzV.index(sortRstQzV[len(sortRstQzV)-1])
        bestTargetRst = target_rst[key][maxRstQZIndex]
        target_best_rst[key] = bestTargetRst
    print("target_best_rst：最优染色体:", target_best_rst)
    return target_best_rst,not_target_rst


def rst_weighall(BS, SQ, Rst):
    rst_qz = {}
    tmepRst = Rst
    for key in tmepRst:
        rstal = tmepRst[key]
        rst_qz[key] = []
        sum = 0
        for rstV in rstal:
            target_key = rstV
            values_list = BS.get(target_key, [])
            target_value = key
            if target_value in values_list:
                index = values_list.index(target_value)
                # index_to_find = 1
                value = SQ.get(target_key, [])
                if isinstance(value, (list, tuple)):
                    # 如果是可迭代的，检查索引是否在范围内
                    if 0 <= index < len(value):
                        # 获取第i个元素
                        result = value[index]
                        sum += result
        rst_qz[key].append(sum)
    # print(rst_qz)
    sumQZ = 0.0
    for key in rst_qz:
        string_number = rst_qz[key][0]
        float_number = float(string_number)
        sumQZ += float_number
    # print(sumQZ)
    return sumQZ

if __name__ == '__main__':
    main(sys.argv[1:])
