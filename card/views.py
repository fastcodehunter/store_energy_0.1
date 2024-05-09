from django.shortcuts import render
from django.shortcuts import render, redirect
from card.models import Card, CardItem ,Order
from card.forms import FormMakingAnOrder
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages



def delete_card_item(card_item_id):
    try:
        card_item = CardItem.objects.filter(product_id=card_item_id)
        card_item.delete()
    except CardItem.DoesNotExist:
        pass
def list_products(request): 
    try:
        user_key = request.session.session_key
        card = Card.objects.get(session_user=user_key)
    except Card.DoesNotExist:
        card=None
    
    if request.method == 'POST':
            get_product_post = request.POST.get("delete")
            delete_card_item(get_product_post)  
                  
    if user_key or card is None:
        card_items = CardItem.objects.filter(card=card)
        total_cost = 0
        lenghttt=[]
        for card_item in card_items:
            total_cost += float(card_item.price)
            lenghttt.append(card_item.product.title)
            
            
        return render(request, 'home/card/card.html', {"card_items": card_items,
                                                       "total_cost": total_cost,
                                                       "lenghttt": len(lenghttt)})
    return render(request, 'home/card/card.html')


def place_an_order(request):
    try:
        user_key=request.session.session_key
        user_session=Card.objects.get(session_user=user_key)
        items = CardItem.objects.filter(card=user_session)
        total_number=0
    except Card.DoesNotExist:
        pass

    if request.method == "POST":
        form = FormMakingAnOrder(request.POST)
        shopping_list=[]
        
        if form.is_valid():
            order = form.save()
            order.card = user_session
            
            for item in items:
                item.product.quantity -= item.quantity
                item.product.popular+=item.quantity
                total_number+=item.price
                print(total_number)
                item.product.save()
                
                shopping_list.append(
                    {
                        "Product name":item.product.title,
                        'quantity':item.quantity,
                        'total number': total_number,
                    }   
                )
                order.shopping_list=shopping_list
                order.save()
                items.delete()
            get_id_order=Order.objects.filter(card=user_session).last()
            send_mail(
                    'The order has been placed',
                    'Your order has been successfully placed. Your order number: {}'.format(get_id_order.id),
                    'bothlpr@gmail.com',
                    [order.email],
                    fail_silently=False,
                )
            return redirect('store')
        else:
            messages.error(request, 'The fields contain errors')  # Добавление сообщения об ошибке
    else:
        
        form = FormMakingAnOrder()
    return render(request, 'home/order/order.html', locals())
