from django.shortcuts import render, redirect
from .models import News
from django.forms import modelformset_factory
from django import forms


def new(request):
    class NewsForm(forms.ModelForm):
        title = forms.CharField(label='Название')

        class Meta:
            model = News
            fields = ('title', 'type', 'news', )

    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            post = news.save()

            post.save()
            return redirect(new)
    else:
        news = NewsForm()
        formset = News.objects.filter
        return render(request, 'news/news.html', {'news': news, 'new': formset})


