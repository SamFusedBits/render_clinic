# Generated by Django 5.0.6 on 2024-07-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('working', models.CharField(max_length=5)),
                ('work_shift', models.CharField(max_length=20)),
                ('job_nature', models.CharField(max_length=20)),
                ('lift_heavy_weights', models.CharField(max_length=5)),
                ('use_devices_often', models.CharField(max_length=10)),
                ('sitting_hours', models.CharField(max_length=20)),
                ('fast_food_frequency', models.CharField(max_length=20)),
                ('consume_oily_spicy_food', models.CharField(max_length=5)),
                ('dinner_time', models.CharField(max_length=20)),
                ('digestion_problems', models.CharField(max_length=5)),
                ('stool_frequency', models.CharField(max_length=20)),
                ('buttock_pain', models.CharField(max_length=20)),
                ('cutting_pain', models.CharField(max_length=5)),
                ('burning_sensation', models.CharField(max_length=5)),
                ('itching', models.CharField(max_length=5)),
                ('pile_mass_coming_out', models.CharField(max_length=5)),
                ('pile_mass_condition', models.CharField(max_length=30)),
                ('bleeding_issue', models.CharField(max_length=5)),
                ('bleeding_type', models.CharField(max_length=30)),
                ('bleeding_amount', models.CharField(max_length=30)),
                ('blood_color', models.CharField(max_length=10)),
                ('pus_discharge', models.CharField(max_length=5)),
                ('boils_around_anus', models.CharField(max_length=5)),
                ('anus_swelling', models.CharField(max_length=5)),
                ('first_time_swelling', models.CharField(max_length=5)),
                ('body_hair_type', models.CharField(max_length=30)),
                ('diabetes', models.CharField(max_length=5)),
                ('redness_swelling', models.CharField(max_length=5)),
                ('treatment_type', models.CharField(max_length=20)),
                ('treatment_kind', models.CharField(max_length=30)),
                ('blood_color_during_treatment', models.CharField(max_length=5)),
                ('recurrence', models.CharField(max_length=5)),
                ('relapse_frequency', models.CharField(max_length=30)),
                ('pain_while_sitting', models.CharField(max_length=5)),
                ('pain_while_defecation', models.CharField(max_length=5)),
                ('weight_loss', models.CharField(max_length=5)),
                ('just_delivered_baby', models.CharField(max_length=30)),
                ('family_anal_cancer', models.CharField(max_length=5)),
                ('first_time_doctor_visit', models.CharField(max_length=5)),
            ],
        ),
    ]
