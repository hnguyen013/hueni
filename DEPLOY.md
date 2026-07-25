# HƯỚNG DẪN DEPLOY — Render (Task 5.3)

> Nền tảng đã chọn: **Render** — free tier có Postgres miễn phí (90 ngày,
> gia hạn được), tự build từ GitHub, hỗ trợ tốt Django/gunicorn, cấu hình
> qua file `render.yaml` (Blueprint) nên không cần bấm tay từng ô trên
> dashboard. Lý do không chọn PythonAnywhere: free tier không cho phép
> Postgres + khó tự động hoá build (phải SSH cấu hình tay). Lý do không
> chọn Railway: free tier gần đây giới hạn theo giờ dùng/tháng chặt hơn
> Render và không có Blueprint file chuẩn hoá tương đương.

## 0. Tổng quan các file liên quan (đã tạo sẵn trong Task 5.3)

| File | Vai trò |
|---|---|
| `config/settings.py` | Đọc cấu hình qua biến môi trường (xem bảng biến ở mục 3) — **không cần sửa file này để deploy**, chỉ cần set đúng biến môi trường. |
| `requirements.txt` | Đã thêm `gunicorn`, `whitenoise`, `dj-database-url`, `psycopg[binary]` (Postgres), `django-storages`+`boto3` (tuỳ chọn S3). |
| `Procfile` | Dùng nếu deploy thủ công kiểu Heroku/Railway (`web: gunicorn ...`). Render không bắt buộc cần file này nếu dùng `render.yaml`, nhưng để sẵn cho tương thích. |
| `render.yaml` | **Blueprint** — Render đọc file này để tự tạo 1 Web Service + 1 Postgres database, tự nối `DATABASE_URL`, tự sinh `DJANGO_SECRET_KEY`. Cách nhanh nhất, khuyến nghị dùng file này. |
| `.env.example` | Danh sách biến môi trường cần thiết, dùng làm tham chiếu khi tự điền tay trên dashboard (nếu không dùng Blueprint). |

## 1. Chuẩn bị

1. Tạo tài khoản GitHub (nếu chưa có) và tài khoản [Render](https://render.com)
   (đăng nhập bằng GitHub cho tiện).
2. Đẩy toàn bộ project (thư mục có `manage.py` ở gốc) lên 1 repo GitHub:
   ```powershell
   cd đường-dẫn-tới-project
   git init
   git add .
   git commit -m "Deploy: chuẩn bị lên Render"
   git branch -M main
   git remote add origin https://github.com/<username>/<ten-repo>.git
   git push -u origin main
   ```
   Kiểm tra `.gitignore` đã có sẵn `venv/`, `db.sqlite3`, `staticfiles/`,
   `node_modules/`, `.env` — không commit nhầm mấy thứ này.

## 2. Deploy bằng Blueprint (`render.yaml`) — cách nhanh nhất

1. Vào <https://dashboard.render.com/blueprints> → **New Blueprint Instance**.
2. Chọn repo GitHub vừa đẩy lên. Render tự đọc `render.yaml` ở gốc repo,
   hiện preview: 1 Web Service (`hueni`) + 1 Postgres (`hoclieuso-db`).
3. Bấm **Apply** — Render tự động:
   - Tạo Postgres database, set `DATABASE_URL` cho Web Service.
   - Tự sinh `DJANGO_SECRET_KEY` ngẫu nhiên (an toàn, không cần tự nghĩ).
   - Set `DJANGO_ALLOWED_HOSTS` = đúng domain Render vừa cấp
     (`hueni.onrender.com`).
   - Chạy `buildCommand` (cài dependency, build Tailwind, `collectstatic`,
     `migrate`) rồi `startCommand` (`gunicorn config.wsgi:application`).
4. `DJANGO_CSRF_TRUSTED_ORIGINS` đã được set sẵn đúng
   `https://hueni.onrender.com` khớp tên service — không cần sửa gì thêm
   nếu build từ `render.yaml` này. Nếu build ra domain khác (Render đôi khi
   thêm hậu tố nếu tên bị trùng, vd `hueni-abcd.onrender.com`), sửa lại giá
   trị này cho khớp domain thật rồi **Manual Deploy → Deploy latest commit**.
5. Đợi build xong (theo dõi log ngay trên dashboard) → mở link
   `https://<ten-app>.onrender.com` — sẽ thấy trang chủ (chưa có dữ liệu
   vì DB Postgres mới còn trống).

> ⚠️ **Muốn đổi tên app/domain SAU KHI đã deploy?** Không sửa `name:` trong
> `render.yaml` rồi push — Blueprint dùng `name` để nhận diện service đã
> tồn tại, sửa trong file mà không đổi trên dashboard trước dễ khiến Render
> hiểu nhầm là phải **tạo mới** 1 service khác, để service cũ mồ côi. Thứ tự
> đúng: (1) Dashboard → service đang chạy → **Settings → Name** → đổi tên
> → Save (đây là bước đổi domain thật); (2) sau đó mới sửa `name:` trong
> `render.yaml` cho khớp lại; (3) `git push` rồi Manual Deploy.


## 3. Nếu muốn tự cấu hình tay (không dùng Blueprint)

Tạo **Web Service** mới trỏ tới repo, chọn Runtime = Python, rồi điền:

- **Build Command:**
  ```
  pip install -r requirements.txt && npm install && npm run build && python manage.py collectstatic --noinput && python manage.py migrate --noinput
  ```
- **Start Command:**
  ```
  gunicorn config.wsgi:application
  ```
- Tạo thêm 1 **Postgres** instance riêng (Render dashboard → New → Postgres),
  copy **Internal Database URL** của nó.
- Vào tab **Environment** của Web Service, thêm đúng các biến trong bảng
  dưới (tham khảo `.env.example`):

| Biến | Giá trị ví dụ | Bắt buộc? |
|---|---|---|
| `DJANGO_SECRET_KEY` | chuỗi ngẫu nhiên ≥50 ký tự | **Có** |
| `DJANGO_DEBUG` | `False` | **Có** |
| `DJANGO_ALLOWED_HOSTS` | `ten-app.onrender.com` | **Có** |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://ten-app.onrender.com` | **Có** |
| `DATABASE_URL` | Internal Database URL của Postgres vừa tạo | **Có** |
| `USE_S3_MEDIA` | `False` (hoặc `True` nếu dùng S3, xem mục 5) | Không |
| `PYTHON_VERSION` | `3.12.3` | Khuyến nghị |

## 4. Sau khi deploy xong — tạo dữ liệu & superuser

Render cho phép mở **Shell** trực tiếp trên container đang chạy (dashboard
→ service → tab **Shell**):

```bash
python manage.py createsuperuser
python manage.py seed_demo_data
```

- `createsuperuser` để có tài khoản đăng nhập `/admin/`.
- `seed_demo_data` để có ngay 2 Era/4 Lesson demo (xem Task 5.1) — **lưu ý
  mục 6 bên dưới** nếu không dùng S3, dữ liệu ảnh demo sẽ mất sau lần
  deploy tiếp theo, cần chạy lại lệnh này mỗi lần redeploy.

## 5. (Tuỳ chọn) Bật lưu media bền vững qua Amazon S3

Mặc định (`USE_S3_MEDIA=False`), ảnh/file người dùng upload qua `/admin/`
lưu trên đĩa container — **sẽ mất mỗi khi Render build lại** (đĩa tạm).
Nếu cần lưu lâu dài (không chỉ demo), làm theo các bước sau:

1. Tạo bucket S3 mới trên AWS Console (vùng gần VN, vd `ap-southeast-1`),
   tắt "Block all public access" nếu muốn ảnh truy cập public trực tiếp
   (khuyến nghị cho website trưng bày công khai như dự án này).
2. Tạo IAM user riêng chỉ có quyền đọc/ghi đúng bucket đó (không dùng
   root key), lấy `Access Key ID` + `Secret Access Key`.
3. Set thêm các biến môi trường trên Render:
   - `USE_S3_MEDIA=True`
   - `AWS_ACCESS_KEY_ID=...`
   - `AWS_SECRET_ACCESS_KEY=...`
   - `AWS_STORAGE_BUCKET_NAME=ten-bucket`
   - `AWS_S3_REGION_NAME=ap-southeast-1`
4. Deploy lại (Manual Deploy) — từ giờ media upload mới sẽ lưu lên S3 tự
   động (`config/settings.py` đã có sẵn logic đọc `USE_S3_MEDIA`, không
   cần sửa code). Ảnh cũ đã có trên đĩa tạm (nếu còn) sẽ không tự chuyển
   sang S3 — cần upload lại hoặc viết script di chuyển riêng nếu cần.

## 6. Giới hạn cần biết (free tier)

- **Đĩa tạm (ephemeral disk):** nếu không bật S3, mọi ảnh/file upload qua
  `/admin/` mất khi Render build lại (deploy code mới, hoặc container bị
  khởi động lại do rảnh quá lâu). Với mục đích demo/đồ án, giải pháp đơn
  giản nhất là chạy lại `python manage.py seed_demo_data` (idempotent,
  không tạo trùng Era/Lesson nhưng sẽ tạo lại đúng nội dung con nếu DB bị
  reset) sau mỗi lần deploy quan trọng.
- **Free Web Service tự "ngủ"** sau ~15 phút không có truy cập, lần truy
  cập đầu tiên sau đó sẽ chậm (cold start ~30–60 giây) — bình thường, không
  phải lỗi.
- **Free Postgres hết hạn sau 90 ngày** (theo chính sách Render hiện tại,
  có thể thay đổi) — cần tạo lại hoặc nâng cấp plan trả phí nếu dùng lâu
  dài; kiểm tra chính sách mới nhất trên trang Render trước khi phụ thuộc
  vào free tier cho production thật.

## 7. Deploy lại sau khi sửa code

Chỉ cần `git push` lên nhánh đã kết nối — Render tự động build & deploy lại
(có thể tắt "Auto-Deploy" trên dashboard nếu muốn tự bấm Deploy thủ công).
Nhớ: nếu sửa CSS/template, `npm run build` đã nằm trong `buildCommand` nên
Render tự chạy lại, không cần build tay trước khi push.

## 8. Sự cố thực tế đã gặp & đã sửa

- **Build lỗi `django.db.utils.OperationalError: [Errno -2] Name or
  service not known`** khi chạy `migrate` trong `buildCommand`. Nguyên
  nhân: `databases:` trong `render.yaml` **thiếu `region:`**, khiến
  Postgres bị tạo ở region mặc định (khác region `singapore` của web
  service) — internal `DATABASE_URL` chỉ resolve được giữa các service
  **cùng region**, khác region là lỗi DNS y hệt trên. Đã sửa: thêm
  `region: singapore` vào `databases:` trong `render.yaml` (khớp web
  service). Nếu gặp lại lỗi này: kiểm tra `region` của cả 2 khối
  `databases:`/`services:` có khớp nhau không trước khi nghi ngờ chỗ khác.
- **Đổi tên app/domain (vd `hoclieuso` → `hueni`)** phải làm đúng thứ tự:
  đổi trên Dashboard (**Settings → Name**) trước, rồi mới sửa `name:`
  trong `render.yaml` cho khớp — xem cảnh báo ⚠️ ở mục 2. Sửa ngược thứ tự
  (chỉ sửa file rồi push) có thể khiến Render tạo nhầm 1 service mới thay
  vì đổi tên service cũ.
