from django import forms


from faker import Faker


from general_app.models import Words


fake = Faker()


class AddWordForm(forms.ModelForm):

    class Meta:
        model = Words
        fields = ('english_word', 'russian_word')


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Words
        fields = ('english_word', 'russian_word')
