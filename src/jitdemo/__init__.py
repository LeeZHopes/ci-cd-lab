"""jitdemo：JIT 缺陷预测的评价指标（教学骨架）。

只保留纯函数，便于测试与覆盖率门槛演示。
"""

from .metrics import f1, precision, recall, recall_at_loc_ratio

# 注意：ruff 的 RUF022 要求 __all__ 按字母序排列（f1 在 precision 之前）
__all__ = ["f1", "precision", "recall", "recall_at_loc_ratio"]
