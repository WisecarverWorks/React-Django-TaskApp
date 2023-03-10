# Generated by Django 4.1.7 on 2023-02-15 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('description', models.TextField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='images/', verbose_name='Image')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]
