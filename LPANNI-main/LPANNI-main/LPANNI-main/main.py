import sys, getopt
import networkx as nx
import lpanni
import generator
import sys
from datetime import datetime
import time
from datetime import datetime

def main(argv):
    opts = []
    try:
        opts, args = getopt.getopt(argv, 'i:o:')
    except:
        print('main.py -i <inputFile> -o <outputFile>')
    input_file = './input/network.dat'
    output_file = './output/community.dat'
    current_datetime1 = datetime.now()
    start_time = datetime.now()
    for o in opts:
        opt = o[0]
        value = o[1]
        if opt == '-i':
            input_file = value
        if opt == '-o':
            output_file = value
    g: nx.Graph = nx.read_edgelist(str(input_file))
    lpanni.LPANNI(g)
    gen = generator.GraphGenerator(0.4, g)
    communities = gen.get_Overlapping_communities()
    f = open(output_file, 'w')
    for community in communities:
        for u in community:
            f.write(str(u) + ' ')
        f.write('\n')
    f.flush()
    f.close()
    current_datetime2 = datetime.now()

    #print(current_datetime2-current_datetime1)
    end_time = datetime.now()
    print(f"社区检测时间：{(end_time-start_time).microseconds}微秒")


if __name__ == '__main__':
    main(sys.argv[1:])
