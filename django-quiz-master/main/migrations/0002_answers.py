# Generated by Django 3.2.9 on 2022-01-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_A', models.TextField(verbose_name='description')),
                ('answer_B', models.TextField(verbose_name='description')),
                ('answer_C', models.TextField(verbose_name='description')),
                ('answer_D', models.TextField(verbose_name='description')),
            ],
        ),
    ]
