import logging
import math


class Circle:
    """
    This class represents a circle with attributes like radius,
    diameter, and area.
    """

    def __init__(self, radius: float = 1.0) -> None:
        """
        Initialize Circle with default radius of 1.0 if not
        provided.
        Calculate diameter and area based on the given radius.
        """
        self._radius: float = radius
        self._diameter: float = radius * 2
        self._area: float = math.pi * (radius**2)

        logging.info(f"Circle inialized with radius: {self._radius}")

    def __str__(self) -> str:
        """
        Printing current radius.
        """
        return f"""
        Circle properties:
        radius: {self._radius}
        diameter: {self._diameter}
        area: {self._area}
        """

    def __eq__(self, other):
        """
        Check if two Circle instances are equal based on their
        radii.
        """
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __ne__(self, other):
        """
        Check if two Circle instances are not equal based
        on their radii.
        """
        if isinstance(other, Circle):
            return self.radius != other.radius
        return NotImplemented

    def __lt__(self, other):
        """
        Check if the radius of the current Circle instance
        is less than the radius of another Circle instance.
        """
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        """
        Check if the radius of the current Circle instance
        is less than or equal to the radius of another Circle
        instance.
        """
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __gt__(self, other):
        """
        Check if the radius of the current Circle instance
        is greater than the radius of another Circle instance,
        or if the area of the current Circle instance is
        greater than the area of another Circle instance.
        """
        if isinstance(other, Circle):
            return (self.radius > other.radius) or (self.area > other.area)
        return NotImplemented

    def __ge__(self, other):
        """
        Check if the radius of the current Circle instance
        is less than the radius of another Circle instance.
        """
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def __add__(self, other):
        """
        Enable addition between Circle and Square instances.
        """
        if isinstance(other, Circle):
            combined_area = self.area + other.area
            combined_radius = math.sqrt(combined_area / math.pi)
            return Circle(combined_radius)
        elif isinstance(other, Square):
            return Square(math.sqrt(self.area + other.area))
        else:
            raise TypeError("Objects must be instances of Circle or Square")

    @property
    def radius(self) -> float:
        """
        Get the radius of the circle.
        """
        return self._radius

    @radius.setter
    def radius(self, new_radius: float) -> None:
        """
        Set the radius of the circle.
        Calculate diameter and area based on the new radius.
        """
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = new_radius
        self._diameter = new_radius * 2
        self._area = math.pi * (new_radius**2)
        logging.info(f"Radius set to: {self._radius}")

    @property
    def diameter(self) -> float:
        """
        Get the diameter of the circle.
        """
        return self._diameter

    @diameter.setter
    def diameter(self, new_diameter: float) -> None:
        """
        Set the diameter of the circle.
        Calculater radius and area based on the new diamter.
        """
        if new_diameter < 0:
            raise ValueError("Diameter cannot be negative")
        self._diameter = new_diameter
        self._radius = new_diameter / 2
        self._area = math.pi * ((new_diameter / 2) ** 2)
        logging.info(f"Diameter set to: {self._diameter}")

    @property
    def area(self) -> float:
        """
        Get the area of the circle.
        """
        return round(self._area, 2)

    @area.setter
    def area(self, new_area: float) -> None:
        """
        Set the area of the circle.
        Calculate radius and diameter based on the new area.
        """
        if new_area < 0:
            raise ValueError("Area cannot be negative")
        self._area = new_area
        self._radius = math.sqrt(new_area / math.pi)
        self._diameter = self._radius * 2
        logging.info(f"Area set to: {self._area}")


class Square:
    def __init__(self, side):
        """
        Initialize a Square instance with a specified side length.
        Calculate and assign the area based on the given sidelength.
        """
        self.side = side
        self.area = side**2

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"Square({self.side})"

    def __eq__(self, other):
        """
        Check if two Square instances are equal based on their
        areas.
        """
        if isinstance(other, Square):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        """
        Check if two Square instances are not equal based
        on their areas.
        """
        if isinstance(other, Square):
            return self.area != other.area
        return NotImplemented

    def __lt__(self, other):
        """
        Check if the area of the current Square instance
        is less than the area of another Square instance.
        """
        if isinstance(other, Square):
            return self.area < other.area
        return NotImplemented

    def __le__(self, other):
        """
        Check if the area of the current Square instance
        is less than or equal to the area of another Square instance.
        """
        if isinstance(other, Square):
            return self.area <= other.area
        return NotImplemented

    def __gt__(self, other):
        """
        Check if the area of the current Square instance
        is greater than the area of another Square instance.
        """
        if isinstance(other, Square):
            return self.area > other.area
        return NotImplemented

    def __ge__(self, other):
        """
        Check if the area of the current Square instance
        is greater than or equal to the area of another
        Squareinstance.
        """
        if isinstance(other, Square):
            return self.area >= other.area
        return NotImplemented

    def __add__(self, other):
        """
        Add two Square instances to create a new Square with
        an area calculated based on the sum of their areas.
        """
        if isinstance(other, Square):
            return Square(math.sqrt(self.area + other.area))
        elif isinstance(other, Circle):
            return Circle(math.sqrt(self.area + other.area))
        else:
            raise TypeError("Objects must be instances of Square or Circle")


if __name__ == "__main__":
    # This section will run if the script is executed directly
    # You can put testing or usage examples here
    c = Circle(5)
    s = Square(4)
    print("Circle area:", c.area)
    print("Square area:", s.area)
