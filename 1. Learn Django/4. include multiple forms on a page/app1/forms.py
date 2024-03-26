from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()

class CouponApplyForm2(forms.Form):
    code = forms.CharField()