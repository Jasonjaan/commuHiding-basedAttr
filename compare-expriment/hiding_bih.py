import sys, getopt
import timeit
from datetime import datetime
import random

def main(argv):
    start_time = timeit.default_timer()
    start_time2 = datetime.now()
    # 步骤一：求某个社区中各个节点的重要度
    # 1.获取：community\network
    input_file_path = './data/community.dat'
    output_file_path = './data/subcommunity.dat'
    T_num=1000
    community = {}
    commDictKeyLen = {}
    commDictSortKey =[]
    my_num = 1
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # 逐行读取输入文件
        for line in input_file:
            for str1 in line.split():
                # 将符合条件的行写入输出文件
                my_str = str(my_num)
                output_file.write(my_str)  # 社区
                output_file.write(" ")
                output_file.write(line)  # 数据
                lindData = line.split()
                community[my_str] = lindData  # key->值
                l = len(line.split())
                commDictKeyLen[l] = []  # todo:初始化操作
                commDictKeyLen[l].append(my_str)  # key->长度
                commDictSortKey.append(l)
            my_num +=1
    input_file_path = './data/network.dat'
    output_file_path = './data/networkSub.dat'

    network = {}
    commDictKeyLen = {}
    commDictSortKey =[]
    my_num = 1
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # 逐行读取输入文件
        for line in input_file:
            for str1 in line.split():
                # 将符合条件的行写入输出文件
                my_str = str(my_num)
                output_file.write(my_str)  # 社区
                output_file.write(" ")
                output_file.write(line)  # 数据
                lindData = line.split()
                network[my_str] = lindData  # key->值
                l = len(line.split())
                commDictKeyLen[l] = []  # todo:初始化操作
                commDictKeyLen[l].append(my_str)  # key->长度
                commDictSortKey.append(l)
            my_num +=1
    # 2. ci
    #ci = ['815','639','877','489','632','758','767','880','914','864','770','980'] # 默认自定义，或者随机选一个从community
    ci = ['591', '812', '761', '197', '440', '8', '172', '749', '592', '932', '449', '842', '529', '729', '452', '796',
          '797', '738', '825', '745', '769', '890', '984', '1000', '819', '556', '448', '594', '50', '331', '422',
          '673', '978', '648']
    # 3. t
    t = ci
    # 4. v
    v = {}
    for _, value1 in enumerate(ci):
        v[value1] = []
        vv = []
        for value2 in network.values():
            if value1 in value2:
                vv.extend(value2)
        vv = list(dict.fromkeys(vv))
        for _,c in enumerate(ci):
            if c in vv:
                if c != value1:
                    v[value1].append(c)
        v[value1] = list(dict.fromkeys(v[value1]))
    # 5.tb, vb
    tb,vb = {},{}
    for _, value1 in enumerate(ci):
        tb[value1] = []
        vv = []
        for value2 in network.values():
            if value1 in value2:
                vv.extend(value2)
        vv = list(dict.fromkeys(vv))
        for _, c in enumerate(ci):
            if c in vv:
                if c != value1:
                    tb[value1].append(c)
        tb[value1] = list(dict.fromkeys(tb[value1]))
    for key, values in v.items():
        for _,vs in enumerate(values):
            kk = key+"-"+vs
            vb[kk] = []
            vv = []
            for value2 in network.values():
                if vs in value2:
                    vv.extend(value2)
            vv = list(dict.fromkeys(vv))
            for _, c in enumerate(ci):
                if c in vv:
                    if c != vs and c != key:
                        vb[kk].append(c)
            vb[kk] = list(dict.fromkeys(vb[kk]))
    # 6. delCount
    delCount = {}
    for _, c in enumerate(ci):
        delCount[c] = 0
        set1 = set(tb[c])
        set2 = set(ci)
        setResult = set1.intersection(set2)
        delCount[c] = len(setResult)-1
    # 7. tvc
    tvc1 = {}
    for key, values in vb.items():
        ss = key.split('-')
        t = ss[0]
        tbv = tb[t]
        set1 = set(values)
        set2 = set(tbv)
        setResult = set1.intersection(set2)
        tvc1[key] = (len(setResult))
    tvc = {}
    for _, c in enumerate(ci):
        tvc[c] = 0
        for key, values in tvc1.items():
            if c in key:
                tvc[c]+=values
    # 8. td
    td = {}
    for key, values in tb.items():
        td[key] = len(values)
    # 9. tinf
    tinf = {}
    for _, c in enumerate(ci):
        tinf[c] = 0
        ctvc = tvc[c]
        ctd =td[c]
        tinf[c] = ctvc*(ctd-1)/ctd
    # 步骤二：求某个社区中各个节点的重要度。
    # 1、选tt
    tt = ci[0] # 默认第一个
    del tinf[tt]
    delb = sorted(tinf, key=tinf.get,reverse=True)
    delK = []
    delV= {}
    for _, db in enumerate(delb):
        for k, v in network.items():
            if tt in v and db in v:
                delK.append(k)
                delV[k] = v
    for _,k in enumerate(delK):
        del network[k]
        network[k] = [delV[k][0]+'50',delV[k][1]+'50']
    end_time = timeit.default_timer()
    end_time2 = datetime.now()
    time = end_time2- start_time2
    execution_time = (end_time - start_time) * 1e6
    #print("代码执行耗时: ", execution_time, "微秒")
    print("BIH方法隐藏社区执行时间: ", time.microseconds, "微秒")
    return 0

if __name__ == '__main__':
    main(sys.argv[1:])