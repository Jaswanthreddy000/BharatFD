# Generated by Django 5.1.5 on 2025-02-01 22:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_te',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_te',
            field=models.TextField(blank=True, null=True),
        ),
    ]
