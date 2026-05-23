import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman

# 自己定义节点和边
nodes = [i for i in range(1, 51)]

# 生成边的方法可以根据需要进行调整
edges = [(i, i + 1) for i in range(1, 50)] + [(50, 1)]
edges += [(i, i + 2) for i in range(1, 48, 3)]  # 添加额外的边

# 创建图并添加节点和边
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# 使用 Girvan-Newman 算法检测社区
communities = girvan_newman(G)

# 选择 Girvan-Newman 算法的一步，你可以根据需要调整
communities = next(communities)

# 绘制网络图并标注社区
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, font_color='black', font_weight='bold', node_color='skyblue', edge_color='gray')

# 标注社区
for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos, nodelist=community, node_color=f'C{i+1}', label=f'Community {i+1}')

plt.legend()
plt.title("Custom Network with Overlapping Communities")
plt.show()
