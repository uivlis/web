# -*- coding: utf-8 -*-
# Generated by Django 2.0.7 on 2018-07-30 20:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avatar', '0003_auto_20180903_2005'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('taggit', '0002_auto_20150616_2121'),
        ('dashboard', '0110_profile_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('email', models.CharField(blank=True, max_length=200, verbose_name='Email')),
                ('gh_repos_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='Repository Data')),
                ('gh_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='Github Data')),
                ('gh_members', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], help_text='comma delimited', size=None, verbose_name='Github Members')),
                ('gh_admins', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], help_text='comma delimited', size=None, verbose_name='Github Administrators')),
                ('github_bot_enabled', models.BooleanField(default=True, verbose_name='Is Github Bot Enabled?')),
                ('github_username', models.CharField(blank=True, max_length=80, verbose_name='Github Username')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Is Visible?')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=80, populate_from='name', verbose_name='Slug')),
                ('website_url', models.URLField(blank=True, verbose_name='Website')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('admins', models.ManyToManyField(related_name='organizations_owned', to=settings.AUTH_USER_MODEL, verbose_name='Administrators')),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avatar.Avatar', verbose_name='Avatar')),
                ('followers', models.ManyToManyField(related_name='organizations_following', to='dashboard.Profile', verbose_name='Followers')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='organization_tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
