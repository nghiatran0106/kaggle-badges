# 06 · Model qua API → API Model Creator ✅ · Model Variation Creator ✅ · Model Tagger · Model Documenter

Model (private): https://www.kaggle.com/models/tranphunghia233871/titanic-randomforest-baseline
Có 2 variation là `rf-small` và `rf-large` (framework ScikitLearn), tạo bằng:
```bash
kaggle models create -p 06-model-api/baseline
kaggle models variations create -p 06-model-api/baseline/variations/rf-small
kaggle models variations create -p 06-model-api/baseline/variations/rf-large
```
Phần còn lại làm trên web (trang model → Edit):
- **Model Tagger:** thêm tag (ví dụ *Tabular*, *Binary Classification*, *Scikit-learn*).
- **Model Documenter** (usability 10/10): thêm ảnh bìa, tag, mô tả (đã có), license cho từng variation (đã có), và **một notebook public dùng model này**. Có thể cần chuyển model sang Public. Trên trang model có checklist usability, làm hết các mục đó.
