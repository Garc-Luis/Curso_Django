# Generated by Django 4.0.4 on 2023-04-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateField(null=True),
        ),
    ]