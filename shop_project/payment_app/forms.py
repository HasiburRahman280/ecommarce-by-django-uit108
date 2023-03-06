from django import forms
from .models import *
from store_app.models import *

class ShipingAddressForm(forms.Form):
    name = forms.CharField()
    phone =forms.CharField()
    full_address =forms.CharField(widget=forms.Textarea())
    order_note =forms.CharField(widget=forms.Textarea())


PaymentOption = (
        ('Cash On Delivery','Cash On Delivery'),
        ('SSL Commerze','SSL Commerze'),
    )
class PaymentMethodForm(forms.ModelForm):
    payment_option = forms.ChoiceField(choices=PaymentOption,widget=forms.RadioSelect(attrs={
    }))
    class Meta:
        model = Order
        fields = ['payment_option']
