import sys, getopt
import timeit
from datetime import datetime
import random

def main(argv):
    start_time = timeit.default_timer()
    start_time2 = datetime.now()
    # 步骤一：求某个社区中各个节点的重要度
    # 1.获取：community\network
    input_file_path = './data/club.dat'
    output_file_path = './data/subcommunity.dat'
    T_num=346
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
    input_file_path = './data/club.dat'
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
    # ci = ['591', '812', '761', '197', '440', '8', '172', '749', '592', '932', '449', '842', '529', '729', '452', '796',
    #       '797', '738', '825', '745', '769', '890', '984', '1000', '819', '556', '448', '594', '50', '331', '422',
    #       '673', '978', '648']
    # club数据集中综合影响力计算时间
    # ci = ['0', '16', '4', '5', '6', '10']
    ci = ['0', '1', '2', '3', '7', '8', '12', '13', '14', '15', '17', '18', '19', '20', '21', '22', '23', '26', '27', '28', '29', '30', '32', '33']
    # Dolphin数据集中综合影响力计算时间
    # ci = ['8', '45', '15', '18', '51', '50', '21', '23', '24', '59', '29']
    # ci = ['33', '34', '36', '37', '38', '8', '40', '43', '44', '45', '14', '16', '50', '52', '20', '21']
    # Football数据集中综合影响力计算时间
    # ci = ['2', '3', '68', '5', '69', '7', '72', '8', '74', '11', '10', '77', '78', '81', '84', '21', '22', '23', '24', '4', '90', '28', '97', '98', '102', '40', '107', '108', '111', '50', '51', '52']
    # ci = ['0', '67', '4', '68', '7', '8', '9', '77', '16', '21', '22', '23', '90', '93', '104', '41', '108', '46', '111', '114']
    # Facebook数据集中综合影响力计算时间
    # ci = ['594', '3980', '3989', '4011', '4031', '3981', '3982', '3983', '3984', '3985', '3986', '3987', '3988', '3990', '3991', '3992', '3993', '3994', '3995', '3996', '3997', '3998', '3999', '4000', '4001', '4002', '4003', '4004', '4005', '4006', '4007', '4008', '4009', '4010', '4012', '4013', '4014', '4015', '4016', '4017', '4018', '4019', '4020', '4021', '4022', '4023', '4024', '4025', '4026', '4027', '4028', '4029', '4030', '4032', '4033', '4034', '4035', '4036', '4037', '4038']
    # ci = ['1951', '1972', '1973', '1976', '1991', '1995', '1998', '2001', '2004', '2009', '2018', '2024', '2027', '2116', '2157', '2171', '2225', '2284', '2337', '2364', '2378', '2447', '2459', '2494', '2538', '2583', '2636', '2640', '2647', '2660', '1914', '1919', '1921', '1927', '1928', '1931', '1935', '1950', '1957', '1958', '1968', '1980', '1999', '2000', '2006', '2011', '2012', '2013', '2014', '2016', '2022', '2025', '2050', '2061', '2097', '2159', '2192', '2202', '2297', '2346', '2365', '2435', '2585', '2620', '2626', '2627', '2633', '2639', '2645', '2648', '2657', '2658', '2659']

    # 3. t
    # 通过不同的数据在不同的重叠社区检测算法下的节点综合影响力计算时间
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
    # 6.
    delCount = {}
    for _, c in enumerate(ci):
        delCount[c] = 0
        set1 = set(tb[c])
        set2 = set(ci)
        setResult = set1.intersection(set2)
        delCount[c] = len(setResult)-1
    # 7.
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
    # 8.
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
    print("数据集为club.dat")
    # print("数据集为dolphin.dat")
    # print("数据集为football.dat")
    # print("数据集为facebook.dat")
    print("Based_Influ方法综合影响力执行时间: ", time.microseconds, "微秒")
    return 0

if __name__ == '__main__':
    main(sys.argv[1:])