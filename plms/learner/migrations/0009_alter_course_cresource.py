# Generated by Django 4.0.6 on 2022-07-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0008_alter_course_cresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cresource',
            field=models.FileField(blank=True, default='', upload_to='media/'),
        ),
    ]
