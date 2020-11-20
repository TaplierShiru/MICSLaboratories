import random


class UniformGenerator:
    """
    Generate uniform dist

    """

    @staticmethod
    def generate_single(a, b) -> int:
        return int(random.random() * (b - a) + a)

