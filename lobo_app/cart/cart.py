from decimal import Decimal

from cursos.models import Curso
from django.conf import settings


class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # guardar un carrito vacío en la sesión
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, curso, quantity=1, override_quantity=False):
        """
        Agregar un curso al carrito o actualizar la cantidad.
        """
        curso_id = str(curso.id)
        if curso_id not in self.cart:
            self.cart[curso_id] = {
                "quantity": 0,
                "price": str(curso.precio),
            }
        if override_quantity:
            self.cart[curso_id]["quantity"] = quantity
        else:
            self.cart[curso_id]["quantity"] += quantity
        self.save()

    def save(self):
        # marcar la session como "modificada" para asegurar que Django la guarde
        self.session.modified = True

    def remove(self, curso):
        """
        Remover un producto del carrito
        """
        curso_id = str(curso.id)
        if curso_id in self.cart:
            del self.cart[curso_id]
            self.save()

    def __iter__(self):
        """
        Itera sobre los elementos en el carrito y obtiene los cursos de la base
        de datos
        """
        curso_ids = self.cart.keys()
        # toma los objetos cursos y los agrega al carrito
        cursos = Curso.objects.filter(id__in=curso_ids)
        cart = self.cart.copy()
        for curso in cursos:
            cart[str(curso.id)]["curso"] = curso

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Cuenta los elementos en el carrito
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def clear(self):
        # remover el carrito de la sesión
        del self.session[settings.CART_SESSION_ID]
        self.save()
