from django import template
from store_app.models import WishList

register = template.Library()

@register.filter
def wishlist_product_count(user):
    if user.is_authenticated:
        return WishList.objects.filter(user=user).count()
    return 0


