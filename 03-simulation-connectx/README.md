# 03 · ConnectX → Simulation Competitor

ConnectX là cuộc thi dạng **simulation** (nộp agent dạng file `.py`, chấm bằng các ván đấu).
1. **Bạn phải làm trên web:** https://www.kaggle.com/competitions/connectx/rules → Accept.
2. Submit agent baseline (heuristic: thắng > chặn > cột giữa; local: 9/10 vs random, 6/10 vs negamax):
```bash
source scripts/env.sh
python 03-simulation-connectx/baseline/evaluate.py 03-simulation-connectx/baseline/submission.py
scripts/submit.sh connectx 03-simulation-connectx/baseline/submission.py "heuristic agent (Claude)"
```
Giới hạn: **2 submission/ngày**. Phải đợi khoảng 1 ngày để agent đấu xong và có điểm.
3. Bài học của bạn: `src/submission.py` → tự viết negamax/minimax, test bằng `evaluate.py src/submission.py`.

Nếu badge chưa hiện (ConnectX nằm trong nhóm "Getting Started") thì dùng phương án dự phòng: một simulation khác đang mở (ví dụ `the-pokemon-company-ptcg-ai-battle-challenge-playground`, hạn 2027-01-08).
