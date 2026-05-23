import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def build_tree():
    # 创建一个图
    tree = nx.Graph()

    # 添加边，构造树结构
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    tree.add_edges_from(edges)

    return tree

def breadth_first_traversal(tree, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            neighbors = tree.neighbors(current_node)
            queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

def visualize_tree(tree):
    pos = nx.spring_layout(tree)
    plt.figure(figsize=(8, 6))
    nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', font_size=10, alpha=0.8, edge_color='gray')
    plt.title('Tree Structure')
    plt.show()

if __name__ == "__main__":
    tree = build_tree()
    start_node = 1  # 选择起始节点

    print("Breadth-First Traversal:")
    breadth_first_traversal(tree, start_node)

    print("\n\nVisualization of the Tree:")
    visualize_tree(tree)
