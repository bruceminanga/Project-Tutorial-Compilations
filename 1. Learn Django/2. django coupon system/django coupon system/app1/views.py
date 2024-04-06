from django.shortcuts import render
from .forms import OrderForm, CouponApplyForm
from .models import Order, Coupon
from .utils import calculate_price
from django.utils import timezone

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

@csrf_exempt
def paypal_view(request):
    if request.method == 'POST':
        payment_id = request.POST.get('paymentID')
        # Here you can process the payment using the payment_id
        # You might want to use the PayPal REST API to execute the payment
        # After processing the payment, you can return a JsonResponse
        return JsonResponse({'status': 'success'})
    else:
        # If the request method is not POST, you can render your form here
        return render(request, 'your_template.html')

class CouponView(View):
    def get(self, request, *args, **kwargs):
        code = self.kwargs.get('code')
        try:
            coupon = Coupon.objects.get(code=code)
            if coupon.valid_from <= timezone.now() <= coupon.valid_to:
                return JsonResponse({'active': coupon.active, 'discount': coupon.discount})
            else:
                return JsonResponse({'active': False})
        except Coupon.DoesNotExist:
            return JsonResponse({'active': False})

def order(request):
    price = None
    currency = None 
    academic_level = None
    coupon_apply_form = CouponApplyForm()  # Define here
    if request.method == 'POST':
        form = OrderForm(request.POST)
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

        form2 = CouponApplyForm(request.POST)
        if form2.is_valid():
            code = form2.cleaned_data['coupon_code']
            now = timezone.now()
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None

    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form, 'coupon_apply_form': coupon_apply_form, 'price': price, 'currency':currency, 'academic_level':academic_level})
