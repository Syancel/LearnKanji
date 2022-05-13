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
        except Kanji.DoesNotExist:
            raise Http404("Kanji does not exist")
        return render(request, self.template_name, {
            'kanji_id': kanji_id,
            'kanji': kanji,
            })

    def post(self, request, *args, **kwargs):
        kanji_id = request.POST.get('kanji_id')
        answer = request.POST.get('answer')
        is_correct = False
        try:
            kanji = Kanji.objects.get(pk=kanji_id)
            meanings = kanji.meanings.all()
            onyomis = kanji.onyomis.all()
            kunyomis = kanji.kunyomis.all()
        except Kanji.DoesNotExist:
            raise Http404("Kanji does not exist")

        print('Answer: ' + answer)
        for meaning in meanings:
            if answer == meaning.meaning:
                is_correct = True
                break
        
        if is_correct is True:
            return render(request, 'feedback.html', {'status': True})
        else:
            return render(request, 'feedback.html', {'status': False, 'meanings': meanings})