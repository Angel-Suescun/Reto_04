import random
import time

class MenuItem:
    """Representa un artículo del menú con un nombre y un precio."""

    def __init__(self, name: str, price: int) -> None:
        """Inicializa el artículo del menú con nombre y precio."""
        self._name = name
        self._price = price

    def calculate_total(self, order: 'Order') -> float:
        """Calcula el total de una orden aplicando descuento."""

        def compound_order(order) -> None:
            """Mediante de que se compone el pedido, genera un descuento."""
            # Descuento del 10% si hay un MainDish y un Drink
            if any(isinstance(item, MainDishes) for item in order._items.keys()):
                for key, item in order._items.items():
                    if isinstance(key, Drink):
                        order._items[key] = item * 0.9  # 10% de descuento en Drink
                        print("Descuento del 10% en Drink")
                        break

            # Descuento del 5% si hay un Breakfast y un Dessert
            if any(isinstance(item, Breakfast) for item in order._items.keys()):
                for key, item in order._items.items():
                    if isinstance(key, Dessert):
                        order._items[key] = item * 0.95  # 5% de descuento en Dessert
                        print("Descuento del 5% en Dessert")
                        break

        compound_order(order)
        total = sum(order._items.values())
        total -= total * order._discount_percentage
        return total

    def print_order(self, order: 'Order') -> None:
        """Imprime los detalles de la orden y el total con descuento."""
        total = self.calculate_total(order)
        for item, price in order._items.items():
            print(f"{item._name} - {price}")
        print(f"Descuento: {order._discount_percentage * 100}%")
        print(f"Total: ${total:,} pesos")

    def pagar(self, order):
        order._type_payment.pagar(order._total)

class Order:
    """Representa una orden realizada por un cliente."""

    def __init__(self, type_payment, student: bool = False) -> None:
        """Inicializa la orden con un descuento y una lista de artículos."""
        self._items: dict = {}
        self._discount_percentage: float = 0
        self._student = student
        self._type_payment = type_payment

    def add_item(self, item: MenuItem, quantity: int) -> None:
        """Añade un artículo a la orden multiplicado por la cantidad."""
        self._items[item] = quantity * item._price

    def calculate_total(self) -> float:
        """Calcula el total de la orden aplicando el descuento."""

        def compound_order(self) -> None:
            """Mediante de que se compone el pedido, genera un descuento."""
            if any(isinstance(item, MainDishes) for item in self._items.keys()):
                for key, item in self._items.items():
                    if isinstance(key, Drink):
                        self._items[key] = item * 0.9
                        print("Descuento del 10% en Drink")
                        break

            if any(isinstance(item, Breakfast) for item in self._items.keys()):
                for key, item in self._items.items():
                    if isinstance(key, Dessert):
                        self._items[key] = item * 0.95
                        print("Descuento del 5% en Dessert")
                        break

        compound_order(self)
        total = sum(self._items.values())
        total -= total * self._discount_percentage
        return total

    def promos(self) -> None:
        """Aplica promociones y descuentos según reglas predefinidas."""
        self._discount_percentage = 0

        if len(self._items) >= 6:
            self._discount_percentage += 0.1

        if self._student:
            self._discount_percentage += 0.2

        if random.random() < 0.1:
            self._discount_percentage = 1

    def print_order(self) -> None:
        """Imprime la orden y el total con descuento aplicado."""
        self._total = self.calculate_total()
        for item, price in self._items.items():
            print(f"{item._name} - {price}")
        print(f"Descuento: {self._discount_percentage * 100}%")
        print(f"Total: ${self._total:,} pesos")

    def pagar(self):
        self._type_payment.pagar(self._total)

class Drink(MenuItem):
    def __init__(self, name: str, price: int, unit: int) -> None:
        super().__init__(name, price)
        self._unit = unit

class MainDishes(MenuItem):
    def __init__(self, name: str, price: int, ingredients: list) -> None:
        super().__init__(name, price)
        self._ingredients: list = ingredients

class Dessert(MenuItem):
    def __init__(self, name: str, price: int, size: int) -> None:
        super().__init__(name, price)
        self._size = size

class Salads(MenuItem):
    def __init__(self, name: str, price: int, container: str) -> None:
        super().__init__(name, price)
        self._container = container

class Soups(MenuItem):
    def __init__(self, name: str, price: int, temperature: int) -> None:
        super().__init__(name, price)
        self._temperature = temperature

class Breakfast(MenuItem):
    def __init__(self, name: str, price: int, quantity: int) -> None:
        super().__init__(name, price)
        self._quantity = quantity

class MedioPago:
    def __init__(self):
        pass

    def pagar(self, monto):
        raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(MedioPago):
    def __init__(self, numero, cvv):
        super().__init__()
        self._numero = numero
        self._cvv = cvv

    def pagar(self, monto):
        print(f"Pagando $ {monto:,} con tarjeta ({self._numero[-4:]})")
        print("Realizando transacción...")
        time.sleep(2)
        print("Transacción exitosa.")

class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self._monto_entregado = monto_entregado

    def pagar(self, monto):
        print("Contando dinero...")
        time.sleep(2)
        if self._monto_entregado >= monto:
            print(f"Pago realizado en efectivo. Cambio: ${self._monto_entregado - monto:,}")
        else:
            print(f"Fondos insuficientes. Faltan ${monto - self._monto_entregado:,} para completar el pago.")

# Ejemplo de uso

# Bebidas
cafe = Drink("Café", 2000, 200)  # 200 ml
jugo_lulo = Drink("Jugo de Lulo", 2500, 250)  # 250 ml
agua_panela = Drink("Agua de panela", 1500, 300)  # 300 ml

# Platos principales
arepas = MainDishes("Arepa con queso", 8000, ["arepa", "queso"])
bandeja_paisa = MainDishes(
    "Bandeja Paisa",
    25000,
    ["arroz", "frijoles", "huevo", "carne", "chicharrón", "aguacate"],
)
sancocho = MainDishes(
    "Sancocho de gallina", 15000, ["gallina", "yuca", "papas", "plátano"]
)
ajiaco = MainDishes("Ajiaco", 18000, ["pollo", "papas", "mazorca", "guasca"])
empanadas = MainDishes("Empanadas", 3500, ["harina de maíz", "carne", "papas"])
bandeja_pescado = MainDishes(
    "Bandeja De Pescado",
    22000,
    ["arroz", "pescado frito", "patacones", "ensalada", "aguacate"],
)
tamal = MainDishes(
    "Tamales", 7000, ["masa de maíz", "carne", "pollo", "papa", "zanahoria"]
)

# Postres
arroz_con_leche = Dessert("Arroz con Leche", 3500, 200)  # 200 g
tres_leches = Dessert("Pastel Tres Leches", 5000, 180)  # 180 g
torta_de_guanabana = Dessert("Torta de Guanábana", 4500, 150)  # 150 g

# Ensaladas
ensalada_mixta = Salads("Ensalada Mixta", 4000, "tazón")
ensalada_de_pasta = Salads("Ensalada de Pasta", 5000, "plato")

# Sopas
sopa_de_lentejas = Soups("Sopa de Lentejas", 6000, 1)  # Caliente
sopa_de_carne = Soups("Sopa de Carne", 8000, 1)  # Caliente
sopa_de_vegetales = Soups("Sopa de Vegetales", 7000, 1)  # Caliente

# Desayunos
arepas_con_huevo = Breakfast("Arepas con Huevo", 5000, 2)  # 2 unidades
calentado = Breakfast("Calentado", 7000, 1)  # 1 porción
empanadas_con_aji = Breakfast("Empanadas con Aji", 4500, 3)  # 3 unidades

print("---Orden 1---")
tarjeta = Tarjeta("1234567890123456", 453)
cliente = Order(tarjeta, student=True)
cliente.add_item(arepas, 2)
cliente.add_item(cafe, 1)
cliente.add_item(arroz_con_leche, 1)
cliente.promos()
cliente.print_order()
cliente.pagar()

print("\n\n---Orden 2---")
efectivo = Efectivo(1000)
cliente2 = Order(efectivo)
cliente2.add_item(ajiaco, 1)
cliente2.add_item(jugo_lulo, 1)
cliente2.add_item(sancocho, 1)
cliente2.add_item(tres_leches, 1)
cliente2.add_item(arepas_con_huevo, 5)
cliente2.add_item(empanadas, 2)
cliente2.add_item(torta_de_guanabana, 1)
cliente2.add_item(agua_panela, 1)
cliente2.add_item(arepas_con_huevo, 1)


cliente2.promos()
cliente2.print_order()
cliente2.pagar()
