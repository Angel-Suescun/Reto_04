# Reto#04 

# Ejercicio De Clase

## Clases

### `Point`
Representa un punto en el plano bidimensional con coordenadas \(x\) y \(y\).

#### Métodos
- `__init__(x: float, y: float)`: Inicializa el punto con las coordenadas \(x\) e \(y\).
- `compute_distance(other_point: 'Point') -> float`: Calcula la distancia entre el punto actual y otro punto.
- `set_coordinates(x: float, y: float)`: Establece nuevas coordenadas para el punto.
- `get_x() -> float`: Obtiene la coordenada \(x\).
- `get_y() -> float`: Obtiene la coordenada \(y\).

### `Line`
Representa una línea definida por dos puntos (inicio y fin).

#### Métodos
- `__init__(start_point: Point, end_point: Point)`: Inicializa una línea con dos puntos, calculando su longitud.

### `Shape`
Clase base para todas las figuras geométricas, con métodos comunes para manejar vértices, aristas y cálculos de perímetros y áreas.

#### Métodos
- `set_vertices(*args: Point)`: Establece los vértices de la figura.
- `get_vertices() -> list`: Obtiene los vértices de la figura.
- `set_edges(*args: Line)`: Establece las aristas de la figura.
- `get_edges() -> list`: Obtiene las aristas de la figura.
- `set_inner_angles(inner_angles: list)`: Establece los ángulos interiores de la figura.
- `get_inner_angles() -> list`: Obtiene los ángulos interiores de la figura.
- `compute_area()`: Método abstracto que debe ser implementado en las subclases para calcular el área.
- `compute_perimeter() -> float`: Calcula el perímetro de la figura sumando las longitudes de sus aristas.

### `Rectangle` (subclase de `Shape`)
Representa un rectángulo con cuatro vértices y cuatro aristas.

#### Métodos
- `__init__(vertices: list, edges: list)`: Inicializa el rectángulo con 4 vértices y 4 aristas.
- `compute_area()`: Calcula el área del rectángulo como el producto de dos lados.

### `Square` (subclase de `Rectangle`)
Representa un cuadrado, que es un caso especial de rectángulo con todos los lados iguales.

#### Métodos
- `compute_area()`: Calcula el área del cuadrado como el cuadrado de la longitud de un lado.

### `Triangle` (subclase de `Shape`)
Representa un triángulo con tres vértices, tres aristas y, opcionalmente, ángulos interiores.

#### Métodos
- `__init__(vertices: list, edges: list, inner_angles: list)`: Inicializa el triángulo con 3 vértices y 3 aristas.
- `compute_area()`: Calcula el área del triángulo utilizando la fórmula de Herón.

### Triángulos específicos
- **`Isosceles`, `Equilateral`, `Scalene`, `RightTriangle`**: Subclases de `Triangle` que representan tipos específicos de triángulos (isosceles, equilátero, escaleno, y rectángulo respectivamente).

## Código

```python
import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        """Inicializa un punto con coordenadas x e y."""
        self._x = x
        self._y = y

    def compute_distance(self, other_point: 'Point') -> float:
        """Calcula la distancia a otro punto."""
        return math.sqrt((self._x - other_point._x) ** 2 + (self._y - other_point._y) ** 2)

    def set_coordinates(self, x: float, y: float) -> None:
        """Establece nuevas coordenadas x e y para el punto."""
        self._x = x
        self._y = y

    def get_x(self) -> float:
        """Obtiene la coordenada x del punto."""
        return self._x

    def get_y(self) -> float:
        """Obtiene la coordenada y del punto."""
        return self._y


class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        """Inicializa un segmento de línea definido por dos puntos."""
        self.start_point = start_point
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)


class Shape:
    def __init__(self, is_regular: bool = True) -> None:
        """Inicializa una figura geométrica con regularidad opcional."""
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []

    def set_vertices(self, *args: Point) -> None:
        """Establece los vértices de la figura, verificando que sean válidos."""
        if all(isinstance(vertex, Point) for vertex in args):
            self._vertices = list(args)
        else:
            raise ValueError("Todos los vértices deben ser objetos de tipo Point.")

    def get_vertices(self) -> list:
        """Obtiene los vértices de la figura."""
        return self._vertices

    def set_edges(self, *args: Line) -> None:
        """Establece las aristas de la figura, verificando que sean válidas."""
        if all(isinstance(line, Line) for line in args):
            self._edges = list(args)
        else:
            raise ValueError("Todas las aristas deben ser objetos de tipo Line.")

    def get_edges(self) -> list:
        """Obtiene las aristas de la figura."""
        return self._edges

    def set_inner_angles(self, inner_angles: list = None) -> None:
        """
        Establece los ángulos interiores de la figura. 
        Se calculan automáticamente si es regular.
        """
        if self._is_regular:
            n = len(self._vertices)
            for i in range(n):
                self._inner_angles = [(180 * (n - 2)) / n ]
        else:
            self._inner_angles = inner_angles

    def get_inner_angles(self) -> list:
        """Obtiene los ángulos interiores de la figura."""
        return self._inner_angles

    def compute_area(self) -> float:
        """Calcula el área de la figura (debe ser implementado en subclases)."""
        raise NotImplementedError(
            "El método para calcular el área debe implementarse en las subclases.")

    def compute_perimeter(self) -> float:
        """Calcula el perímetro de la figura como la suma de sus aristas."""
        return sum(edge.length for edge in self._edges)


class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list) -> None:
        """Inicializa un rectángulo con cuatro vértices y cuatro aristas."""
        super().__init__(is_regular=True)
        if len(vertices) == 4 and len(edges) == 4:
            self.set_vertices(*vertices)
            self.set_edges(*edges)
        else:
            raise ValueError("Un rectángulo debe tener 4 vértices y 4 aristas.")

    def compute_area(self) -> float:
        """Calcula el área del rectángulo como el producto de dos lados."""
        return self._edges[0].length * self._edges[1].length


class Square(Rectangle):
    def compute_area(self) -> float:
        """
        Calcula el área del cuadrado como el cuadrado de la longitud de un lado.
        """
        return self._edges[0].length ** 2


class Triangle(Shape):
    def __init__(self,
                is_regular: bool = True, 
                vertices: list = [], 
                edges: list = [], 
                inner_angles: list = None
                ) -> None:
        """
        Inicializa un triángulo con tres vértices, tres aristas y ángulos.
        """
        super().__init__(is_regular)
        if len(vertices) == 3 and len(edges) == 3:
            self.set_vertices(*vertices)
            self.set_edges(*edges)
            self.set_inner_angles(inner_angles)
        else:
            raise ValueError("Un triángulo debe tener 3 vértices y 3 aristas.")

    def compute_area(self) -> float:
        """Calcula el área del triángulo utilizando la fórmula de Herón."""
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self._edges[0].length) 
                         * (s - self._edges[1].length) 
                         * (s - self._edges[2].length)
                )
    

class Isosceles(Triangle):
    def __init__(self, is_regular: bool = False, 
                vertices: list =[], 
                edges: list = [], 
                inner_angles: list = None) -> None:
        """Inicializa un triángulo isósceles."""
        super().__init__(is_regular, vertices, edges, inner_angles)


class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list) -> None:
        """Inicializa un triángulo equilátero."""
        super().__init__(vertices, edges)


class Scalene(Triangle):
    def __init__(self, is_regular: bool = False, 
                vertices: list =[], 
                edges: list = [], 
                inner_angles: list = None) -> None:
        """Inicializa un triángulo isósceles."""
        super().__init__(is_regular, vertices, edges, inner_angles)


class RightTriangle(Triangle):
    def __init__(self, is_regular: bool = False, 
                vertices: list =[], 
                edges: list = [], 
                inner_angles: list = None) -> None:
        """Inicializa un triángulo isósceles."""
        super().__init__(is_regular, vertices, edges, inner_angles)



# Ejemplo de uso
p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(4, 3)
p4 = Point(0, 3)

l1 = Line(p1, p2)
l2 = Line(p2, p3)
l3 = Line(p3, p4)
l4 = Line(p4, p1)

rectangle = Rectangle(vertices=[p1, p2, p3, p4], edges=[l1, l2, l3, l4])
print(f"Área del rectángulo: {rectangle.compute_area()}")
print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")

square = Square(vertices=[p1, p2, p3, p4], edges=[l1, l2, l3, l4])
print(f"Área del cuadrado: {square.compute_area()}")
print(f"Perímetro del cuadrado: {square.compute_perimeter()}")

p5 = Point(0, 0)
p6 = Point(4, 0)
p7 = Point(2, 3)

l5 = Line(p5, p6)
l6 = Line(p6, p7)
l7 = Line(p7, p5)

triangle = Triangle(vertices=[p5, p6, p7], edges=[l5, l6, l7])
print(f"Área del triángulo: {(triangle.compute_area()).__round__(2)}")
print(f"Perímetro del triángulo: {triangle.compute_perimeter().__round__(2)}")
```

#

# Ejercicio De Restaurante
# Función `compound_order`

La función `compound_order` aplica descuentos a las órdenes en función de los tipos de artículos que contienen. Se ejecuta dentro de las clases `MenuItem` y `Order`.

### Descuento en Bebidas
- **10% de descuento en Bebidas**: Si la orden incluye un `MainDish` (plato principal) y una `Drink` (bebida), se aplica un descuento del 10% a la bebida.

### Descuento en Postres
- **5% de descuento en Postres**: Si la orden incluye un `Breakfast` (desayuno) y un `Dessert` (postre), se aplica un descuento del 5% en el postre.


---

# Funciones `get` y `set`

Se añaden funciones `get` y `set` en las subclases específicas de la clase `MenuItem` (como `Drink`, `MainDish`, `Dessert`, etc.) para acceder y modificar los atributos de los objetos. Estas funciones permiten un control más detallado sobre los elementos del menú.

---

# Integración del código de medio de pago

El código permite realizar pagos utilizando diferentes medios, integrados a través de las clases `MedioPago`, `Tarjeta` y `Efectivo`.

```python
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

    def pagar(self, order):
        order.type_payment.pagar(order.total)
        


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
            print(f"Pago realizado en efectivo. Cambio: $ 
                {(self.monto_entregado - monto):,}")

        else:
            print(f"Fondos insuficientes. Faltan $ 
                {(monto - self.monto_entregado):,} para completar el pago.")


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

```
