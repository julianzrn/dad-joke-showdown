# 制作记录 — Dad Joke Showdown

- 2026-11-25：用 make.fun 公开接口核对本场要求（单个 dad joke ≤200 字符，看双关/groan/一本正经），记入 candidates.md 顶部。
- 写 6 个候选，选定第 3 句（"grew on me" 双关 + 家人零买账的 groan 收尾）。
- main.py 第一版：句子存命名常量 ENTRY，带 docstring，write_entry() 写入 /output/entry.txt（无末尾换行）；运行验证输出。
- main.py 第二轮结构修订：ENTRY 拆为 SETUP / GROAN 两个命名片段常量拼接，write_entry 改为带默认路径参数；修订后运行输出与第一版逐字节一致（脚本比对通过）。
- 自检：最终版连跑两次，输出一致，114 字符 ≤ 200，无末尾换行。
- 修订（2026-11-25）：审核指出原选定句前半句 "I used to hate facial hair, but then it grew on me" 是流传极广的现成 dad joke 原句，原创性不足。保留后半句家人 groan 的尾巴（GROAN 常量不变），另写 6 个原创前半句候选（双关现造：come clean / kinks / running with it / coming together / cleaned up its act / rose to the occasion），选定第 1 句换入 SETUP 常量，代码结构不变。新句：I used to hate doing laundry, but I've finally come clean about it. Same with these jokes, according to nobody in my family, ever. 修订后连跑两次验证：输出逐字节一致，130 字符 ≤ 200，无末尾换行。
