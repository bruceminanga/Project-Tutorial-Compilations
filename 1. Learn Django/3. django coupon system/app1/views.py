from django.shortcuts import render
from .forms import OrderForm, CouponApplyForm
from .models import Order
from .utils import calculate_price

def order(request):
    price = None
    currency = None 
    academic_level = None
    if request.method == 'POST':
        form = OrderForm(request.POST)
        coupon_apply_form = CouponApplyForm()

        if form.is_valid():
            academic_level = form.cleaned_data['academic_level']
            service_type = form.cleaned_data['service_type']
            currency = form.cleaned_data['currency']
            price = calculate_price(academic_level, service_type, currency)
            # Save the form but don't commit to the database yet
            order = form.save(commit=False)
            # Assign the calculated price to the order's price field
            order.price = price
            # Now save the order to the database
            order.save()
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form, 'price': price, 'currency':currency, 'academic_level':academic_level})
