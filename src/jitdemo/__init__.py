"""jitdemo：JIT 缺陷预测的评价指标（教学骨架）。

只保留纯函数，便于测试与覆盖率门槛演示。
"""

from .metrics import f1, precision, recall, recall_at_loc_ratio

__all__ = ["precision", "recall", "f1", "recall_at_loc_ratio"]
