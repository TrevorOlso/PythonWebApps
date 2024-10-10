from pathlib import Path
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero


class MainView(TemplateView):
    template_name = 'hero.html'


class HeroView(TemplateView):
    template_name = 'heros.html'


    def get_context_data(self, **kwargs):
        return {
            'superhero': Superhero.objects.get(name=kwargs['name'])
        }

