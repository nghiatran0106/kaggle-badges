# 09 · Dataset → Dataset Documenter (usability 10)

Dataset (private): https://www.kaggle.com/datasets/tranphunghia233871/connectx-self-play-game-logs
Gồm 400 ván ConnectX tự sinh (`baseline/generate.py`), metadata đầy đủ trong `baseline/upload/dataset-metadata.json` (subtitle, mô tả, license, tag, mô tả file và cột, nguồn, tần suất cập nhật).

Usability hiện tại: **15/17 (0.882)**. Ảnh bìa (`baseline/make_cover.py`) và metadata đặt được bằng CLI:
```bash
kaggle datasets metadata --update -p 09-dataset-documenter/baseline/upload tranphunghia233871/connectx-self-play-game-logs
```
Lưu ý: mô tả file và cột chỉ được lưu khi tạo version (`kaggle datasets version`), `metadata --update` không đủ. Client cũng hiểu thiếu `isPrivate` là public, nên luôn giữ trường này trong file.

Bước cuối (cần bạn tự chạy vì nó công khai nội dung): `09-dataset-documenter/baseline/publish.sh` chuyển dataset sang public và đăng notebook `baseline/notebook/`. Dự kiến lên 17/17.

Cập nhật version: `kaggle datasets version -p 09-dataset-documenter/baseline/upload -m "msg"`
