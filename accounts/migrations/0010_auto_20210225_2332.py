# Generated by Django 3.1.7 on 2021-02-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210225_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='localgovunit',
            name='lgu_detail_avatar',
            field=models.ImageField(blank=True, upload_to='lgu_detail_avatar'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=50, null=True),
        ),
    ]