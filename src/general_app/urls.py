from django.urls import path


from general_app.views import WordListView, AddWordView


app_name = 'general-app'


urlpatterns = [
    path('word-list/', WordListView.as_view(), name='word-list'),
    path('add-word/', AddWordView.as_view(), name='add-word'),
]
