# Generated by Django 5.0.3 on 2024-04-01 18:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Chat Sessions',
            },
        ),
        migrations.CreateModel(
            name='Chat_Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=256)),
                ('response', models.CharField(max_length=256)),
                ('user_feedback', models.BooleanField(blank=True, default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.chat_session')),
            ],
            options={
                'verbose_name_plural': 'Chat Messages',
            },
        ),
    ]
