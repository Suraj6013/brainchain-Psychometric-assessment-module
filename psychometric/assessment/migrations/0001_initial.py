# Generated by Django 5.0.7 on 2024-07-23 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('question_type', models.CharField(choices=[('MCQ', 'Multiple Choice'), ('LIKERT', 'Likert Scale'), ('RATING', 'Rating Scale'), ('TRUE_FALSE', 'True/False'), ('RANKING', 'Ranking'), ('OPEN_ENDED', 'Open-Ended'), ('SEMANTIC', 'Semantic Differential'), ('CHECKLIST', 'Checklist'), ('BINARY', 'Binary')], max_length=50)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='assessment.assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='assessment.question')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_response', models.TextField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.question')),
                ('selected_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.option')),
            ],
        ),
    ]
