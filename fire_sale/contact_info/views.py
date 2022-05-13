
from contact_info.forms.contact_form import ContactForm
from django.shortcuts import render, redirect

def contact_info(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            new_contact.user = request.user
            new_contact.save()
            return redirect('checkout-payment')
        else:
            form = ContactForm()
        return render(request, 'checkout/contact_info.html', {
            'form': form
        })




