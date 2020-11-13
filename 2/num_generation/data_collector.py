import random


class DataCollector:
    """
    Моделирует равномерное распределение

    """
    @staticmethod
    def cumulat_dist_function(x: float, a: float, b: float):
        """
        Считает функцию распределения

        """
        return (x - a) / (b - a)

    def __init__(self, a, b):
        self.a_theor = a
        self.b_theor = b

    def generate_single(self) -> float:
        return random.random() * (self.b_theor - self.a_theor) + self.a_theor

    def generate_numbers(self, n: int) -> list:
        numbers = []

        for i in range(n):
            numbers.append(self.generate_single())

        return numbers

