# Generated by Django 4.2.5 on 2023-09-06 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailsendlog',
            options={'ordering': ['-creation_time'], 'verbose_name': '邮件发送log', 'verbose_name_plural': '邮件发送log'},
        ),
        migrations.RenameField(
            model_name='commands',
            old_name='created_time',
            new_name='creation_time',
        ),
        migrations.RenameField(
            model_name='commands',
            old_name='last_mod_time',
            new_name='last_modify_time',
        ),
        migrations.RenameField(
            model_name='emailsendlog',
            old_name='created_time',
            new_name='creation_time',
        ),
    ]
