from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'password', 'avatar', 'telephone')
    list_filter = ('email',)
    search_fields = ('email',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_pay', 'course', 'lesson', 'amount', 'payment_method')
    list_filter = ('user',)
