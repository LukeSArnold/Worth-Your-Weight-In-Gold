# Generated by Django 4.1.2 on 2022-11-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pound_to_troy', models.FloatField()),
                ('pound_to_ton', models.FloatField()),
                ('pound_to_gram', models.FloatField()),
                ('pound_to_kilogram', models.FloatField()),
                ('pound_to_ounce', models.FloatField()),
            ],
        ),
    ]
