# 02 · Playground S6E10 → Playground Competitor ⏰ hạn 2026-10-31

1. **Bạn phải làm trên web:** https://www.kaggle.com/competitions/playground-series-s6e10/rules → *I Understand and Accept* (chưa accept thì CLI báo 403).
2. Tải data + chạy baseline + submit:
```bash
source scripts/env.sh
kaggle competitions download playground-series-s6e10 -p 02-playground-s6e10/data && (cd 02-playground-s6e10/data && unzip -o *.zip && rm *.zip)
python 02-playground-s6e10/baseline/baseline.py
scripts/submit.sh playground-series-s6e10 02-playground-s6e10/submissions/baseline.csv "lgbm baseline (Claude)"
```
3. Sau đó tự làm `src/solution.py`. Nếu lỡ hạn S6E10 thì dùng S6E11 (ra đầu tháng 11). Đổi slug là xong.

Baseline dùng được cho mọi episode: `python 02-playground-s6e10/baseline/baseline.py <thư-mục-episode>`. Đã dùng cho S6E5 (`02-playground-s6e5`, F1 pit stop, public 0.94018).
