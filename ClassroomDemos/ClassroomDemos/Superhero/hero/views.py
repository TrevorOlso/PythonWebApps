from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MainView(TemplateView):
    template_name = 'hero.html'

class BlackWidowView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Black Widow',
            'id': 'Natasha Romanoff',
            'image': 'static/images/black_widow.jpg',
            'strength1': 'Spy skills',
            'strength2': 'Assasin skills',
            'strength3': 'braclet that fires electric shock',
            'weakness1': 'mortal',
            'weakness2': 'self-doubting'
        }

class IronManView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Iron Man',
            'id': 'Tony Stark',
            'image': 'static/images/iron_man.jpg',
            'strength1': 'Genius',
            'strength2': 'Rich',
            'strength3': 'Iron man suit',
            'weakness1': 'Arrogant',
            'weakness2': 'No real superpower'
        }
class HulkView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': 'static/images/hulk.jpg',
            'strength1': 'Massive Size',
            'strength2': 'Super Strength',
            'weakness1': 'Arrogant',
            'weakness2': 'Has to take meds to make strong'
        }
class AntManView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Antman',
            'id': 'Scott Lang',
            'image': 'static/images/antman.jpg',
            'strength1': 'Can change size',
            'strength2': 'Super Strength',
            'weakness1': 'Dealing with his past',
            'weakness2': 'Suit malfunctions at important times'
        }
class BlackPantherView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Black Panther',
            'id': 'TChalla',
            'image': 'static/images/blackpanther.jpg',
            'strength1': 'Super speed',
            'strength2': 'nearly invincible',
            'weakness1': 'Arrogant',
            'weakness2': 'Is mortal'
        }