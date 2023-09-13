from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        widgets = {
            'myfield': forms.TextInput(attrs={'style': 'border-color:darkgoldenrod; border-radius: 10px;'}),
        }
        fields = ['title']