from .cart import Cart

# create context processor so our cart can work on all page

def cart(request):
    return {'cart': Cart(request)}

def cart_quantity(request):
    cart_sumary = Cart(request)
    return {'cart_quantity': cart_sumary.__car__len__() + cart_sumary.__accesary_len__()}