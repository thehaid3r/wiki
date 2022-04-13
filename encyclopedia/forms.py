from django import forms

class new(forms.Form):
    title=forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control col-lg-4 '}),
        label='Title',
        required=True,
    )
    content=forms.CharField(
        widget=forms.Textarea(attrs={'class' : 'form-control col-lg-8'}),
        label='Content',
        required=True,
    )