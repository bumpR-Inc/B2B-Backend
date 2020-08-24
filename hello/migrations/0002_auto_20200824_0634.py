# Generated by Django 2.1.4 on 2020-08-24 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryMade', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('foodItem', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hello.FoodItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='deliveryMade',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='foodItem',
        ),
        migrations.AddField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferences_of_user', to='hello.Profile'),
        ),
    ]