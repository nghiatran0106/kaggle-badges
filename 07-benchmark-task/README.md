# 07 · Kaggle Benchmarks → Benchmark Task local builder ✅

Task đã push: https://www.kaggle.com/benchmarks/tasks/tranphunghia233871/vietnam-capital
```bash
cd 07-benchmark-task/baseline
kaggle benchmarks init -y                  # tạo .env (credential model proxy, KHÔNG commit) + example
kaggle b t push vietnam-capital -f vietnam_capital_task.py --wait
kaggle b t run vietnam-capital             # chạy thêm trên model khác
```
Bài học: viết một task nhiều câu hỏi trong `src/` (đọc `baseline/kaggle_benchmarks_reference.md`), ví dụ đánh giá LLM trả lời lịch sử/địa lý Việt Nam.
