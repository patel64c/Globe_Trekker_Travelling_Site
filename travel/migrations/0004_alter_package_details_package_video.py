# Generated by Django 4.1.4 on 2022-12-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_alter_package_details_package_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_details',
            name='package_video',
            field=models.FileField(upload_to='videos'),
        ),
    ]
