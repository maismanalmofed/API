# Generated by Django 5.0.2 on 2024-02-20 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_rating_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together=set(),
        ),
        migrations.AddField(
            model_name='rating',
            name='customer',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('customer', 'restaurant')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('customer', 'restaurant')},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]
