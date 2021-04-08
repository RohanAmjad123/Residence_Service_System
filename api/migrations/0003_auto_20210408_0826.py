# Generated by Django 3.1.7 on 2021-04-08 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210406_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('IN PROGRESS', 'IN PROGRESS'), ('UNRESOLVED', 'UNRESOLVED')], default='UNRESOLVED', max_length=20),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='urgency_rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='fulfills',
            name='status',
            field=models.CharField(choices=[('FULFILLED', 'FULFILLED'), ('IN PROGRESS', 'IN PROGRESS')], default='IN PROGRESS', max_length=20),
        ),
        migrations.AlterField(
            model_name='resolves',
            name='status',
            field=models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('IN PROGRESS', 'IN PROGRESS')], default='IN PROGRESS', max_length=50),
        ),
        migrations.AlterField(
            model_name='resolves',
            name='technician_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.technician'),
        ),
        migrations.AlterField(
            model_name='resolves',
            name='urgency_rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20),
        ),
    ]
