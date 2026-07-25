# CHECKLIST RESPONSIVE — Task 5.2

> Rà toàn bộ template (Nhóm 3), kiểm tra breakpoint `md:`/`lg:`. Test bằng
> Chrome DevTools responsive mode ở 3 mốc: 375px (mobile nhỏ), 768px
> (tablet/md), 1280px (desktop/lg), với dữ liệu thật từ `seed_demo_data`
> (Task 5.1).

## 1. Global Nav — `partials/navbar.html`
**Trạng thái: ĐÃ SỬA (lỗi tìm thấy + đã vá trong task này).**
- Lỗi tìm thấy: trước Task 5.2, menu dùng `hidden md:flex` cho 3 link
  (Hành trình/Giới thiệu/Liên hệ) — nghĩa là dưới `md` (< 768px) toàn bộ
  menu **biến mất hoàn toàn**, không có cách nào để điều hướng sang trang
  Giới thiệu/Liên hệ từ mobile ngoài link logo. Nút "Bắt đầu" vẫn hiện
  nhưng không thay thế được menu.
- Đã sửa: thêm nút hamburger (`#nav-toggle`, chỉ hiện `md:hidden`) +
  panel `#mobile-menu` (ẩn mặc định bằng pattern `hidden` + `flex` như
  các modal khác trong project, JS chỉ toggle class `hidden`). Nút
  "Bắt đầu" ở thanh ngang chuyển thành `hidden md:inline-flex` (ẩn ở
  mobile, đã có bản riêng trong panel) để tránh lặp 2 nút cùng lúc.
- JS mới: `static/js/navbar.js` (thuần, không phụ thuộc thư viện ngoài),
  tự đóng menu khi bấm 1 link hoặc khi resize sang ≥768px.
- Test: 375px — hamburger hiện, bấm mở ra đủ 3 link + nút Bắt đầu dạng
  cột, đóng lại khi bấm link. 768px trở lên — hamburger ẩn, menu ngang
  hiện như cũ, panel mobile luôn ẩn (do có `md:hidden` cứng, độc lập với
  trạng thái JS).

## 2. Trang chủ / Hành trình — `timeline/timeline_home.html`
**Trạng thái: ĐÃ ĐẠT (không cần sửa).**
- Node timeline dùng `flex-col md:flex-row` cho từng lesson-card → dọc gọn
  trên mobile (ảnh trên, chữ dưới), ngang trên tablet/desktop.
- Đường kẻ dọc + node tròn (`border-l-2 border-secondary/30 ml-3 md:ml-6`)
  giữ nguyên dạng dọc ở mọi kích thước màn hình — đúng yêu cầu thiết kế
  "Story Timeline", không có breakpoint chuyển ngang→dọc vì ngay từ đầu
  đã là dạng dọc theo `screen.png`/DESIGN.md.
- Test 375px: card không bị tràn ngang, ảnh full-width, chữ xuống dòng
  bình thường.

## 3. Trang chi tiết bài học — `timeline/lesson_detail.html`
**Trạng thái: ĐÃ ĐẠT (không cần sửa).**
- Header, ảnh bìa, video (`aspect-video`) co giãn đúng tỉ lệ mọi màn hình.
- Breadcrumb, tiêu đề dùng cỡ chữ responsive (`text-3xl md:text-display-md`).

## 4. Section Phiếu học tập — `showcase/_worksheets.html`
**Trạng thái: ĐÃ ĐẠT.**
- Grid `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` — 1 cột ở mobile, 2 cột
  tablet nhỏ, 3 cột từ `lg` — không tràn, ảnh preview giữ tỉ lệ `aspect-[4/3]`.

## 5. Section Bộ câu hỏi (quiz) — `showcase/_quiz.html`
**Trạng thái: ĐÃ ĐẠT.**
- Card quiz giới hạn `max-w-2xl`, padding co lại `p-6 md:p-10`, các lựa chọn
  xếp `grid` 1 cột tự nhiên theo chiều rộng card → không cần breakpoint
  riêng vì card đã tự thu nhỏ theo màn hình.

## 6. Section Bản đồ số — `showcase/_map.html`
**Trạng thái: ĐÃ ĐẠT.**
- Cả 3 kiểu (embed/image/geojson) đều dùng khối full-width bo góc, ảnh/iframe
  co theo `aspect-video` hoặc chiều rộng cha → không tràn ở mobile.
- Đã test cả 3 kiểu với dữ liệu demo thật (Task 5.1): embed dùng
  `maps.google.com/maps?q=...&output=embed`, image dùng ảnh placeholder,
  geojson dùng Leaflet + 1 marker demo — cả 3 hiển thị đúng, không lỗi JS.

## 7. Section Bộ hình ảnh (gallery) — `showcase/_gallery.html`
**Trạng thái: ĐÃ ĐẠT (đúng yêu cầu "co lại 2 cột" sẵn từ Task 3.7).**
- Grid `grid-cols-2 sm:grid-cols-3 lg:grid-cols-4` — mobile mặc định 2 cột
  đúng theo yêu cầu Task 5.2, không cần sửa thêm.
- Lightbox full-screen (`fixed inset-0`) hoạt động đúng ở mọi kích thước,
  nút điều hướng trước/sau không bị che ở màn hình hẹp.

## 8. Trang Giới thiệu — `pages/about.html`
**Trạng thái: ĐÃ ĐẠT.**
- Card Tầm nhìn/Sứ mệnh: `grid-cols-1 md:grid-cols-2`.
- Giá trị cốt lõi: `grid-cols-1 md:grid-cols-3`.
- Đội ngũ sáng lập: `grid-cols-2 md:grid-cols-4`, avatar co `w-28 h-28
  md:w-48 md:h-48` — không tràn ở mobile (2 cột), đủ rộng ở desktop (4 cột).

## 9. Trang Liên hệ — `pages/contact.html`
**Trạng thái: ĐÃ ĐẠT.**
- Layout chính `grid-cols-1 md:grid-cols-5` (2/5 thông tin liên hệ, 3/5
  form) → xếp chồng dọc hợp lý trên mobile, đúng tỉ lệ trên desktop.
- Input/textarea full-width (`w-full`) ở mọi kích thước, không tràn ngang.

## 10. Footer — `partials/footer.html`
**Trạng thái: ĐÃ ĐẠT.**
- `grid-cols-1 md:grid-cols-4`, cột logo chiếm `md:col-span-2` — xếp dọc
  gọn gàng trên mobile, cân đối trên desktop.

---

## Tổng kết
- **1 lỗi tìm thấy và đã sửa**: menu mobile không có cách mở (Global Nav) —
  đã thêm hamburger + panel (`nav-toggle`, `mobile-menu`, `static/js/navbar.js`).
- **Không phát hiện lỗi tràn ngang (horizontal overflow)** ở bất kỳ trang
  nào khi test 375px với dữ liệu demo thật (`seed_demo_data`).
- Các mục "ĐÃ ĐẠT" là do Nhóm 3 đã áp dụng breakpoint `md:`/`lg:` đúng
  ngay từ lúc dựng template — Task 5.2 xác nhận lại bằng test thực tế
  trên dữ liệu thật thay vì chỉ đọc code.
- Đã chạy `npm run build` sau khi sửa `navbar.html` + thêm `navbar.js`
  để `static/dist/output.css` có đủ class mới (`md:inline-flex`, các class
  trong `#mobile-menu`, v.v.).

## Cách người dùng tự kiểm tra lại
1. `npm run build` (đã build sẵn trong lần bàn giao này, chỉ cần chạy lại
   nếu sửa thêm class).
2. `python manage.py seed_demo_data` (nếu DB rỗng) rồi `runserver`.
3. Mở DevTools (F12) → Toggle device toolbar → thử 375px / 768px / 1280px
   ở cả 4 trang: `/`, `/bai-hoc/<slug>/`, `/gioi-thieu/`, `/lien-he/`.
4. Riêng Global Nav: thu nhỏ dưới 768px → phải thấy icon hamburger (☰) góc
   phải, bấm vào phải xổ ra menu dọc, bấm 1 link phải tự đóng menu lại.
