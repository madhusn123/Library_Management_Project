# Generated by Django 3.1.1 on 2023-01-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0006_student_stud_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_password',
            field=models.CharField(max_length=50),
        ),
    ]