# Generated by Django 4.2.1 on 2023-05-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FabricaNeeds', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurrencyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'RecurrencyTypes',
            },
        ),
    ]