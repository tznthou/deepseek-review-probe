# deepseek-review-probe

暫時性的探針 repo，只為回答一個問題：

> 由 `workflow_run` 觸發的 caller workflow，能不能呼叫**跨 repo** 的 reusable workflow？

官方文件沒有寫，從 `uses:` 的語法層面推論是可以（它是 job 層級的語法，與觸發事件無關），
但推論不是事實。

配對的 reusable workflow 在
[tznthou/deepseek-code-review](https://github.com/tznthou/deepseek-code-review)
的 `probe/reusable-workflow-run` 分支。

驗證完畢後這個 repo 會被刪除。
