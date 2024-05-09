from django.shortcuts import render, redirect
from store.models import Products
from card.models import Card, CardItem
from django.views import View


from django.core.paginator import Paginator
from django.http import JsonResponse


class StoreView(View):
    def get(self, request, page=1):
        product_list = Products.objects.all()
        paginator = Paginator(product_list, 9)
        page_obj = paginator.get_page(page)
        card_items = CardItem.objects.all()

        return render(request, 'home/index.html', {
            'page_obj': page_obj,
            'card_items': card_items,
        })

    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        user_key = request.session.session_key

        if not user_key:
            request.session.save()
            user_key = request.session.session_key

        card, _ = Card.objects.get_or_create(session_user=user_key)
        product = Products.objects.get(id=product_id)
        card_item = CardItem.objects.filter(card=card, product=product).first()

        if card_item:
            card_item.quantity += quantity
            card_item.price = product.price * card_item.quantity
            card_item.save()
        else:
            product_price = product.price * quantity
            card_item = CardItem(
                card=card,
                product=product,
                quantity=quantity,
                price=product_price,
                status=False
            )
            card_item.save()
        card_items_count = CardItem.objects.count()
        return JsonResponse({'success': True, 'card_len': card_items_count})





