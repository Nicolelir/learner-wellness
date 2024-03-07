# Generated by Django 4.2.10 on 2024-03-06 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0002_therapist_rename_user_booking_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('physical', 'Physical Wellness Appointment'), ('mental', 'Mental Health Appointment')], max_length=50)),
                ('startTime', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_client', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_status', to=settings.AUTH_USER_MODEL)),
                ('therapist', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sessions_as_therapist', to='bookings.therapist')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
