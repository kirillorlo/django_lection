# Generated by Django 5.0.3 on 2024-03-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinFlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('heads', 'Орёл'), ('tails', 'Решка')], max_length=5)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]
