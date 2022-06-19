from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.conf import settings
from .mailer import mail_system
from .models import (Comparision, Consult, Contact_Detail, Market_News,
                     Most_popular, Recent_News, Reviews, Second_Hand_Car)


def home(request):
    # views to display the home page
    recent_news = Recent_News.objects.all()
    # get all recently added 3 most_popular
    most_popular = Most_popular.objects.all().order_by("-id")[:3]
    return render(
        request,
        "frontend/home.html",
        {"recent_news": recent_news, "most_popular": most_popular},
    )


def car_consultancy(request):
    # views to display the car consultancy page
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        budget = request.POST.get("budget")
        average_travel = request.POST.get("average_travel")
        number_of_people_traveling = request.POST.get("number_of_people_traveling")
        road_type = request.POST.get("road_type")
        first_priority = request.POST.get("first_priority")
        second_priority = request.POST.get("second_priority")
        third_priority = request.POST.get("third_priority")
        cars_shortlisted = request.POST.get("cars_shortlisted")
        message = request.POST.get("message")
        consult = Consult(
            name=name,
            phone=phone,
            email=email,
            address=address,
            budget=budget,
            average_travel=average_travel,
            number_of_people_traveling=number_of_people_traveling,
            road_type=road_type,
            first_priority=first_priority,
            second_priority=second_priority,
            third_priority=third_priority,
            cars_shortlisted=cars_shortlisted,
            message=message,
        )
        consult.save()

        # sending data to the admin mail
        mail_system(
            "New Consult",
            "mailtemp/mail.html",
            {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address,
                "budget": budget,
                "average_travel": average_travel,
                "number_of_people_traveling": number_of_people_traveling,
                "road_type": road_type,
                "first_priority": first_priority,
                "second_priority": second_priority,
                "third_priority": third_priority,
                "cars_shortlisted": cars_shortlisted,
                "message": message,
            },
            param_user_mail=settings.USER_MAIL, 
        )
        messages.add_message(request, messages.INFO, "Your Form has been sent")

        # redirect to "car_consultancy"
        return redirect("car_consultancy")

    return render(request, "frontend/consultancy.html")


def comparision(request):
    # views to display the car comparision page
    comparision = Comparision.objects.all().order_by("-id")[:12]
    # get first car field from model
    return render(request, "frontend/comparison.html", {"comparisions": comparision})
    # get comparision detail through name


def load_all_comp(request):
    comparision = Comparision.objects.all()
    return render(request, "frontend/comparison.html", {"comparisions": comparision})


def comparison_details(request, name):
    # views to display the car detail page
    comparison_detail = Comparision.objects.get(name=name)

    return render(
        request,
        "frontend/comparisiondetails.html",
        {"comparision_detail": comparison_detail},
    )


def reviews(request):
    # views to display the reviews page
    # get only 12 reviews from model
    reviews = Reviews.objects.all().order_by("-id")[:12]
    return render(request, "frontend/reviews.html", {"reviews": reviews})


def all_reviews(request):
    # views to display all reviews page
    reviews = Reviews.objects.all()
    return render(request, "frontend/reviews.html", {"reviews": reviews})


def reviews_details(request, name):
    # views to display the reviews details page
    review_detail = Reviews.objects.get(name=name)
    return render(request, "frontend/reviewsdetails.html", {"reviews": review_detail})


def market(request):
    # views to display the market page
    second_hand_car = Second_Hand_Car.objects.filter(approve_status=True).order_by(
        "-id"
    )[:12]
    return render(request, "frontend/secondhand.html", {"shc": second_hand_car})


def load_all_market(request):
    # views to display the market page
    # get second hand car by approve_status status true
    second_hand_car = Second_Hand_Car.objects.filter(approve_status=True)
    return render(request, "frontend/secondhand.html", {"shc": second_hand_car})


def contact(request):
    # views to take input from form and send the mail to the admin
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        message = request.POST.get("message")
        mail_system(
            f"{name} has contacted you",
            "mailtemp/contactmail.html",
            {
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "message": message,
            },
            param_user_mail="bivekpokhrel19@gmail.com",
        )
        contact = Contact_Detail(
            name=name,
            phone=phone,
            email=email,
            address=address,
            message=message,
        )
        # saving the data to the database
        contact.save()
        messages.add_message(request, messages.INFO, "Your Form has been sent")
        return redirect("home")
    return render(request, "frontend/contact.html")


def recent_news_details(request, news_title):
    # views to display the recent news details page
    recent_detail_news = Recent_News.objects.get(title=news_title)

    return render(
        request, "frontend/newsdetails.html", {"news_details": recent_detail_news}
    )


@login_required()
def post_your_car(request):
    # views to display the post your car page
    if request.method == "POST":
        seller_name = request.POST.get("seller")
        number = request.POST.get("number")
        location = request.POST.get("location")
        carname = request.POST.get("carname")
        price = request.POST.get("price")
        make_year = request.POST.get("year")
        running = request.POST.get("running")
        model = request.POST.get("model")
        color = request.POST.get("color")
        engine = request.POST.get("engine")
        transmission = request.POST.get("transmission")
        fuel = request.POST.get("fuel")
        features = request.POST.get("features")
        front = request.FILES["front"]
        rear = request.FILES["rear"]
        side = request.FILES["side"]
        interior = request.FILES["interior"]

        second_hand_car = Second_Hand_Car(
            seller_name=seller_name,
            number=number,
            location=location,
            carname=carname,
            price=price,
            make_year=make_year,
            running=running,
            model=model,
            color=color,
            engine=engine,
            transmission=transmission,
            fuel=fuel,
            features=features,
            front=front,
            rear=rear,
            side=side,
            interior=interior,
        )
        # saving the data to the database
        second_hand_car.save()
        messages.add_message(request, messages.INFO, "Post sent, waiting for approval")

    return render(request, "frontend/postyourcar.html")


def car_detail(request, id):
    # views to display the car detail page
    car_detail = Second_Hand_Car.objects.get(id=id)
    return render(request, "frontend/cardetail.html", {"car_detail": car_detail})

def about_us(request):
    return render(request, "frontend/about.html")

