from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='cover_image_url',
            field=models.URLField(
                blank=True,
                help_text='URL ảnh bìa công khai (Imgur, Cloudinary, Drive public...). Ưu tiên hơn file upload.',
            ),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='cover_image',
            field=models.ImageField(
                blank=True,
                help_text='Upload ảnh bìa (sẽ mất khi redeploy trên free tier). Ưu tiên dùng Cover image url bên dưới.',
                null=True,
                upload_to='lessons/covers/',
            ),
        ),
    ]
