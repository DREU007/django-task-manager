# Generated by Django 4.2.6 on 2023-11-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'Task status with such Name already exist.'}, help_text='Required 255 characters or fewer.', max_length=255, unique=True, verbose_name='name')),
                ('task', models.ManyToManyField(to='task.task')),
            ],
        ),
    ]