# Generated by Django 3.0 on 2020-11-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20201104_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file_upload',
            field=models.BinaryField(blank=True, db_column='data'),
        ),
    ]