# Generated by Django 2.0.6 on 2018-06-26 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Developer'),
        ),
    ]
