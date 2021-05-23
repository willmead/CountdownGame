from django.views import generic

import random


class IndexView(generic.TemplateView):
    template_name = 'number_game/index.html'
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.big_num = random.choice([20, 50, 75, 100])
        self.small_num1 = random.randint(1, 10)
        self.small_num2 = random.randint(1, 10)
        self.small_num3 = random.randint(1, 10)
        self.small_num4 = random.randint(1, 10)
        self.small_num5 = random.randint(1, 10)
        self.total_to_get = random.randint(100, 999)

        context.update({'big_num': self.big_num})
        context.update({'small_num1':  self.small_num1})
        context.update({'small_num2':  self.small_num2})
        context.update({'small_num3':  self.small_num3})
        context.update({'small_num4':  self.small_num4})
        context.update({'small_num5':  self.small_num5})
        context.update({'total_to_get': self.total_to_get})

        return context
