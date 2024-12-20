import random
import time

class MenuItem:
    """Representa un artículo del menú con un nombre y un precio."""

    def __init__(self, name: str, price: int) -> None:
        """Inicializa el artículo del menú con nombre y precio."""
        self.name = name
        self.price = price

    def calculate_total(self, order: 'Order') -> float:
        """Calcula el total de una orden aplicando descuento."""
        
        def compound_order(order) -> None:
            """Mediante de que se compone el pedido, genera un descuento."""
            # Descuento del 10% si hay un MainDish y un Drink
            if any(isinstance(item, MainDishes) for item in order.items.keys()):  # Verifica si hay MainDishes
                for key, item in order.items.items():
                    if isinstance(key, Drink):  # Si el item es una bebida
                        self.items[key] = item * 0.9  # 10% de descuento en Drink
                        print("Descuento del 10% en Drink")
                        break

            # Descuento del 5% si hay un Breakfast y un Dessert
            if any(isinstance(item, Breakfast) for item in order.items.keys()):  # Verifica si hay Breakfast
                for key, item in order.items.items():
                    if isinstance(key, Dessert):  # Si el item es un Dessert
                        order.items[key] = item * 0.95  # 5% de descuento en Dessert
                        print("Descuento del 5% en Dessert")
                        break
        
        compound_order(order)
        total = sum(order.items.values())
        total -= total * order.discount_percentage
        return total

    def print_order(self, order: 'Order') -> None:
        """Imprime los detalles de la orden y el total con descuento."""
        total = self.calculate_total(order)
        for item, price in order.items.items():
            print(f"{item.name} - {price}")
        print(f"Descuento: {order.discount_percentage * 100}%")
        print(f"Total: ${total:,} pesos")


class Order:
    """Representa una orden realizada por un cliente."""

    def __init__(self, type_payment,  student: bool = False) -> None:
        """Inicializa la orden con un descuento y una lista de artículos."""
        self.items: dict = {}  # Diccionario de artículos con cantidades
        self.discount_percentage: float = 0  # Descuento inicial
        self.student = student  # Flag para indicar si es estudiante
        self.type_payment = type_payment

    def add_item(self, item: MenuItem, quantity: int) -> None:
        """Añade un artículo a la orden multiplicado por la cantidad."""
        self.items[item] = quantity * item.price

    def calculate_total(self) -> float:
        """Calcula el total de la orden aplicando el descuento."""

        def compound_order(self) -> None:
            """Mediante de que se compone el pedido, genera un descuento."""
            # Descuento del 10% si hay un MainDish y un Drink
            if any(isinstance(item, MainDishes) for item in self.items.keys()):  # Verifica si hay MainDishes
                for key, item in self.items.items():
                    if isinstance(key, Drink):  # Si el item es una bebida
                        self.items[key] = item * 0.9  # 10% de descuento en Drink
                        print("Descuento del 10% en Drink")
                        break

            # Descuento del 5% si hay un Breakfast y un Dessert
            if any(isinstance(item, Breakfast) for item in self.items.keys()):  # Verifica si hay Breakfast
                for key, item in self.items.items():
                    if isinstance(key, Dessert):  # Si el item es un Dessert
                        self.items[key] = item * 0.95  # 5% de descuento en Dessert
                        print("Descuento del 5% en Dessert")
                        break
        
        compound_order(self)
        total = sum(self.items.values())
        total -= total * self.discount_percentage  # Aplica descuento
        return total

    def promos(self) -> None:
        """Aplica promociones y descuentos según reglas predefinidas."""
        self.discount_percentage = 0  # Restablece el descuento

        # Descuento por cantidad de artículos
        if len(self.items) >= 6:  # 6 platos o más 10% de descuento
            self.discount_percentage += 0.1

        # Descuento adicional para estudiantes
        if self.student:  # Descuento del 20% para estudiantes
            self.discount_percentage += 0.2

        # Descuento aleatorio del 100%
        if random.random() < 0.1:  # 10% de probabilidad
            self.discount_percentage = 1

    def print_order(self) -> None:
        """Imprime la orden y el total con descuento aplicado."""
        self.total = self.calculate_total()
        for item, price in self.items.items():
            print(f"{item.name} - {price}")
        print(f"Descuento: {self.discount_percentage * 100}%")
        print(f"Total: ${self.total:,} pesos")

    def pagar(self):
        self.type_payment.pagar(self.total)



class Drink(MenuItem):
    """Clase para representar una bebida del menú."""

    def __init__(self, name: str, price: int, unit: int) -> None:
        """
        Inicializa una bebida con su nombre, precio y unidad de medida(ml).
        """
        super().__init__(name, price)
        self.unit = unit

    def set_name(self, name: str) -> None:
        """Establece el nombre de la bebida."""
        self.name = name

    def set_price(self, price: int) -> None:    
        """Establece el precio de la bebida."""
        self.price = price

    def set_unit(self, unit: int) -> None:
        """Establece la unidad de medida de la bebida."""
        self.unit = unit

    def get_name(self) -> str:
        """Obtiene el nombre de la bebida."""
        return self.name
    
    def get_price(self) -> int:
        """Obtiene el precio de la bebida."""
        return self.price
    
    def get_unit(self) -> int:
        """Obtiene la unidad de medida de la bebida."""
        return self.unit

class MainDishes(MenuItem):
    """Clase para representar un plato principal del menú."""

    def __init__(self, name: str, price: int, ingredients: list) -> None:
        """
        Inicializa un plato principal con su nombre, precio e ingredientes.
        """
        super().__init__(name, price)
        self.ingredients: list = ingredients

    def set_name(self, name: str) -> None:
        """Establece el nombre del plato principal."""
        self.name = name

    def set_price(self, price: int) -> None:    
        """Establece el precio delplato principal."""
        self.price = price

    def set_ingredients(self, ingredients: list) -> None:
        """Establece los ingredientes del plato principal."""
        self.ingredients = ingredients

    def get_name(self) -> str:
        """Obtiene el nombre del plato principal."""
        return self.name
    
    def get_price(self) -> int:
        """Obtiene el precio del plato principal."""
        return self.price
    
    def get_ingredients(self) -> int:
        """Obtiene los ingredientes del plato principal."""
        return self.ingredients

class Dessert(MenuItem):
    """Clase para representar un postre del menú."""

    def __init__(self, name: str, price: int, size: int) -> None:
        """Inicializa un postre con su nombre, precio y tamaño."""
        super().__init__(name, price)
        self.size = size
    
    def set_name(self, name: str) -> None:
        """Establece el nombre del postre."""
        self.name = name

    def set_price(self, price: int) -> None:    
        """Establece el precio del postre."""
        self.price = price

    def set_size(self, size: int) -> None:
        """Establece el tamaño del postre."""
        self.size = size

    def get_name(self) -> str:
        """Obtiene el nombre del postre."""
        return self.name
    
    def get_price(self) -> int:
        """Obtiene el precio del postre."""
        return self.price
    
    def get_size(self) -> int:
        """Obtiene el tamaño del postre."""
        return self.size

class Salads(MenuItem):
    """Clase para representar una ensalada del menú."""

    def __init__(self, name: str, price: int, container: str) -> None:
        """
        Inicializa una ensalada con su nombre, precio y tipo de recipiente.
        """
        super().__init__(name, price)
        self.container = container

    def set_name(self, name: str) -> None:
        """Establece el nombre de la ensalada."""
        self.name = name

    def set_price(self, price: int) -> None:
        """Establece el precio de la ensalada."""
        self.price = price

    def set_container(self, container: str) -> None:
        """Establece el tipo de recipiente de la ensalada."""
        self.container = container

    def get_name(self) -> str:
        """Obtiene el nombre de la ensalada."""
        return self.name
    
    def get_price(self) -> int:
        """Obtiene el precio de la ensalada."""
        return self.price   
    
    def get_container(self) -> str:
        """Obtiene el tipo de recipiente de la ensalada."""
        return self.container

class Soups(MenuItem):
    """Clase para representar una sopa del menú."""

    def __init__(self, name: str, price: int, temperature: int) -> None:
        """Inicializa una sopa con su nombre, precio y temperatura."""
        super().__init__(name, price)
        self.temperature = temperature  # 1: caliente, 2: frío

    def set_name(self, name: str) -> None:
        """Establece el nombre de la sopa."""
        self.name = name

    def set_price(self, price: int) -> None:
        """Establece el precio de la sopa."""
        self.price = price

    def set_temperature(self, temperature: int) -> None:
        """Establece la temperatura de la sopa."""
        self.temperature = temperature
    
    def get_name(self) -> str:
        """Obtiene el nombre de la sopa."""
        return self.name    
    
    def get_price(self) -> int:
        """Obtiene el precio de la sopa."""
        return self.price
    
    def get_temperature(self) -> int:
        """Obtiene la temperatura de la sopa."""
        return self.temperature

class Breakfast(MenuItem):
    """Clase para representar un desayuno del menú."""

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """Inicializa un desayuno con su nombre, precio y cantidad."""
        super().__init__(name, price)
        self.quantity = quantity

    def set_name(self, name: str) -> None:
        """Establece el nombre del desayuno."""
        self.name = name
    
    def set_price(self, price: int) -> None:
        """Establece el precio del desayuno."""
        self.price = price  
    
    def set_quantity(self, quantity: int) -> None:
        """Establece la cantidad de unidades del desayuno."""
        self.quantity = quantity

    def get_name(self) -> str:
        """Obtiene el nombre del desayuno."""
        return self.name
    
    def get_price(self) -> int:
        """Obtiene el precio del desayuno."""
        return self.price
    
    def get_quantity(self) -> int:
        """Obtiene la cantidad de unidades del desayuno."""
        return self.quantity

class MedioPago:
    def __init__(self):
        pass

    def pagar(self, monto):
        raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(MedioPago):
    def __init__(self, numero, cvv):
        super().__init__()
        self.numero = numero
        self.cvv = cvv

    def pagar(self, monto):
        print(f"Pagando $ {monto:,} con tarjeta ({self.numero[-4:]})")
        print("Realizando transacción...")
        time.sleep(2)
        print("Transacción exitosa.")

class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto):
        print(f"Contando dinero...")
        time.sleep(2)
        if self.monto_entregado >= monto:
            print(f"Pago realizado en efectivo. Cambio: $ {(self.monto_entregado - monto):,}")

        else:
            print(f"Fondos insuficientes. Faltan $ {(monto - self.monto_entregado):,} para completar el pago.")


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


# Funcionamiento de las órdenes
print("---Orden 1---")
tarjeta = Tarjeta("1234567890123456", 453)
cliente = Order(tarjeta, student=True)
cliente.add_item(arepas, 2)
cliente.add_item(cafe, 1)
cliente.add_item(bandeja_paisa, 1)
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
