# Generated by Django 3.2.6 on 2021-12-30 21:46

import accounts.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': '同じユーザー名が既に登録済みです。'}, help_text='この項目は必須です。半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('first_name', models.CharField(max_length=30, verbose_name='姓')),
                ('last_name', models.CharField(max_length=30, verbose_name='名')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='入会日')),
                ('description', models.TextField(blank=True, default='', verbose_name='自己紹介')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='プロフィール画像')),
                ('is_staff', models.BooleanField(default=False, help_text='ユーザーが管理サイトにログイン可能かどうかを示します。', verbose_name='スタッフ権限')),
                ('is_active', models.BooleanField(default=True, help_text='ユーザーがアクティブかどうかを示します。アカウントを削除する代わりに選択を解除してください。', verbose_name='有効')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
