# Generated by Django 4.2.3 on 2023-08-01 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_username_alter_userprofile_email'),
        ('memes', '0006_alter_meme_meme_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.userprofile'),
        ),
    ]
