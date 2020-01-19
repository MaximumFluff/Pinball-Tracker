from django import forms

class ScoreForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100)
    high_score = forms.IntegerField(label='Score')