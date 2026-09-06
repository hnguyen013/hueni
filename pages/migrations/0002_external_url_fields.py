from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='avatar_url',
            field=models.URLField(
                blank=True,
                help_text='URL ảnh avatar công khai — ưu tiên hơn file upload.',
            ),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='avatar',
            field=models.ImageField(
                blank=True,
                help_text='Upload avatar (sẽ mất khi redeploy). Ưu tiên Avatar url.',
                null=True,
                upload_to='team/avatars/',
            ),
        ),
        migrations.AddField(
            model_name='sitecontent',
            name='image_url',
            field=models.URLField(
                blank=True,
                help_text='URL ảnh công khai — ưu tiên hơn file upload.',
            ),
        ),
        migrations.AlterField(
            model_name='sitecontent',
            name='image',
            field=models.ImageField(
                blank=True,
                help_text='Upload ảnh (sẽ mất khi redeploy). Ưu tiên Image url.',
                null=True,
                upload_to='pages/site_content/',
            ),
        ),
    ]
