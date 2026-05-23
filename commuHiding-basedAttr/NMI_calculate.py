import sys, getopt
import sys
import networkx as nx
import math
def main():
    # 这里写主函数的逻辑
    commu1 = {}
    commu2 = {}
    input_file_path = './date/club.txt'
    count = 1
    set1 = set()
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            commu1[count] = []
            commu2[count] = []
            for str1 in line.split(','):
                str_temp = str1.strip()
                number = int(str_temp)
                commu1[count].append(number)
                commu2[count].append(number)
                set1.add(number)
            count += 1
    target_key = 2
    #
    # element_to_remove1 = 107
    element_to_remove2 = 33

    if target_key in commu2 and element_to_remove2 in commu2[target_key]:
        commu2[target_key].remove(element_to_remove2)
    # if target_key in commu2 and element_to_remove2 in commu2[target_key]:
    #     commu2[target_key].remove(element_to_remove2)
    #print(commu1)
    len1 = len(commu1)
    #print(commu2)
    len2 = len(commu2)
    #print(set1)
    set_len = len(set1)
    # print(len1,len2,set_len)
    #计算nmi值
    i1 = 1
    N = set_len
    fz = 0.0
    while i1 <= len1 :
        j1 = 1
        tt = 0
        while j1 <= len2 :
            N_ij = 0
            N_i = 0
            N_j = 0
            values1 = commu1.get(i1)
            values2 = commu2.get(j1)
            for value1 in values1:
                for value2 in values2:
                    if value2 == value1 :
                        N_ij += 1
            # print(N_ij)
            # return
            vv1 = commu1.get(i1)
            if vv1 is not None and isinstance(vv1,(list,tuple)):
                N_i = len(vv1)
            vv2 = commu2.get(j1)
            if vv2 is not None and isinstance(vv2, (list, tuple)):
                N_j = len(vv2)
            sum = (N_ij * N)/(N_i * N_j)
            if N_ij != 0 :
                tt = N_ij * math.log10(sum)
                fz += tt
            j1 += 1

        i1 += 1
    #print(fz)
    #
    sm = -2 * fz
    #

    qm = 0.0
    hm = 0.0
    i2 = 1
    while i2 <= len1:
        N_i2 = 0
        vv2 = commu1.get(i2)
        if vv2 is not None and isinstance(vv2, (list, tuple)):
            N_i2 = len(vv2)
        sum1 = N_i2/N
        t_t1 = math.log10(sum1)
        qm += (N_i2 * t_t1)
        i2 += 1
    j2 = 1
    while j2 <= len2 :
        N_j2 =0
        vv3 = commu2.get(j2)
        if vv3 is not None and isinstance(vv3, (list, tuple)):
            N_j2 = len(vv3)
        sum2 = N_j2 / N
        t_t2 = math.log10(sum2)
        hm += (N_j2 * t_t2)
        j2 += 1
    # print(qm,hm)
    fm = qm + hm
    nmi = sm/fm
    print("数据集：club",)
    print("检测算法：CMP",)
    print("NMI值为：",nmi)





# 判断是否执行主函数
if __name__ == "__main__":
    main()