# 04 · R notebook → R Coder ✅ (đã push, chạy COMPLETE)

https://www.kaggle.com/code/tranphunghia233871/titanic-eda-r-badge (private)

Bài học: viết `src/` là notebook R của chính bạn (ví dụ: logistic regression Titanic bằng `tidymodels`), copy `baseline/kernel-metadata.json` sang `src/`, đổi `id`, `code_file`, rồi:
```bash
scripts/push_kernel.sh 04-r-notebook/src
```
Lưu ý: trên Kaggle hiện nay dữ liệu cuộc thi không nằm ở `/kaggle/input/titanic/` nữa, nên hãy dùng `list.files("/kaggle/input", recursive=TRUE)` để tìm file.
