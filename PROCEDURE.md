# Quy trình học (áp dụng cho mọi thư mục)

## 1. Code
```bash
cd /media/TranPhuNghia_20233871/TRANSCEND/kaggle-badges
source scripts/env.sh
git switch -c 01-titanic-v1          # mỗi bài 1 nhánh
# sửa <thư mục>/src/..., chạy thử cho tới khi ra file submission
```

## 2. Nhờ Claude review
Nói với Claude: *"review 01-getting-started-titanic/src"*. Claude sẽ đọc `git diff`, chạy thử, chỉ ra lỗi (leak, CV sai, sai format submission…) và góp ý. Bạn tự sửa theo góp ý.

## 3. Commit & push
```bash
git status                           # chắc chắn không có data/, .env, *.pkl
git add 01-getting-started-titanic/src
git commit -m "titanic: title + family-size features, CV 0.83"
# lần đầu: tạo repo public trên GitHub (cần cho thư mục 11)
gh repo create nghiatran0106/kaggle-badges --public --source . --remote origin
git push -u origin 01-titanic-v1
gh pr create --fill                  # tự review PR, rồi merge vào main
```

## 4. Submit
```bash
scripts/submit.sh titanic 01-getting-started-titanic/submissions/solution.csv "v1: title+family"
scripts/streak.sh
```
Ghi điểm public vào README của thư mục và so với baseline.

## Quy tắc
- Không commit dữ liệu cuộc thi (luật cuộc thi cấm phát tán), file `.env` hay token.
- Mỗi người chỉ được có 1 tài khoản Kaggle. Không dùng tài khoản phụ, không mượn tài khoản, không nhờ vote theo nhóm.
