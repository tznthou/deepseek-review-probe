# deepseek-review-probe

[tznthou/deepseek-code-review](https://github.com/tznthou/deepseek-code-review)
的**跨 repo 整合測試場**。

這裡不放真正的程式，只放最小的素材（`app.py`、`run.sh`）和三份照
[USAGE.md](https://github.com/tznthou/deepseek-code-review/blob/main/USAGE.md)
抄來的 caller，用來回答一個問題：**那份文件照抄，是不是真的跑得起來。**

## 怎麼用它做回歸測試

改了 kit 的 reusable workflow 之後：

1. push 一個 commit 到 `trigger` 分支（PR #1 一直開著，會自動重跑）
2. 看三支 workflow 的結果

```
code review        → static（reviewdog / gitleaks）+ codeql（CodeQL / Trivy）
ai review collect  → 產 diff artifact
ai review post     → 由 workflow_run 觸發，呼叫 DeepSeek
```

`ai review post` **預期會失敗**：這裡的 `DEEPSEEK_API_KEY` 是假值，會在呼叫 API 時
回 401。那是刻意的——**失敗點的位置就是證據**。停在 401 代表前面的 checkout
`.kit@v1`、下載 artifact、選 rubric、反查 PR 編號全都走通了；如果失敗在更早的地方，
那才是真的壞了。

## 這裡的 secret 都是假的

| Name | 用途 |
|---|---|
| `DEEPSEEK_API_KEY` | 驗證 secret 傳遞，以及 401 的失敗位置 |
| `PROBE_SECRET` | 早期驗證 `secrets: inherit` 與明確傳兩種寫法 |

**不要在這個 repo 放真的憑證。**

## 這裡驗出來的東西

2026-09-20 用這個 repo 確認了三件官方文件沒寫、或寫了但沒說清楚的事：

1. **由 `workflow_run` 觸發的 caller 可以呼叫跨 repo 的 reusable workflow**（文件沒寫）
2. **reusable workflow 裡的 `actions/checkout` 抓的是呼叫方的 repo**，所以 kit 的腳本
   與 rubric 必須自己再 checkout 一次
3. **caller 不宣告 `permissions` 會整個 `startup_failure`**——被呼叫的 workflow 拿不到
   超過呼叫方的權限。這個失敗特別難查：`actionlint` 驗不出來、`--log-failed` 是空的、
   `gh run view` 只會說「likely failed because of a workflow file issue」

第四輪：驗證 v1.0.1（shell injection 修正）。
