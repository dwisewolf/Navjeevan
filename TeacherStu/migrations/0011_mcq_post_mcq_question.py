# Generated by Django 2.1.5 on 2020-07-15 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStu', '0010_auto_20200709_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('school', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('clas', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MCQ_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que_title', models.CharField(max_length=50)),
                ('choice_1', models.CharField(max_length=50)),
                ('choice_2', models.CharField(max_length=50)),
                ('choice_3', models.CharField(max_length=50)),
                ('choice_4', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('MCQPost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Quiz_Topic', to='TeacherStu.MCQ_Post')),
            ],
        ),
    ]
