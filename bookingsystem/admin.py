# from django.contrib import admin
# from .models import Post
# from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):

#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
#     list_filter = ('status', 'created_on')
#     summernote_fields = ('content')
from django.contrib import admin
from .models import Booking, SignUp


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('name', 'email_address')


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    model = SignUp
    list_display = ('first_name', 'last_name', 'email_address')
