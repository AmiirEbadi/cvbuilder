# Generated by Django 4.1 on 2022-09-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_github_alter_user_linkedin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(default='ok'),
            preserve_default=False,
        ),
    ]
