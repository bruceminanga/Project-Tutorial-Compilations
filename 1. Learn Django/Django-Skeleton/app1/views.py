from django.shortcuts import render
from .forms import CouponApplyForm, CouponApplyForm2
from django.forms import formset_factory
# def home(request):
#     # form = CouponApplyForm()
#     FirstFormSet = formset_factory(CouponApplyForm, extra=1)
#     return render(request, 'index.html', {'FirstFormSet': FirstFormSet})

# def home2(request):
#     # form2 = CouponApplyForm2()
#     FirstFormSet2 = formset_factory(CouponApplyForm2, extra=1)

#     return render(request, 'index.html', {'FirstFormSet2': FirstFormSet2})

def home(request):
    form = CouponApplyForm()
    form2 = CouponApplyForm2()
    if request.method == 'POST':
        if 'form' in request.POST:
            form = forms.BlogForm()
            
        if 'fom2' in request.POST:
            form2 = forms.CouponApplyForm2()
            
    context = {
        'form': form,
        'form2': form2,
    }
    return render(request, 'index.html', context=context)