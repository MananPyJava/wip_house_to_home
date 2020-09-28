from django.shortcuts import render, HttpResponse, redirect
from .models import shop_items, orders
from django.core.mail import send_mail
import random

context=''
real_otp=0
email=''
ordered_item=''
name=''
phone_number=0
address=''
# Create your views here.
def shop(request):
    global context
    try:
        q=request.GET['q']
        return search(request=request, q=q)
    except:
        try:
            buy=request.GET['buy']
            items=shop_items
            items_all=items.objects.all()
            for x in items_all:
                if buy in x.name_of_item:
                    context=x
                    break
                else:
                    pass
            if context != '':
                return render(request, 'buy.html')
            else:
                return redirect('/shop')
        except:
                items=shop_items
                context=items.objects.all() 
                return render(request, 'shop.html', {'context': context,'alerts':'1'})

def search(request, q):
    items=shop_items
    items_all=items.objects.all()
    context=[]
    for x in items_all:
        if q in x.name_of_item:
            context.append(x)
    if context != []:
       return render(request, 'shop.html', {'context':context})
    else:
        return render(request, 'no_item.html')

def buy(request):
    global context, real_otp, email, ordered_item, name, phone_number, address
    ordered_item=context.name_of_item
    name=request.POST['name']
    address=request.POST['address']
    email=request.POST['email']
    phone_number=request.POST['phone_number']
    if name=='':
        return render(request, 'all_details.html')
    elif address=='':
        return render(request, 'all_details.html')
    elif email=='':
        return render(request, 'all_details.html')
    elif phone_number=='':
        return render(request, 'all_details.html')
    else:
        real_otp=random.randint(100000,999999)
        send_mail(f'OTP for {ordered_item}', f'your OTP for {ordered_item} is {real_otp}.','gandhimanan1810@gmail.com',[email])
        return render(request,'bought.html')

def check(request):
    global real_otp, email, ordered_item, name, phone_number, address
    Otp=int(request.POST['OTP'])
    if Otp==real_otp:
        o=orders(name=name, address=address, email=email, ordered_item=ordered_item, phone_number=phone_number)
        o.save()
        send_mail('Order Placed', f'your order for {ordered_item} is has been placed. Further communication about your order will be done through mobile phone call. If you want to know about your order, you can contact us at the email Id: gandhimanan1810@gmail.com.','gandhimanan1810@gmail.com',[email])
        return render(request,'done.html')
    else:
        return render(request,'wrong_otp.html')