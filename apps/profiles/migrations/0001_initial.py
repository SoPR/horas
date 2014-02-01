# encoding: utf8
from django.db import models, migrations
import django.core.validators
import apps.profiles.fields
import django.utils.timezone


class Migration(migrations.Migration):
    
    dependencies = [
        ('auth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bio', models.TextField()),
                ('twitter_username', models.CharField(blank=True, max_length=50)),
                ('facebook_username', models.CharField(blank=True, max_length=50)),
                ('github_username', models.CharField(blank=True, max_length=50)),
                ('website_url', models.URLField(blank=True, max_length=50)),
                ('day_of_week', apps.profiles.fields.DaysOfWeekField(max_length=1, blank=True, db_index=True, choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('skype', models.CharField(blank=True, max_length=50)),
                ('google', models.CharField(blank=True, max_length=50)),
                ('jitsi', models.CharField(blank=True, max_length=50)),
                ('address', models.TextField(blank=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=(models.Model,),
        ),
    ]
