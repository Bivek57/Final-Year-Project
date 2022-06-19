from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),                                          # homepage
    path("car_consultancy/", views.car_consultancy, name="car_consultancy"),    # car_consultancy page
    path("reviews/", views.reviews, name="reviews"),                            # reviews page
    path("reviews/<str:name>/", views.reviews_details, name="reviews_details"), # detailed review of carname
    path("reviews/#show-all-reviews", views.all_reviews, name="all_reviews"),   # shows all the reviews
    path("market/", views.market, name="market"),                               # shows the market page
    path("market/#show-all-car", views.load_all_market, name="allmarket"),      # shows the market page
    path("contact/", views.contact, name="contact"),                            # shows the contact page
    path("newsdetails/<str:news_title>/", views.recent_news_details, name="newsdetails"),# show the recent news details page 
    path("post_your_car/", views.post_your_car, name="postcar"),                # shows the post_your_car page
    path("detail/<str:id>", views.car_detail, name="car_detail"),               # shows the car_detail page taking car id as parameter
    path("comparision/", views.comparision, name="comparision"),                # shows the comparision page
    path("comparision/#show-all-comparision", views.load_all_comp, name="allcomp"),#shows all the comparision
    path("comparision/<str:name>", views.comparison_details, name="comparision_detail"), #shows detail comparision of carname
    path("about", views.about_us, name="about_us")
]
