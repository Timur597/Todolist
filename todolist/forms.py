from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Text for todolist',
        'aria-label': 'Todolist',
        'aria-describedby': 'add-btn'
    }))
