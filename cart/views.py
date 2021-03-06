from django.shortcuts import render, redirect, reverse
from django.utils.html import format_html
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    """
    A View that renders the cart contents page
    """
    context = {
        'title': 'Cart',
        'nbar': 'cart',
    }
    return render(request, "cart.html", context)


@login_required
def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    if quantity > 0:
        message = format_html('Go to cart? <a class="jpt-link-red" href="{}">Click here</a>.', reverse('checkout'))
        messages.info(request, message, extra_tags='safe')

    return redirect(reverse('products'))


@login_required
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))