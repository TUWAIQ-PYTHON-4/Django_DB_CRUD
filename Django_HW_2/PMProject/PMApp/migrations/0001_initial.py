# Generated by Django 4.0.4 on 2022-05-24 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the project', max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='The creation time')),
                ('completion_time', models.DateTimeField(help_text='The completion time', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title', max_length=50)),
                ('description', models.TextField(help_text='The description')),
                ('time_estimate', models.IntegerField(help_text='the time estimate')),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
    ]
