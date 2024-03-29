# Generated by Django 4.0.5 on 2022-12-15 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_useravatar_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='useravatar',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='useravatar',
            name='user',
        ),
        migrations.AddField(
            model_name='useravatar',
            name='userimage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.avatar'),
        ),
    ]
