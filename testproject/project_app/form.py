from django import forms


class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    father_name = forms.CharField(max_length=100)
    mother_name = forms.CharField(max_length=100)


class CatagoryiesForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_code = forms.CharField(max_length=100)
    product_address = forms.CharField(max_length=100)