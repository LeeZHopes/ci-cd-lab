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
