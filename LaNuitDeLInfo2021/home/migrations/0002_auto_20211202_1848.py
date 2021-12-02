# Generated by Django 3.2.9 on 2021-12-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescue',
            name='lifeguard',
            field=models.ManyToManyField(blank=True, related_name='rescues', to='home.Person'),
        ),
        migrations.AddField(
            model_name='rescue',
            name='rescued',
            field=models.ManyToManyField(blank=True, related_name='distresses', to='home.Person'),
        ),
    ]
