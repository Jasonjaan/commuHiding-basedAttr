import Attrhiding
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    def __str__(self):
        return f"TreeNode(value={self.value})"
# #调用subcomunity中的目标节点
# T_num = subcommunity.T_num
#
# # 创建树的节点
# root = TreeNode(T_num)
# #循环遍历subcommunity.dat 对社区进行遍历，首先对所有社区成员数量进行排序，从高到低排序
#
#
# #遍历排序好的社区，如果社区中成员属于属于之前大社区的子社区，把该社区放在大社区的孩子节点上。
# child2 = TreeNode(2)
# child3 = TreeNode(3)
# child4 = TreeNode(4)
# child5 = TreeNode(5)
#
# # 连接节点
# root.add_child(child2)
# root.add_child(child3)
# child2.add_child(child4)
# child2.add_child(child5)