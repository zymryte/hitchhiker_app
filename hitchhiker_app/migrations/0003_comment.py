# Generated by Django 2.2 on 2020-07-21 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hitchhiker_app', '0002_trip_reserve_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='hitchhiker_app.User')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='hitchhiker_app.Trip')),
            ],
        ),
    ]
