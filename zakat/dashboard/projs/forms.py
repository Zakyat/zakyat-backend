from django import forms

from payment.models import PaymentOptions
from projects.models import Campaign


class CloseCampaignForm(forms.Form):
    text = forms.CharField(max_length=128)


class PaymentOptionsCreateForm(forms.ModelForm):
    PAYMENT_TYPES_ENUM = (
        ('true', 'Credit Card'),
        ('unknown', 'Some Other'),
        ('false', 'Cash Money'),
    )
    PAYMENT_TYPES_TRANSFOR = {
        'false': False,
        'unknown': None,
        'true': True
    }
    payment_type = forms.ChoiceField(choices=PAYMENT_TYPES_ENUM, required=True)

    class Meta:
        model = PaymentOptions
        fields = ['title', 'description', 'payment_type']

    def clean_payment_type(self):
        payment_type = self.cleaned_data['payment_type']
        return self.PAYMENT_TYPES_TRANSFOR.get(payment_type)


class CampaignEditForm(forms.ModelForm):
    class Meta:
        model = Campaign
        # TODO keep in mind to specify Employer as creator
        fields = ['title', 'description', 'project', 'request', 'goal']
