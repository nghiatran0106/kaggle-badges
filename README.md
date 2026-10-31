# kaggle-badges

Mỗi thư mục ứng với một hoặc vài badge Kaggle. Thư mục nào cũng tách hai phần:
- `baseline/`: bản tối thiểu do Claude viết, **chỉ để lấy badge**. Đừng copy, hãy đọc hiểu rồi tự viết lại.
- `src/`: phần **của bạn**, có sẵn khung TODO. Bạn tự code, Claude review, sau đó bạn commit/push/submit theo `PROCEDURE.md`.

Thiết lập một lần: `source scripts/env.sh` (venv ở `~/.venvs/kaggle-badges`, vì ổ exFAT không tạo được symlink cho venv).

## Bảng badge (cập nhật 2026-10-31)

✅ đã xong qua CLI · 🖱️ cần bạn bấm vài nút trên web · ⏳ cần thời gian / đợi mùa giải · ⛔ không còn đạt được

| # | Badge | Trạng thái | Thư mục / việc cần làm |
|---|---|---|---|
| 1 | Getting Started Competitor | ✅ Titanic 0.78708 | 01 |
| 2 | Playground Competitor | ✅ late submission S6E5 (0.94018), chờ xác nhận badge | 02-playground-s6e5 |
| 3 | Simulation Competitor | ✅ đã submit agent ConnectX, chờ xác nhận badge | 03 |
| 4 | R Coder | ✅ notebook R đã push | 04 |
| 5 | R Markdown Coder | ✅ script .Rmd đã push | 05 |
| 6 | API Model Creator | ✅ model tạo qua CLI | 06 |
| 7 | Model Variation Creator | ✅ 2 variation | 06 |
| 8 | Model Tagger | 🖱️ thêm tag cho model | 06 |
| 9 | Model Documenter | 🖱️ ảnh bìa + tag + notebook public → 10/10 | 06 |
| 10 | Benchmark Task local builder | ✅ task `vietnam-capital` | 07 |
| 11 | Utility Scripter | 🖱️ File → Set as Utility Script | 08 |
| 12 | Dataset Documenter | 🖱️ đang 15/17; chạy `09-dataset-documenter/baseline/publish.sh` | 09 |
| 13 | Model Pipeline Creator | 🖱️ Output → New Model | 10 |
| 14 | Github Coder | 🖱️ cần push repo public trước | 11 |
| 15 | Linked Dataset Creator | 🖱️ cần push repo public trước | 11 |
| 16 | Linked Model Creator | 🖱️ cần push repo public trước | 11 |
| 17 | Code Forker | 🖱️ Copy & Edit, sửa, Save | 12 |
| 18 | Stylish · Collector · Bookmarker · Agent of Discord | 🖱️ khoảng 15 phút | 15 |
| 19 | Santa Competitor | ✅ late submission santa-2025 (173.65), chờ xác nhận badge; nếu không tính thì Santa 2026 | 13 |
| 20 | March Mania Competitor | ✅ late submission mùa 2026 (0.25), chờ xác nhận badge; nếu không tính thì mùa 2027 | 14 |
| 21 | Student / Graduate | ⏳ 5 / 10 khoá Kaggle Learn | 16 |
| 22 | Submission Streak 7 / 30 / 100 | ⏳ tính cả ClimX/UMUD/3LC; xem `scripts/streak.sh` | 17 |
| 23 | 100 Day / Year Long Login Streak | ⏳ đăng nhập mỗi ngày | 17 |
| 24 | 2 / 5 / 10 / 15 Years on Kaggle | ⏳ chỉ phụ thuộc tuổi tài khoản | — |
| 25 | 5-Day Gen AI / AI Agents / Vibe Coding Intensive | ⛔ khoá theo đợt đã kết thúc; chờ Kaggle mở đợt mới | — |
| 26 | Stack Overflow Road Safety Challenge | ⛔ sự kiện S5E10 (2025) đã đóng | — |
| 27 | Founding Benchmark Task Author | ⛔ chỉ dành cho người tham gia early access | — |

Badge có thể mất vài giờ đến 1 ngày mới hiện trên profile.

## Scripts
| Lệnh | Tác dụng |
|---|---|
| `scripts/submit.sh <comp> <file> "<msg>"` | submit, ghi log, báo 403 nếu chưa accept rules |
| `scripts/push_kernel.sh <folder>` | push notebook/script và chờ chạy xong |
| `scripts/status.sh` | liệt kê kernel, dataset, model, submission |
| `scripts/streak.sh` | đếm số ngày submit liên tiếp (UTC) trên mọi cuộc thi đã tham gia |
