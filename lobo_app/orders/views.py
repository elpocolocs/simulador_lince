from cart.cart import Cart
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["curso"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            # limpiar el carrito
            cart.clear()
            return render(
                request,
                "created.html",
                {
                    "order": order,
                },
            )
    else:
        form = OrderCreateForm()
    return render(
        request,
        "create.html",
        {
            "cart": cart,
            "form": form,
        },
    )
