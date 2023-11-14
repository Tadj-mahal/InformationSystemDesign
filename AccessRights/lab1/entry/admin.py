from django.contrib import admin
from .models import User
from .forms import UserCreateForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
	model = User
	add_form = UserCreateForm

	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'User position',
			{
				'fields':(
					'position',
					'address',
					'phone',
				)
			}
		)
	)
admin.site.register(User, CustomUserAdmin)