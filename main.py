from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """Базовый класс фигуры, который является интерфейсом
    """

    @property
    @abstractmethod
    def area(self) -> float:
        pass 


class Circle(Figure):
    """Класс круга
    
    Attributes: 
        radius: радиус круга
    """
    
    def __init__(self, radius: int | float):
        self.radius = radius
        
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом!")
        if type(radius) not in (int, float):
            raise TypeError("Радиус должен быть целым или действительным числом!")


    @property
    def area(self) -> float:
        """Вычисляет площадь круга по формуле S = pi * r^2

        Returns:
            Площадь круга
        """
        return math.pi * self.radius**2 


class Triangle(Figure):
    """Класс треугольника

    Attributes:
        a: первая сторона треугольника
        b: вторая сторона треугольника
        c: третья сторона треугольника
    """
    
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a = a 
        self.b = b 
        self.c = c 

        if not all(type(side) in (int, float) for side in (a,b,c)):
            raise TypeError("Стороны должны быть целыми или действительными числами!")

        if a+b <= c or a+c <= b or b+c <= a: # Проверка на неравенство треугольника
            raise ValueError("Треугольник является вырожденным!")

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть положительными числами!")
        

    @property
    def area(self) -> float:
        """Вычисляет площадь треугольника

        Returns:
            Площадь треугольника
        """
        p = (self.a+self.b+self.c)/2 # Полупериметр треугольника
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5  # Вычисяем площадь по формуле Герона
    

    def is_right(self) -> bool: 
        """Определяет является ли треугольник прямоугольным

        Returns:
            True - если треугольник прямоугольный
            False - если треугольник непрямоугольный
        """

        # Сортируем стороны по неубыванию
        sides = [self.a, self.b, self.c] 
        sides.sort() 

        return sides[0]**2 + sides[1]**2 == sides[2]**2 # Проверяем по теореме Пифагора
