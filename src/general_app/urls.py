from django.urls import path
from django.views.generic import TemplateView


from general_app.views import WordListView, AddWordView, game_en_ru_view


app_name = 'general-app'


urlpatterns = [
    path('word-list/', WordListView.as_view(), name='word-list'),
    path('add-word/', AddWordView.as_view(), name='add-word'),
    path('game/', game_en_ru_view, name='game'),
    path('game-wrong/', TemplateView.as_view(template_name='game_wrong.html'), name='game-wrong'),
]
