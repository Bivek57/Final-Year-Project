from django.contrib import admin

# import user model
from django.contrib.auth.models import User

from .models import (
    Car_detail,
    Comparision,
    Consult,
    Contact_Detail,
    Most_popular,
    Recent_News,
    Reviews,
    Second_Hand_Car,
)


class ConsultAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "phone",
        "email",
        "address",
    )
    # add search list
    search_fields = (
        "name",
        "id",
        "phone",
        "email",
        "address",
    )


class Recent_NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
        "description",
        "image",
    )
    # add search list
    search_fields = (
        "title",
        "id",
        "description",
        "image",
    )


class Most_popularAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
        "image",
    )
    # add search list
    search_fields = (
        "title",
        "id",
        "image",
    )


class Second_Hand_CarAdmin(admin.ModelAdmin):
    list_display = (
        "seller_name",
        "id",
        "carname",
        "approve_status",
        "price",
        "location",
        "make_year",
    )
    # add search list
    search_fields = (
        "seller_name",
        "id",
        "carname",
        "price",
        "location",
        "make_year",
    )


class Contact_DetailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "phone",
        "email",
        "address",
    )
    # add search list
    search_fields = (
        "name",
        "id",
        "phone",
        "email",
        "address",
    )


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "thumbnail",
    )
    # add search list
    search_fields = (
        "name",
        "id",
    )


class ComparisionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "thumbnail",
        "vs_image",
    )
    # add search list
    search_fields = (
        "name",
        "id",
        "thumbnail",
        "vs_image",
    )


class CarDetailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "price",
    )
    # add search list
    search_fields = (
        "name",
        "id",
        "price",
    )


class UserAdmin(admin.ModelAdmin):
    odering = ["-id"]
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    # add search list
    search_fields = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
        "date_joined",
    )


admin.site.register(Consult, ConsultAdmin)
admin.site.register(Contact_Detail, Contact_DetailAdmin)
admin.site.register(Most_popular, Most_popularAdmin)
admin.site.register(Recent_News, Recent_NewsAdmin)
admin.site.register(Second_Hand_Car, Second_Hand_CarAdmin)
admin.site.register(Reviews, ReviewsAdmin)
# admin.site.register(Car_detail)
admin.site.register(Comparision, ComparisionAdmin)
admin.site.register(Car_detail, CarDetailAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# change the admin site title
admin.site.site_header = "CarSansar Admin"
admin.site.site_title = "CarSansar Admin"
admin.site.index_title = "CarSansar Admin"
