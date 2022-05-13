from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.http import Http404

from .models import Kanji

import random

class QuizView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        kanji_id = random.randint(1, Kanji.objects.all().count())
        try:
            kanji = Kanji.objects.get(pk=kanji_id)
            meanings = kanji.meanings.all()
            onyomis = kanji.onyomis.all()
            kunyomis = kanji.kunyomis.all()
        except Kanji.DoesNotExist:
            raise Http404("Kanji does not exist")
        return render(request, self.template_name, {
            'kanji': kanji,
            'meanings': meanings,
            'onyomis': onyomis,
            'kunyomis': kunyomis,
            })

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if request.POST.get('answer') in request.POST.get('meanings'):
            return render(request, 'feedback.html', {'status': True})
        else:
            return render(request, 'feedback.html', {'status': False})