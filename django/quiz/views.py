from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views import View
from django.http import Http404

from .models import Kanji

import random

class QuizView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        easy_kanji = Kanji.objects.filter(Q(jlpt=5)|Q(jlpt=4))
        random_kanji = random.choice(easy_kanji)
        return render(request, self.template_name, {
            'kanji_id': random_kanji.id,
            'kanji': random_kanji.symbol,
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

        for meaning in meanings:
            if answer == meaning.meaning:
                is_correct = True
                break
        
        if is_correct is True:
            return render(request, 'feedback.html', {'status': True, 'meanings': meanings})
        else:
            return render(request, 'feedback.html', {'status': False, 'meanings': meanings, 'kanji': kanji})