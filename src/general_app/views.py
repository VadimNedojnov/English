from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


from general_app.models import Words
from general_app.forms import AddWordForm


class WordListView(ListView):
    model = Words
    template_name = 'words_list.html'
    queryset = Words.objects.all()


class AddWordView(CreateView):
    template_name = 'add_word.html'
    queryset = Words.objects.all()
    success_url = reverse_lazy('index')
    form_class = AddWordForm
