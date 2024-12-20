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
        self._start_point = start_point
        self._end_point = end_point
        self._length = start_point.compute_distance(end_point)

    def get_length(self) -> float:
        """Obtiene la longitud de la línea."""
        return self._length


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
            self._inner_angles = [(180 * (n - 2)) / n] * n
        else:
            print("La figura no es regular, los triángulos tiene funcion especial")

    def get_inner_angles(self) -> list:
        """Obtiene los ángulos interiores de la figura."""
        return self._inner_angles

    def compute_area(self) -> float:
        """Calcula el área de la figura (debe ser implementado en subclases)."""
        raise NotImplementedError(
            "El método para calcular el área debe implementarse en las subclases.")

    def compute_perimeter(self) -> float:
        """Calcula el perímetro de la figura como la suma de sus aristas."""
        return sum(edge.get_length() for edge in self._edges)


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
        return self._edges[0].get_length() * self._edges[1].get_length()


class Square(Rectangle):
    def compute_area(self) -> float:
        """
        Calcula el área del cuadrado como el cuadrado de la longitud de un lado.
        """
        return self._edges[0].get_length() ** 2


class Triangle(Shape):
    def __init__(self,
                is_regular: bool = True, 
                vertices: list = [], 
                edges: list = [], 
                ) -> None:
        """
        Inicializa un triángulo con tres vértices, tres aristas y ángulos.
        """
        super().__init__(is_regular)
        if len(vertices) == 3 and len(edges) == 3:
            self.set_vertices(*vertices)
            self.set_edges(*edges)
        else:
            raise ValueError("Un triángulo debe tener 3 vértices y 3 aristas.")

    def compute_area(self) -> float:
        """Calcula el área del triángulo utilizando la fórmula de Herón."""
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self._edges[0].get_length()) 
                         * (s - self._edges[1].get_length()) 
                         * (s - self._edges[2].get_length())
                )
    def compute_inner_angles(self) -> None:
        """Calcula los ángulos interiores del triángulo."""
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
        cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

        radians_A = math.acos(cos_A)
        radians_B = math.acos(cos_B)
        radians_C = math.acos(cos_C)

        self._inner_angles = [
            math.degrees(radians_A),
            math.degrees(radians_B), 
            math.degrees(radians_C)]



class Isosceles(Triangle):
    def __init__(self, is_regular: bool = False, 
            vertices: list =[], 
            edges: list = [], ) -> None:
        """Inicializa un triángulo isósceles."""
        super().__init__(is_regular, vertices, edges)


class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list) -> None:
        """Inicializa un triángulo equilátero."""
        super().__init__(vertices, edges)


class Scalene(Triangle):
    def __init__(self, is_regular: bool = False, 
        vertices: list =[], 
        edges: list = []) -> None:
        """Inicializa un triángulo escaleno."""
        super().__init__(is_regular, vertices, edges)


class RightTriangle(Triangle):
    def __init__(self, is_regular: bool = False, 
        vertices: list =[], 
        edges: list = [], 
        inner_angles: list = None) -> None:
        """Inicializa un triángulo rectangulo."""
        super().__init__(is_regular, vertices, edges)


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
print(f"Área del triángulo: {triangle.compute_area().__round__(2)}")
print(f"Perímetro del triángulo: {triangle.compute_perimeter().__round__(2)}")
