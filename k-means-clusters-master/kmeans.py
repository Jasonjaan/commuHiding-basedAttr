import scikit

from sklearn.metrics.cluster import normalized_mutual_info_score

def calculate_nmi(ground_truth_labels, predicted_labels):
    """
    计算规范化互信息（NMI）

    参数:
    - ground_truth_labels: 真实标签
    - predicted_labels: 预测标签

    返回:
    - nmi_score: 规范化互信息分数
    """
    nmi_score = normalized_mutual_info_score(ground_truth_labels, predicted_labels)
    return nmi_score

# 示例用法
# 替换下面的数据为你实际的数据
ground_truth_labels = [0, 0, 1, 1, 2, 2]
predicted_labels = [0, 0, 1, 1, 3, 3]

nmi_score = calculate_nmi(ground_truth_labels, predicted_labels)
print("规范化互信息分数:", nmi_score)