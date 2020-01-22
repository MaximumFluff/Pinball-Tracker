from django.shortcuts import render
from django.utils import timezone
from .models import Score
from .forms import ScoreForm


def index(request):
    scores = Score.objects.order_by('-high_score')[:5]
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            q = Score(high_score=form.data['high_score'], username=form.data['username'], date=timezone.now())
            q.save()
        form = ScoreForm()
        context = {'scores': scores, 'form': form, 'title': 'Home'}
        return render(request, 'pinball/index.html', context)
    else:
        form = ScoreForm()
        context = {'scores': scores, 'form': form, 'title': 'Home'}
        return render(request, 'pinball/index.html', context)


def list_all(request):
    scores = Score.objects.order_by('-high_score')
    context = {'scores': scores, 'title': 'All high scores'}
    return render(request, 'pinball/list_all.html', context)