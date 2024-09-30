from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView
)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayMixin:
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass


class BirthdayCreateView(BirthdayMixin, CreateView):
    pass


class BirthdayDeleteView(DeleteView):
    pass


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 2


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context
