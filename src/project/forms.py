from django import forms


class PostQuery(forms.Form):
    name = forms.CharField(max_length=50)
    weigth = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()


class PutQuery(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    weigth = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
