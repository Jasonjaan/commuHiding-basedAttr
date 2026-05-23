import networkx as nx
import random

# 创建一个包含80个节点的图
G = nx.Graph()

# 添加80个节点
nodes = range(80)
G.add_nodes_from(nodes)

# 添加500条边
while G.number_of_edges() < 500:
    node1, node2 = random.sample(nodes, 2)
    if not G.has_edge(node1, node2):
        G.add_edge(node1, node2)

# 划分成30个重叠社区，确保每个节点属于至少三个社区
communities = [set(random.sample(nodes, random.randint(3, 8))) for _ in range(30)]

# 添加剩余的节点以确保每个节点属于至少三个社区
remaining_nodes = set(nodes)
for community in communities:
    remaining_nodes -= community

for node in remaining_nodes:
    for _ in range(3):
        # 每个节点加入至多三个社区
        community = random.choice(communities)
        community.add(node)

# 构造重叠社区网络
overlap_network = nx.Graph()

# 将重叠社区中的节点连接起来
for community in communities:
    overlap_network.add_edges_from((n1, n2) for n1 in community for n2 in community if n1 != n2)

# 将边写入文件
with open('./networksynth/edges.txt', 'w') as edges_file:
    for edge in G.edges():
        edges_file.write(f"{edge[0]} {edge[1]}\n")

# 将社区写入文件
with open('./networksynth/communities.txt', 'w') as communities_file:
    for i, community in enumerate(communities):
        communities_file.write(f"{community}\n")

input_file_path = './networksynth/communities.txt'
output_file_path = './networksynth/communitie.txt'
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # 这里可以根据你的条件进行选择
        # 选择包含特定关键字的行
        for str23 in line.split(","):
            output_file.write(" ")
            output_file.write(str23)