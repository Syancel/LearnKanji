from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import Http404

from .models import Kanji

import random

class QuizView(View):
    form_class = None
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        kanji_id = random.randint(1, Kanji.objects.all().count())
        try:
            kanji = Kanji.objects.get(pk=kanji_id)
        except Kanji.DoesNotExist:
            raise Http404("Kanji does not exist")
        return render(request, self.template_name, 
                    {'kanji': kanji, 'meanings': None, 'kunyomis': None, 'onyomis': None})

    def post(self, request, *args, **kwargs):
        pass
