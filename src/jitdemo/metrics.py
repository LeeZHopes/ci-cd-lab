"""JIT 缺陷预测的评价指标（最小实现，供测试门禁课程使用）。

真实项目里这些数字来自模型预测与 SZZ 标注，这里只保留纯函数部分，
好处是：逻辑可测、无外部依赖、跑得快。
"""

from __future__ import annotations

from collections.abc import Sequence


def precision(true_positives: int, predicted_positives: int) -> float:
    """精确率：预测为缺陷的提交里，真的有多少是缺陷。"""
    if predicted_positives <= 0:
        return 0.0
    return true_positives / predicted_positives


def recall(true_positives: int, actual_positives: int) -> float:
    """召回率：真的是缺陷的提交里，被抓到多少。"""
    if actual_positives <= 0:
        return 0.0
    return true_positives / actual_positives


def f1(precision_value: float, recall_value: float) -> float:
    """F1：精确率与召回率的调和平均。"""
    total = precision_value + recall_value
    if total <= 0:
        return 0.0
    return 2 * precision_value * recall_value / total


def recall_at_loc_ratio(
    labels: Sequence[int],
    scores: Sequence[float],
    ratio: float = 0.2,
) -> float:
    """Effort-aware 的最简形式：只检查得分最高的前 ratio 比例提交，能抓到多少缺陷。

    参数
    ----
    labels : 每个提交是否为缺陷提交（1/0）
    scores : 模型给出的风险分数，越大越可能缺陷
    ratio  : 要检查的比例，按 LOC 或提交数计，默认 20%

    返回
    ----
    被检查的提交中命中的缺陷数 / 全部缺陷数。
    """
    if len(labels) != len(scores):
        raise ValueError("labels 与 scores 长度必须一致")
    if not labels:
        raise ValueError("输入不能为空")
    if not 0 < ratio <= 1:
        raise ValueError("ratio 必须在 (0, 1] 之间")

    checked = max(1, round(len(labels) * ratio))
    order = sorted(range(len(labels)), key=lambda i: scores[i], reverse=True)[:checked]
    caught = sum(1 for i in order if labels[i])
    total = sum(1 for value in labels if value)
    return caught / total if total else 0.0
