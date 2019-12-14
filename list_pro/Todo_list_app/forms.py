from django import forms
class TodoForms(forms.Form):
    text = forms.CharField(max_length=40,
                           widget = forms.TextInput(attrs={'class': 'form-control' ,'placeholder' : 'Enter todo list@@','aria-label' : 'Todo', 'aria-describedby' : 'add-btn' }))