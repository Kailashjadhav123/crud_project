# Generated by Django 4.2.2 on 2023-09-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_student_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='code',
            field=models.CharField(default='Code1', max_length=100),
        ),
    ]
