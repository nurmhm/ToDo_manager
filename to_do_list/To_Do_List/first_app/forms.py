from django import forms

from . import models

class ToDoform(forms.ModelForm):
    class Meta:
        model = models.ToDoModel
        fields = ['titel','discription']


