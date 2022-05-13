from payment.forms.payment_form import PaymentForm
from django.shortcuts import redirect
from django.shortcuts import render

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            new_payment = form.save()
            new_payment.user = request.user
            new_payment.save()
            return redirect('item-index')
        else:
            form = PaymentForm()
        return render(request, 'checkout/payment.html', {
            'form': form
        })




# Create your views here.
