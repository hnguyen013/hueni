from django.db import models


class TeamMember(models.Model):
    """Thành viên đội ngũ sáng lập, hiển thị ở section 'Đội ngũ sáng lập' trang Giới thiệu."""

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(
        upload_to='team/avatars/', blank=True, null=True,
        help_text='Ảnh chân dung, hiển thị avatar tròn grayscale.',
    )
    bio = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(
        default=True, help_text='Bỏ chọn để ẩn thành viên khỏi trang Giới thiệu.'
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name


class SiteContent(models.Model):
    """
    Khối nội dung tĩnh có thể chỉnh sửa qua admin, dùng cho các section
    không có model riêng: Hero, Tầm nhìn/Sứ mệnh, Giá trị cốt lõi (trang
    Giới thiệu), thông tin liên hệ (trang Liên hệ), ...

    Mỗi bản ghi là 1 khối nội dung, phân loại theo `section`, sắp xếp theo
    `order`. Ví dụ: 3 bản ghi section='about_value' -> 3 cột Giá trị cốt lõi.
    """

    class Section(models.TextChoices):
        ABOUT_HERO = 'about_hero', 'Giới thiệu - Hero'
        ABOUT_VISION = 'about_vision', 'Giới thiệu - Tầm nhìn'
        ABOUT_MISSION = 'about_mission', 'Giới thiệu - Sứ mệnh'
        ABOUT_VALUE = 'about_value', 'Giới thiệu - Giá trị cốt lõi'
        CONTACT_INFO = 'contact_info', 'Liên hệ - Thông tin'
        GENERAL = 'general', 'Khác'

    key = models.SlugField(
        unique=True,
        help_text="Định danh duy nhất để gọi trong template, vd: 'about-hero', 'value-1'.",
    )
    section = models.CharField(
        max_length=30, choices=Section.choices, default=Section.GENERAL
    )
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='pages/site_content/', blank=True, null=True)
    icon = models.CharField(
        max_length=100, blank=True,
        help_text='Tên icon (vd cho Giá trị cốt lõi), tuỳ chọn.',
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['section', 'order', 'id']
        verbose_name = 'Site Content'
        verbose_name_plural = 'Site Contents'

    def __str__(self):
        return f'[{self.get_section_display()}] {self.title or self.key}'
