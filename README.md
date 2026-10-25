# py-starter：第 04 课用的最小 Python 项目

放进新仓库就能跑通「lint → 测试 → 覆盖率门槛 → 报告留档」四步，用来练测试门禁，不用先搭实训项目的完整代码。

## 结构

```
py-starter/
├── pyproject.toml            # 包配置 + pytest / coverage / ruff 设置
├── src/jitdemo/
│   ├── __init__.py
│   └── metrics.py            # precision / recall / f1 / recall_at_loc_ratio
├── tests/test_metrics.py     # 11 个用例，含边界与异常路径
└── .github/workflows/ci.yml  # 门禁本体（3 个 Python 版本矩阵）
```

## 用法

```powershell
# 1) 在 GitHub 新建空仓库（如 jit-門禁练习），把本目录内容复制进去
cd D:\myself\ci-cd-lab\py-starter
git init -b main
git add .
git commit -m "chore: bootstrap jit demo with ci gate"
git remote add origin git@github.com:<你的用户名>/<仓库名>.git
git push -u origin main
```

## 本地跑（可选）

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[dev]"
.venv\Scripts\python.exe -m pytest --cov --cov-fail-under=80 --cov-report=term-missing
```

## 三个反证实验（课程的验收点，已实测）

| 实验 | 改什么 | 实测结果 |
|---|---|---|
| ① 门槛不触发 | 删掉 `test_recall_at_loc_ratio_rejects_bad_input` + `test_recall_at_loc_ratio_no_positive_labels` | 覆盖率 **85.4%**，仍然绿（85 > 80） |
| ② 门槛触发 | 再把 `test_recall_at_loc_ratio_takes_top_scored_only` 删掉 | 覆盖率 **58.5%**，**红**，且报告照样上传 |
| ③ 断言失败 | 把某条断言改成 `assert 1 == 2` | pytest 红，junit 报告里能定位到具体断言 |

初始状态实测：**12 passed，覆盖率 100%**（29 条语句 / 12 个分支），ruff 无告警。

> 结论：门禁的价值不在「跑测试」，而在**红了就合不进去**；而门槛只在你跨过那条线时才拦你——所以 ratcheting 要贴近现状。
