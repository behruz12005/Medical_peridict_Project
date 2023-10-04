# Generated by Django 4.2.1 on 2023-10-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyzResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('buying', models.IntegerField()),
                ('systolic_blood_pressure', models.IntegerField()),
                ('total_cholesterol', models.IntegerField()),
                ('hdl_cholesterol', models.IntegerField()),
                ('on_blood_pressure_medication', models.CharField(max_length=10)),
                ('cigarette_smoker', models.CharField(max_length=10)),
                ('diabetes_present', models.CharField(max_length=10)),
                ('predict', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='file/')),
            ],
        ),
    ]
