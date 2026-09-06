from django.db import models


class Era(models.Model):
    """Một giai đoạn/thời kỳ trong dòng thời gian, chứa nhiều Lesson bên trong."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    year_label = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Era'
        verbose_name_plural = 'Eras'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Một bài học thuộc về một Era, hiển thị trong dòng thời gian và trang chi tiết."""

    era = models.ForeignKey(Era, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    year_label = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    # Upload file (sẽ mất trên Render free) HOẶC dán URL ảnh ngoài (bền vững).
    cover_image = models.ImageField(
        upload_to='lessons/covers/', blank=True, null=True,
        help_text='Upload ảnh bìa (sẽ mất khi redeploy trên free tier). Ưu tiên dùng Cover image url bên dưới.',
    )
    cover_image_url = models.URLField(
        blank=True,
        help_text='URL ảnh bìa công khai (Imgur, Cloudinary, Drive public...). Ưu tiên hơn file upload.',
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/bai-hoc/{self.slug}/'

    @property
    def cover_image_src(self):
        """URL ảnh bìa: ưu tiên cover_image_url, fallback file upload."""
        if self.cover_image_url:
            return self.cover_image_url
        if self.cover_image:
            try:
                return self.cover_image.url
            except ValueError:
                return ''
        return ''
