from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(required=False)


class DistributeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DistributeForm, self).__init__(*args, **kwargs)
        self.fields = args[0]
