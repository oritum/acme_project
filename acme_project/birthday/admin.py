from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    """Админ-класс для управления моделями Birthday."""

    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    search_fields = (
        'first_name',
        'last_name',
        'birthday',
    )
