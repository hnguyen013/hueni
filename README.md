# Hướng dẫn dùng trang Quản trị (Admin) — Website Trưng bày Học liệu số

> Dành cho nhóm sản xuất nội dung (không cần biết code). Toàn bộ việc thêm
> bài học, tải phiếu học tập, video, bản đồ, ảnh... đều làm qua trình duyệt,
> tại địa chỉ `/admin/`.

---

## 1. Đăng nhập

1. Mở trình duyệt, vào: **`https://hueni.onrender.com/admin/`**
   (máy local thì là `http://127.0.0.1:8000/admin/`).
2. Đăng nhập bằng tài khoản quản trị (username/password đã được cấp).
3. Vào được trang chủ Admin — thấy 2 khối chính: **TIMELINE** (Eras, Lessons)
   và **SHOWCASE** (Lesson Videos, Worksheets, Quizzes, Digital Maps,
   Galleries), cùng khối **PAGES** (Team Members, Site Contents).

---

## 2. Hiểu cấu trúc dữ liệu trước khi nhập

Mọi nội dung đều gắn vào **1 Bài học (Lesson)**, và mỗi Bài học thuộc về
**1 Giai đoạn (Era)**. Thứ tự bắt buộc: **tạo Era trước → rồi mới tạo
Lesson → rồi mới thêm tài liệu/video/quiz/bản đồ/ảnh vào bên trong Lesson đó.**

```
Era (giai đoạn lịch sử)
 └── Lesson (bài học) — có thể có nhiều bài trong 1 Era
      ├── Video (1 video)
      ├── Worksheet (nhiều phiếu học tập — TÀI LIỆU tải về)
      ├── Quiz (nhiều bộ câu hỏi, mỗi bộ nhiều câu, mỗi câu nhiều đáp án)
      ├── Digital Map (nhiều bản đồ)
      └── Gallery (nhiều bộ ảnh, mỗi bộ nhiều ảnh)
```

---

## 3. Tạo 1 Giai đoạn (Era) mới

1. Vào **TIMELINE → Eras → ADD ERA** (góc trên bên phải).
2. Điền:
   - **Name**: tên giai đoạn, vd "Thời kỳ Đại Việt".
   - **Slug**: bấm vào ô này, nếu để trống Django tự gợi ý theo Name (có
     nút tự sinh) — đây là phần URL, nên để tiếng Việt không dấu, không
     dấu cách (vd `thoi-ky-dai-viet`).
   - **Year label**: mốc năm hiển thị, vd "938 – 1858".
   - **Description**: mô tả ngắn (không bắt buộc).
   - **Order**: số thứ tự hiển thị trên trang chủ (số nhỏ hiện trước).
3. Bấm **SAVE**.

---

## 4. Tạo 1 Bài học (Lesson) — kèm luôn Video/Phiếu/Quiz/Bản đồ/Ảnh

Đây là màn hình quan trọng nhất — **nhập được toàn bộ nội dung 1 bài học
trong CÙNG 1 trang**, không cần chuyển qua lại nhiều màn hình.

1. Vào **TIMELINE → Lessons → ADD LESSON**.
2. Phần trên cùng — thông tin cơ bản:
   - **Era**: chọn giai đoạn đã tạo ở Bước 3.
   - **Title**: tên bài học.
   - **Slug**: để trống, tự sinh theo Title (hoặc bấm nút cạnh ô Title).
   - **Year label**: mốc năm của riêng bài học này.
   - **Summary**: đoạn tóm tắt ngắn, hiện ngay dưới tiêu đề trang chi tiết.
   - **Body**: nội dung chi tiết đầy đủ.
   - **Cover image**: **bắt buộc phải có** — bấm **Choose File**, chọn ảnh
     bìa từ máy tính. Đây là ảnh đại diện hiện ở node timeline + đầu trang
     chi tiết.
   - **Order**: số thứ tự trong Era.
   - **Is published**: **tích vào ô này** thì bài học mới hiện công khai
     trên web — quên tích thì bài học vẫn nằm trong admin nhưng người xem
     không thấy.
3. **Không bấm Save vội** — kéo xuống, các khối bên dưới cho phép nhập
   luôn nội dung con:

### 4.1. Khối "Lesson Videos" — thêm video

- **Title**: tên video (không bắt buộc).
- **Video url**: dán link Youtube trực tiếp vào đây (vd
  `https://www.youtube.com/watch?v=xxxxxxxxxxx`) — **cách được khuyến
  khích**, không cần upload file nặng.
- **Video file**: chỉ dùng nếu KHÔNG có link Youtube, muốn tự upload file
  video (.mp4) — để trống nếu đã điền Video url.

### 4.2. Khối "Worksheets" — **đây là chỗ tải TÀI LIỆU (phiếu học tập)**

Mỗi dòng là 1 tài liệu. Có sẵn 1 dòng trống, muốn thêm dòng nữa bấm
**"Add another Worksheet"** ở cuối khối.

- **Title**: tên tài liệu, vd "Phiếu học tập bài 1".
- **Preview image**: ảnh minh hoạ hiển thị trên thẻ tài liệu (không bắt
  buộc, nhưng nên có để đẹp giao diện) — bấm **Choose File**.
- **File**: **bắt buộc** — bấm **Choose File**, chọn file tài liệu thật từ
  máy (PDF, Word, ảnh chụp phiếu... định dạng nào cũng được, hệ thống chỉ
  lưu và cho tải về, không giới hạn loại file). Đây chính là file người
  xem sẽ bấm nút "Tải phiếu học tập" để tải về.
- **Order**: thứ tự hiển thị nếu có nhiều tài liệu.

> ⚠️ Nếu bạn chỉ muốn "up tài liệu" đơn thuần mà bài học đã tồn tại từ
> trước (không tạo Lesson mới), xem **Mục 7** bên dưới — thêm trực tiếp
> vào Worksheet mà không cần mở lại toàn bộ trang Lesson.

### 4.3. Khối "Quiz Showcases" — chỉ nhập nhanh tên bộ quiz

- **Title**, **Order**: điền cơ bản.
- Sau khi **Save** trang Lesson, quay lại khối này sẽ thấy link
  **"Change"** cạnh mỗi dòng — bấm vào để vào đúng trang quản lý quiz đó
  và nhập chi tiết từng câu hỏi + đáp án (xem Mục 5).

### 4.4. Khối "Digital Maps" — bản đồ số

Có 3 kiểu, chọn ở ô **Map type**, chỉ điền đúng 1 trong 3 mục tương ứng:

| Map type | Điền vào ô nào |
|---|---|
| **Nhúng iframe (embed)** | `Embed url` — dán link nhúng Google Maps (Chia sẻ → Nhúng bản đồ → copy URL trong `src="..."`) |
| **Ảnh tĩnh (image)** | `Image` — upload 1 ảnh bản đồ, người xem bấm vào sẽ phóng to (lightbox) |
| **GeoJSON + Leaflet** | `Geojson file` — upload file `.geojson`; sau khi Save, vào trang riêng của bản đồ này để thêm từng điểm đánh dấu (marker) — xem Mục 6 |

### 4.5. Khối "Galleries" — chỉ nhập nhanh tên bộ ảnh

Giống Quiz — điền Title/Order, Save xong bấm **"Change"** để vào thêm
từng ảnh (xem Mục 8).

4. Điền xong các khối cần thiết → bấm **SAVE** ở cuối trang (hoặc **Save
   and continue editing** nếu muốn ở lại trang để kiểm tra thêm).

---

## 5. Thêm câu hỏi cho Quiz (sau khi đã tạo bộ Quiz ở Mục 4.3)

1. Từ trang Lesson, bấm **Change** cạnh dòng Quiz cần sửa (hoặc vào
   **SHOWCASE → Quizzes** → chọn đúng bộ quiz).
2. Kéo xuống khối **"Quiz Questions"** → bấm **Add another Quiz Question**:
   - **Question text**: nội dung câu hỏi.
   - **Explanation**: giải thích hiện ra sau khi người xem chọn đáp án
     (không bắt buộc nhưng nên có).
   - **Order**: thứ tự câu hỏi.
3. Save trang Quiz → quay lại, bấm **Change** vào từng câu hỏi vừa tạo →
   kéo xuống khối **"Quiz Choices"** → thêm từng đáp án:
   - **Choice text**: nội dung đáp án.
   - **Is correct**: **tích vào ô này cho đúng 1 đáp án đúng** trong mỗi câu.
   - **Order**: thứ tự hiển thị đáp án.
4. Nên có tối thiểu 2 đáp án/câu (mặc định form đã chừa sẵn 2 dòng trống).

---

## 6. Thêm điểm đánh dấu cho bản đồ kiểu GeoJSON

1. Vào **SHOWCASE → Digital Maps** → chọn đúng bản đồ (map_type = geojson).
2. Kéo xuống khối **"Map Markers"** → thêm từng điểm:
   - **Label**: tên địa điểm.
   - **Lat** / **Lng**: toạ độ (lấy từ Google Maps — bấm chuột phải vào vị
     trí trên Google Maps sẽ hiện toạ độ, copy đúng 2 số vào 2 ô này).
   - **Note**: ghi chú hiện trong popup khi bấm vào điểm trên bản đồ.

---

## 7. Thêm/sửa tài liệu (Worksheet) mà không cần mở lại cả trang Lesson

Nếu bài học đã có sẵn, chỉ muốn thêm 1 tài liệu mới:

1. Vào **SHOWCASE → Worksheets → ADD WORKSHEET**.
2. Chọn **Lesson** tương ứng ở ô đầu tiên.
3. Điền Title, upload **File** (bắt buộc) + Preview image (tuỳ chọn).
4. Save.

---

## 8. Thêm ảnh cho Gallery

1. Vào **SHOWCASE → Galleries** → chọn đúng bộ ảnh (hoặc tạo mới, chọn
   Lesson tương ứng).
2. Kéo xuống khối **"Gallery Images"** → mỗi dòng 1 ảnh:
   - **Image**: bấm Choose File, chọn ảnh.
   - **Caption**: chú thích hiện trong lightbox khi phóng to ảnh.
   - **Order**: thứ tự ảnh trong bộ.

---

## 9. Sửa nội dung trang Giới thiệu / Liên hệ (không thuộc bài học)

- **PAGES → Team Members**: thêm/sửa thành viên đội ngũ sáng lập (Name,
  Role, Avatar, Bio) — hiện ở trang Giới thiệu.
- **PAGES → Site Contents**: các khối nội dung tĩnh khác (Hero, Tầm
  nhìn/Sứ mệnh, Giá trị cốt lõi ở trang Giới thiệu; thông tin liên hệ ở
  trang Liên hệ). Mỗi bản ghi có 1 **Section** (chọn đúng loại) — vd 3 bản
  ghi cùng section "Giới thiệu - Giá trị cốt lõi" sẽ hiện thành 3 cột.

---

## 10. Lưu ý quan trọng — file có thể bị mất

Nếu website đang chạy trên **free tier không bật lưu trữ S3**, đĩa lưu
file là **tạm thời**: mỗi lần trang web được cập nhật/deploy lại (đội kỹ
thuật đẩy code mới lên), **toàn bộ ảnh/file đã tải lên qua Admin sẽ bị xoá
sạch**, phải tải lại từ đầu. Nếu nhóm sản xuất nội dung đã nhập nhiều dữ
liệu thật, nên báo đội kỹ thuật kiểm tra đã bật lưu trữ bền vững (S3) chưa
trước khi nhập số lượng lớn, tránh mất công làm lại.

---

## 11. Một số lỗi hay gặp

| Hiện tượng | Nguyên nhân thường gặp | Cách sửa |
|---|---|---|
| Bài học không hiện ngoài trang chủ | Chưa tích **Is published** | Vào lại Lesson, tích ô Is published, Save |
| Bấm "Tải phiếu học tập" không ra gì | Chưa upload **File** ở Worksheet | Vào Worksheet tương ứng, upload lại File |
| Bản đồ không hiện | Chọn sai **Map type** so với ô đã điền (vd chọn "embed" nhưng lại điền Image) | Kiểm tra Map type khớp đúng ô đã điền theo bảng ở Mục 4.4 |
| Ảnh/file bị mất sau vài ngày | Chưa bật S3, site vừa được deploy lại | Xem Mục 10 — báo đội kỹ thuật |
| Không đăng nhập được `/admin/` | Sai username/password, hoặc tài khoản chưa được tạo | Liên hệ đội kỹ thuật cấp lại tài khoản |
