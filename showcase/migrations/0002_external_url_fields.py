from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='preview_image_url',
            field=models.URLField(
                blank=True,
                help_text='URL ảnh xem trước công khai — ưu tiên hơn file upload.',
            ),
        ),
        migrations.AddField(
            model_name='worksheet',
            name='file_url',
            field=models.URLField(
                blank=True,
                help_text='URL file tải về (Google Drive public, Dropbox...). Ưu tiên hơn file upload.',
            ),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='file',
            field=models.FileField(
                blank=True,
                help_text='Upload file phiếu (sẽ mất khi redeploy). Ưu tiên File url.',
                null=True,
                upload_to='worksheets/files/',
            ),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='preview_image',
            field=models.ImageField(
                blank=True,
                help_text='Upload ảnh xem trước (sẽ mất khi redeploy). Ưu tiên Preview image url.',
                null=True,
                upload_to='worksheets/previews/',
            ),
        ),
        migrations.AddField(
            model_name='digitalmap',
            name='image_url',
            field=models.URLField(
                blank=True,
                help_text="URL ảnh bản đồ công khai — dùng khi map_type = 'image'.",
            ),
        ),
        migrations.AlterField(
            model_name='digitalmap',
            name='image',
            field=models.ImageField(
                blank=True,
                help_text='Upload ảnh bản đồ (sẽ mất khi redeploy). Ưu tiên Image url.',
                null=True,
                upload_to='maps/images/',
            ),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='image_url',
            field=models.URLField(
                blank=True,
                help_text='URL ảnh công khai — ưu tiên hơn file upload.',
            ),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(
                blank=True,
                help_text='Upload ảnh (sẽ mất khi redeploy). Ưu tiên Image url.',
                null=True,
                upload_to='galleries/images/',
            ),
        ),
    ]
