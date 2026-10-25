import pytest

from jitdemo import f1, precision, recall, recall_at_loc_ratio


def test_precision_basic():
    assert precision(3, 4) == pytest.approx(0.75)


def test_precision_zero_denominator_returns_zero():
    # 边界：没有任何预测时，约定返回 0 而不是抛异常
    assert precision(0, 0) == 0.0


def test_recall_basic():
    assert recall(2, 5) == pytest.approx(0.4)


def test_recall_zero_denominator_returns_zero():
    assert recall(0, 0) == 0.0


def test_f1_harmonic_mean():
    assert f1(0.5, 0.5) == pytest.approx(0.5)
    # 一边为 0 时 F1 必须为 0（这是 F1 与算术平均最大的不同）
    assert f1(1.0, 0.0) == 0.0


def test_f1_both_zero():
    assert f1(0.0, 0.0) == 0.0


def test_recall_at_loc_ratio_takes_top_scored_only():
    labels = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    scores = [0.9, 0.1, 0.2, 0.8, 0.3, 0.05, 0.4, 0.7, 0.15, 0.25]
    # 前 20%（=2 个）是 0.9 与 0.8 对应的两个提交，都是缺陷，但总共 3 个缺陷
    assert recall_at_loc_ratio(labels, scores, ratio=0.2) == pytest.approx(2 / 3)

    # 前 10%（=1 个）只抓到一个缺陷
    assert recall_at_loc_ratio(labels, scores, ratio=0.1) == pytest.approx(1 / 3)

    # 前 50%（=5 个）把三个缺陷全抓到
    assert recall_at_loc_ratio(labels, scores, ratio=0.5) == pytest.approx(1.0)
