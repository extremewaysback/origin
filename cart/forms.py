#cart/forms.py

from django import forms

PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    #This allows the user to select a quantity between 1-20.
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    #this allows you to indicate whether the quantity has to be added to any existing quantity or updated with the given quantity
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)