# Generated by Django 4.1 on 2022-08-31 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_chef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]