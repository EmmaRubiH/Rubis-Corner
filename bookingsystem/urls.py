# from . import views
# from django.urls import path


# urlpatterns = [
#     path('', views.PostList.as_view(), name='home'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
# ]
""" This file contains all the
URLs for the booking site
"""

from django.urls import path
from . import views


app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('menus/', views.Menus.as_view(), name='menus'),
    path('thanks/', views.ThankYou.as_view(), name='thanks'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('my_bookings/', views.ListBookingView.as_view(), name='my_bookings'),
    path('edit_bookings/<booking_id>', views.edit_booking_view, name='edit'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete'),
]