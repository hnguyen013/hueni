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
    cover_image = models.ImageField(upload_to='lessons/covers/')
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
        # Task 4.1 sẽ đăng ký route 'timeline:lesson_detail' tương ứng.
        # Dùng path tĩnh ở đây để model không phụ thuộc vào urls.py (chưa có ở task này).
        return f'/bai-hoc/{self.slug}/'
