from abc import ABC, abstractmethod
import math

class Figure(ABC):
    """
    Abstract base class representing a geometric figure.
    """

    @property
    @abstractmethod
    def area(self) -> float:
        """Abstract method to calculate the area of the figure."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method to calculate the perimeter of the figure."""
        pass

    def __eq__(self, other: "Figure") -> bool:
        """Compare figures based on their areas."""
        return self.area == other.area

    def __lt__(self, other: "Figure") -> bool:
        """Compare figures based on their areas."""
        return self.area < other.area

    def __add__(self, other: "Figure") -> "Figure":
        """Combine figures to create a new figure with
        the sum of their areas."""
        if not isinstance(other, Figure):
            raise TypeError("Operands must be instances of Figure")
        return self.__class__(self.area + other.area)

    def __str__(self) -> str:
        """String representation of the figure."""
        return f"""
        {self.__class__.__name__}
        Area: {self.area}
        Perimeter: {self.perimeter}
        """


class Square(Figure):
    """
    Class representing a square figure.
    """

    def __init__(self, side_length: float) -> None:
        self.side_length = side_length

    @property
    def area(self) -> float:
        """Calculate the area of the square."""
        return self.side_length ** 2

    def perimeter(self) -> float:
        """Calculate the perimeter of the square."""
        return 4 * self.side_length


class Circle(Figure):
    """
    Class representing a circle figure.
    """

    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius


class Triangle(Figure):
    """
    Class representing a triangle figure.
    """

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    @property
    def area(self) -> float:
        """Calculate the area of the triangle."""
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle."""
        # Assuming it's an equilateral triangle
        return 3 * self.base
