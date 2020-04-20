from django import forms


from general_app.models import Words


class AddWordForm(forms.ModelForm):

    class Meta:
        model = Words
        fields = ('english_word', 'russian_word')
