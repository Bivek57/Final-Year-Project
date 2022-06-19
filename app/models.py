from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField


class Consult(models.Model):
    """Consult us form details"""

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    average_travel = models.CharField(max_length=100)
    number_of_people_traveling = models.CharField(max_length=100)
    road_type = models.CharField(max_length=100)
    first_priority = models.CharField(max_length=100)
    second_priority = models.CharField(max_length=100)
    third_priority = models.CharField(max_length=100)
    cars_shortlisted = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name 


class Recent_News(models.Model):
    """
    Recent News of home page in corousel
    """

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    full_description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="thumbnails/")
    # newslink = models.URLField(max_length=200, default=" ")

    def __str__(self):
        return self.title


class Market_News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=" ")
    image = models.ImageField(upload_to="thumbnails/")

    def __str__(self):
        return self.title


class Most_popular(models.Model):
    """Most popular car in home page below corousel"""

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="thumbnails/")
    url = models.URLField(max_length=1000, default=" ")

    def __str__(self):
        return self.title


class Second_Hand_Car(models.Model):
    """Second hand car"""

    id = models.BigAutoField(
        primary_key=True,
        editable=False,
        unique=True,
    )
    seller_name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    carname = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    make_year = models.CharField(max_length=100)
    running = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    features = models.TextField(max_length=1000)
    front = models.ImageField(upload_to="cars/")
    rear = models.ImageField(upload_to="cars/")
    side = models.ImageField(upload_to="cars/")
    interior = models.ImageField(upload_to="cars/")
    # add  approved status
    approve_status = models.BooleanField(default=False)

    def __str__(self):
        return str(f"{self.carname}|{self.seller_name}")


class Contact_Detail(models.Model):
    """Contact us form details"""

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    """Reviews of each cars for detail page"""

    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    description = RichTextField(blank=True, null=True)
    interior = RichTextField(blank=True, null=True)
    interior_image = models.ImageField(upload_to="cars/", blank=True, null=True)
    exterior = RichTextField(blank=True, null=True)
    exterior_image = models.ImageField(upload_to="cars/", blank=True, null=True)
    engine_performance = RichTextField(blank=True, null=True)
    engine_performance_image = models.ImageField(
        upload_to="cars/", blank=True, null=True
    )
    drivequality_safety = RichTextField(blank=True, null=True)
    drivequality_safety_image = models.ImageField(
        upload_to="cars/", blank=True, null=True
    )
    conclusion = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Car_detail(models.Model):
    # basic info
    name = models.CharField(max_length=100, default="car")
    price = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    displacement = models.CharField(max_length=100)
    cylinders = models.CharField(max_length=100)
    max_power = models.CharField(max_length=100)
    max_torque = models.CharField(max_length=100)
    valve_per_cylinder = models.CharField(max_length=100)
    valve_configuration = models.CharField(max_length=100)
    fuel_system = models.CharField(max_length=100)
    turbo_charger = models.CharField(max_length=100)
    # make a choices for transmission type
    TRANSMISSION = [
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
        ("Semi-Automatic", "Semi-Automatic"),
    ]

    transmission = models.CharField(max_length=100, choices=TRANSMISSION)
    gear_box = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=100)
    # make choice for fuel type
    FUEL = [
        ("petrol", "petrol"),
        ("diesel", "diesel"),
        ("CNG", "CNG"),
        ("LPG", "LPG"),
        ("Hybrid", "Hybrid"),
        ("Electric", "Electric"),
    ]

    fuel_type = models.CharField(choices=FUEL, max_length=100)
    emission = models.CharField(max_length=100)
    milage = models.CharField(max_length=100)
    # Suspensions, steering and brakes
    front_suspension = models.CharField(max_length=100)
    rear_suspension = models.CharField(max_length=100)
    front_brakes = models.CharField(max_length=100)
    rear_brakes = models.CharField(max_length=100)
    steering_type = models.CharField(max_length=100)
    steering_column = models.CharField(max_length=100)
    steering_gear_type = models.CharField(max_length=100)
    tyre_size = models.CharField(max_length=100)
    tyre_type = models.CharField(max_length=100)
    alloy_wheel_size = models.CharField(max_length=100)
    fuel_capacity = models.CharField(max_length=100)
    # dimensions and capacity
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    wheelbase = models.CharField(max_length=100)
    seating_capacity = models.CharField(max_length=100)
    boot_space = models.CharField(max_length=100)
    doors = models.IntegerField()
    # interior
    tachometer = models.BooleanField(default=True)
    leather_seats = models.BooleanField(default=True)
    leather_steering_wheel = models.BooleanField(default=True)
    digitial_odometer = models.BooleanField(default=True)
    ventilated_seats = models.BooleanField(default=True)
    height_adjustable_seats = models.BooleanField(default=True)
    additional_features = models.CharField(max_length=100)
    # comfort and conveience
    power_steering = models.BooleanField(default=True)
    power_boot = models.BooleanField(default=True)
    automatic_climate_control = models.BooleanField(default=True)
    air_quality_control = models.BooleanField(default=True)
    rear_ac_vents = models.BooleanField(default=True)
    rear_ac_vents_desc = models.CharField(max_length=100)
    engine_start_stop = models.BooleanField(default=True)
    usb_charger = models.CharField(max_length=100)
    cruise_control = models.BooleanField(default=True)
    parking_sensor = models.CharField(max_length=100)
    additional_features2 = RichTextField(blank=True, null=True)
    available_color = RichTextField(blank=True, null=True)
    adjustable_headlights = models.BooleanField(default=True)
    fog_lights = models.BooleanField(default=True)
    rear_window_wiper = models.BooleanField(default=True)
    alloy_wheel = models.BooleanField(default=True)
    sunroof = models.BooleanField(default=True)
    led_DRLS = models.BooleanField(default=True)
    led_headlights = models.BooleanField(default=True)
    lead_taillights = models.BooleanField(default=True)
    additional_features3 = RichTextField(blank=True, null=True)
    # safety and comfort
    anti_lock_braking_system = models.BooleanField(default=True)
    central_locking = models.BooleanField(default=True)
    power_door_locks = models.BooleanField(default=True)
    child_safety_locks = models.BooleanField(default=True)
    airbag = models.IntegerField()
    seat_belt_warning = models.BooleanField(default=True)
    hill_assist = models.BooleanField(default=True)
    head_up_display = models.BooleanField(default=True)
    additional_features4 = RichTextField(blank=True, null=True)
    pros = RichTextField(blank=True, null=True)
    cons = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comparision(models.Model):
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True,
    )
    vs_image = models.ImageField(upload_to="pictures/", default="")
    name = models.CharField(max_length=100)
    first_car = models.ForeignKey(
        Car_detail, on_delete=models.CASCADE, related_name="first_car"
    )
    second_car = models.ForeignKey(
        Car_detail, on_delete=models.CASCADE, related_name="second_car"
    )

    def __str__(self):
        return f"{self.first_car} vs {self.second_car}"
