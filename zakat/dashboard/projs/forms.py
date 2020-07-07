from django import forms


class CloseCampaignForm(forms.Form):
    text = forms.CharField(max_length=128)
