from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView


from general_app.models import Words
from general_app.forms import AddWordForm, QuestionForm


class WordListView(ListView):
    model = Words
    template_name = 'words_list.html'
    queryset = Words.objects.all()


class AddWordView(CreateView):
    template_name = 'add_word.html'
    queryset = Words.objects.all()
    success_url = reverse_lazy('index')
    form_class = AddWordForm


def word_generator():
    queryset = Words.objects.all()
    vocabulary = set()
    for i in queryset:
        vocabulary.add(i.english_word)
    vocabulary_list = list(vocabulary)
    return iter(vocabulary_list)


def game_en_ru_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.data['russian_word'] == Words.objects.get(english_word=form.data['english_word']).russian_word:
            return HttpResponseRedirect(reverse('general-app:game'))
        else:
            return HttpResponseRedirect(reverse('general-app:game-wrong'))
    else:
        form = QuestionForm()
        return render(request, 'game.html', context={'form': form, 'words': word_generator()})
