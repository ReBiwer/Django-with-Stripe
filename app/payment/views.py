from django.http import HttpRequest, JsonResponse
from django.views.generic import View, DetailView
from .utils import get_stripe_session
from .models import Item


class GetStripeSession(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        id_item = self.kwargs.get('id')
        item_obj = Item.objects.get(id=int(id_item))
        session_pay = get_stripe_session(item_obj, request)
        return JsonResponse(data={'session': session_pay})


class PayItem(DetailView):
    template_name = 'payment/buy_item.html'
    context_object_name = 'item'
    model = Item
