from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from store_app.models import *
from .models import ShipingAddress
from django.contrib import messages

#ssl
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import json
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class CheckoutView(View):
    def get(self,request, *args, **kwargs):
        form = ShipingAddressForm()
        paymentform = PaymentMethodForm()
        order = Order.objects.filter(user=request.user, ordered=False)
        context ={
            'form':form,
            'paymentform':paymentform,
            'order':order
        }
        return render(request, 'payment_app/checkout.html', context)

    def post(self,request,*args, **kwargs):
        form = ShipingAddressForm(request.POST)     
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)

        if request.method == 'POST':
            form = ShipingAddressForm(request.POST)
            pay_form = PaymentMethodForm(request.POST,instance=payment_obj)

            if form.is_valid() and pay_form.is_valid():
                name = form.cleaned_data.get('name')
                phone = form.cleaned_data.get('phone')
                full_address =form.cleaned_data.get('full_address')
                order_note =form.cleaned_data.get('order_note')
                
                shipingaddress = ShipingAddress(
                    user = request.user,
                    name = name,
                    phone = phone,
                    full_address = full_address,
                    order_note = order_note,
                )
                shipingaddress.save()
                pay_method = pay_form.save()

                if pay_method.payment_option == 'Cash On Delivery':
                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.total_order_amount = order.total()
                    order.payment_option = pay_method.payment_option

                    cart_products = CartProduct.objects.filter(user=request.user, ordered=False)
                    for cart_product in cart_products:
                        cart_product.ordered = True
                        cart_product.save()
                    order.save()
                    messages.success(request, ' Order successfully done')
                    return redirect('/')

                elif pay_method.payment_option == 'SSL Commerze':
                    store_id = settings.STORE_ID
                    store_pass = settings.STORE_PASS
                    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_pass)
                    
                    status_url = request.build_absolute_uri(reverse('status'))
                    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order_items = order_qs[0].cart_products.all()
                    order_item_count = order_qs[0].cart_products.count()
                    order_total = order_qs[0].total()
                    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='clothing', product_name=order_items, num_of_item=order_item_count, shipping_method='YES', product_profile='None')
                	
		            #customer profile information dite hobe

                    current_user = request.user
                    mypayment.set_customer_info(name=current_user.username, email=current_user.email, address1='demo1', address2='demo2', city='Dhaka', postcode=1207, country='Bangladesh', phone='01704870490')
          
                    mypayment.set_shipping_info(shipping_to=current_user.username, address='demo3', city='Dhaka', postcode=1207, country='Bangladesh')
                    
                    response_data = mypayment.init_payment()
                    # print(response_data)
                    return redirect(response_data['GatewayPageURL'])
                return redirect('checkout')

@csrf_exempt
def sslc_status(request):
    if request.method == 'post' or request.method == 'POST':
        payment_data = request.POST
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']

            return HttpResponseRedirect(reverse('sslc-complete', kwargs={'val_id': val_id, 'tran_id': tran_id}))
    return render(request, 'payment_app/status.html')

def sslc_complete(request,val_id,tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    order.ordered = True
    order.total_order_amount = order.total()
    order.payment_option = pay_method.payment_option

    cart_products = CartProduct.objects.filter(user=request.user, ordered=False)
    for cart_product in cart_products:
        cart_product.ordered = True
        cart_product.save()
    order.save()
    messages.success(request, ' Order successfully done')
    return redirect('/')


