# Generated by Django 3.1.1 on 2023-01-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0002_auto_20230118_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_password',
            field=models.CharField(max_length=50),
        ),
    ]