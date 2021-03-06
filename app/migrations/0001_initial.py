# Generated by Django 4.0.3 on 2022-04-22 15:10

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car_detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="car", max_length=100)),
                ("price", models.CharField(max_length=100)),
                ("engine_type", models.CharField(max_length=100)),
                ("displacement", models.CharField(max_length=100)),
                ("cylinders", models.CharField(max_length=100)),
                ("max_power", models.CharField(max_length=100)),
                ("max_torque", models.CharField(max_length=100)),
                ("valve_per_cylinder", models.CharField(max_length=100)),
                ("valve_configuration", models.CharField(max_length=100)),
                ("fuel_system", models.CharField(max_length=100)),
                ("turbo_charger", models.CharField(max_length=100)),
                (
                    "transmission",
                    models.CharField(
                        choices=[
                            ("Automatic", "Automatic"),
                            ("Manual", "Manual"),
                            ("Semi-Automatic", "Semi-Automatic"),
                        ],
                        max_length=100,
                    ),
                ),
                ("gear_box", models.CharField(max_length=100)),
                ("drive_type", models.CharField(max_length=100)),
                (
                    "fuel_type",
                    models.CharField(
                        choices=[
                            ("petrol", "petrol"),
                            ("diesel", "diesel"),
                            ("CNG", "CNG"),
                            ("LPG", "LPG"),
                            ("Hybrid", "Hybrid"),
                            ("Electric", "Electric"),
                        ],
                        max_length=100,
                    ),
                ),
                ("emission", models.CharField(max_length=100)),
                ("milage", models.CharField(max_length=100)),
                ("front_suspension", models.CharField(max_length=100)),
                ("rear_suspension", models.CharField(max_length=100)),
                ("front_brakes", models.CharField(max_length=100)),
                ("rear_brakes", models.CharField(max_length=100)),
                ("steering_type", models.CharField(max_length=100)),
                ("steering_column", models.CharField(max_length=100)),
                ("steering_gear_type", models.CharField(max_length=100)),
                ("tyre_size", models.CharField(max_length=100)),
                ("tyre_type", models.CharField(max_length=100)),
                ("alloy_wheel_size", models.CharField(max_length=100)),
                ("fuel_capacity", models.CharField(max_length=100)),
                ("length", models.CharField(max_length=100)),
                ("width", models.CharField(max_length=100)),
                ("height", models.CharField(max_length=100)),
                ("wheelbase", models.CharField(max_length=100)),
                ("seating_capacity", models.CharField(max_length=100)),
                ("boot_space", models.CharField(max_length=100)),
                ("doors", models.IntegerField()),
                ("tachometer", models.BooleanField(default=True)),
                ("leather_seats", models.BooleanField(default=True)),
                ("leather_steering_wheel", models.BooleanField(default=True)),
                ("digitial_odometer", models.BooleanField(default=True)),
                ("ventilated_seats", models.BooleanField(default=True)),
                ("height_adjustable_seats", models.BooleanField(default=True)),
                ("additional_features", models.CharField(max_length=100)),
                ("power_steering", models.BooleanField(default=True)),
                ("power_boot", models.BooleanField(default=True)),
                ("automatic_climate_control", models.BooleanField(default=True)),
                ("air_quality_control", models.BooleanField(default=True)),
                ("rear_ac_vents", models.BooleanField(default=True)),
                ("rear_ac_vents_desc", models.CharField(max_length=100)),
                ("engine_start_stop", models.BooleanField(default=True)),
                ("usb_charger", models.CharField(max_length=100)),
                ("cruise_control", models.BooleanField(default=True)),
                ("parking_sensor", models.CharField(max_length=100)),
                (
                    "additional_features2",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                (
                    "available_color",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                ("adjustable_headlights", models.BooleanField(default=True)),
                ("fog_lights", models.BooleanField(default=True)),
                ("rear_window_wiper", models.BooleanField(default=True)),
                ("alloy_wheel", models.BooleanField(default=True)),
                ("sunroof", models.BooleanField(default=True)),
                ("led_DRLS", models.BooleanField(default=True)),
                ("led_headlights", models.BooleanField(default=True)),
                ("lead_taillights", models.BooleanField(default=True)),
                (
                    "additional_features3",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                ("anti_lock_braking_system", models.BooleanField(default=True)),
                ("central_locking", models.BooleanField(default=True)),
                ("power_door_locks", models.BooleanField(default=True)),
                ("child_safety_locks", models.BooleanField(default=True)),
                ("airbag", models.IntegerField()),
                ("seat_belt_warning", models.BooleanField(default=True)),
                ("hill_assist", models.BooleanField(default=True)),
                ("head_up_display", models.BooleanField(default=True)),
                (
                    "additional_features4",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                ("pros", django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text")),
                ("cons", django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text")),
            ],
        ),
        migrations.CreateModel(
            name="Consult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("budget", models.CharField(max_length=100)),
                ("average_travel", models.CharField(max_length=100)),
                ("number_of_people_traveling", models.CharField(max_length=100)),
                ("road_type", models.CharField(max_length=100)),
                ("first_priority", models.CharField(max_length=100)),
                ("second_priority", models.CharField(max_length=100)),
                ("third_priority", models.CharField(max_length=100)),
                ("cars_shortlisted", models.CharField(max_length=200)),
                ("message", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Contact_Detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("message", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Market_News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(default=" ", max_length=1000)),
                ("image", models.ImageField(upload_to="thumbnails/")),
            ],
        ),
        migrations.CreateModel(
            name="Most_popular",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="thumbnails/")),
            ],
        ),
        migrations.CreateModel(
            name="Recent_News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=200)),
                (
                    "full_description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                ("image", models.ImageField(upload_to="thumbnails/")),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("thumbnail", models.ImageField(upload_to="thumbnails/")),
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                (
                    "interior",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                (
                    "interior_image",
                    models.ImageField(blank=True, null=True, upload_to="cars/"),
                ),
                (
                    "exterior",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                (
                    "exterior_image",
                    models.ImageField(blank=True, null=True, upload_to="cars/"),
                ),
                (
                    "engine_performance",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                (
                    "engine_performance_image",
                    models.ImageField(blank=True, null=True, upload_to="cars/"),
                ),
                (
                    "drivequality_safety",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                (
                    "drivequality_safety_image",
                    models.ImageField(blank=True, null=True, upload_to="cars/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Second_Hand_Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("seller_name", models.CharField(max_length=100)),
                ("number", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("carname", models.CharField(max_length=100)),
                ("price", models.CharField(max_length=100)),
                ("make_year", models.CharField(max_length=100)),
                ("running", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=100)),
                ("engine", models.CharField(max_length=100)),
                ("transmission", models.CharField(max_length=100)),
                ("fuel", models.CharField(max_length=100)),
                ("features", models.TextField(max_length=1000)),
                ("front", models.ImageField(upload_to="cars/")),
                ("rear", models.ImageField(upload_to="cars/")),
                ("side", models.ImageField(upload_to="cars/")),
                ("interior", models.ImageField(upload_to="cars/")),
                ("approve_status", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Comparision",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="thumbnails/"),
                ),
                ("vs_image", models.ImageField(default="", upload_to="pictures/")),
                ("name", models.CharField(max_length=100)),
                (
                    "first_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="first_car",
                        to="app.car_detail",
                    ),
                ),
                (
                    "second_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="second_car",
                        to="app.car_detail",
                    ),
                ),
            ],
        ),
    ]
