# Generated by Django 4.2.4 on 2023-08-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoredTemplate',
            fields=[
                ('template_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('content', models.TextField(max_length=1048)),
            ],
        ),
    ]
