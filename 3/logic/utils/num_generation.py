import random


class UniformGenerator:
    """
    Моделирует равномерное распределение

    """

    @staticmethod
    def generate_single(a, b) -> int:
        return int(random.random() * (b - a) + a)

