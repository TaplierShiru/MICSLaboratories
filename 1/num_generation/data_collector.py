import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from .generate_numbers import FILE_NAME, generate_numbers

# Минимальное значение, если количество элементов будет ниже него,
# То соседние значения в гистограмме будут соединяться
MIN = 10


class DataCollector():

    @staticmethod
    def cumulat_dist_function(x, avg, variance, alpha, beta):
        """
        Считает функцию усеченного распределения

        """
        x_norm = (x - avg) / variance
        Z = norm.cdf(beta) - norm.cdf(alpha)
        return (norm.cdf(x_norm) - norm.cdf(alpha)) / Z

    def __init__(self):
        # Переменные для распределения
        self.number_var = None
        self.N = 15 #int(1 + 3.22 * math.log10(n)) + 1
        self.R = None
        self.u = None
        self.avg = None
        self.variance = None

        self.a = None
        self.b = None
        self.alpha = None
        self.beta = None

        self.prob_list = None
        self.friq_list = None
        self.frequency = None
        self.x_watch = None

    def collect_data_from_dist(self):
        # Загружаем выборку в массив
        numbers = self.read_numbers()

        n = len(numbers)
        # Сортируем выборку и получаем вариационный ряд
        self.numbers_var = sorted(numbers)

        # Находим размах
        self.R = self.numbers_var[-1] - self.numbers_var[0]

        # Длину интервалов
        u = self.R / self.N

        # Находим среднее и среднеквадратичное отклонение.
        self.avg = sum(self.numbers_var) / n
        self.variance = sum([(x_i - self.avg) ** 2 for x_i in self.numbers_var]) / n

        # Параметр распределения
        self.a = self.numbers_var[0]
        self.b = self.numbers_var[-1]
        self.alpha = (self.a - self.avg) / self.variance
        self.beta = (self.b - self.avg) / self.variance

        # Каждый элемент:
        # tuple (левая_граница,
        #        правая_граница,
        #        частота_элементов,
        #        высота_гистограммы,
        #        теорит_вероятность
        # )
        frequency = []

        for i in range(self.N):
            if i == 0:
                left_limit = self.numbers_var[0]
                right_limit = self.numbers_var[0] + u
                frequency.append([left_limit, right_limit, 0, 0.0, 0.0])
            else:
                left_limit = frequency[-1][1]
                right_limit = frequency[-1][1] + u
                frequency.append([left_limit, right_limit, 0, 0.0, 0.0])

            # Подсчитываем количество цифр в данном интервале
            for number in self.numbers_var:
                if right_limit > number >= left_limit:
                    frequency[-1][2] += 1

            # Подсчитываем высоту гистограммы
            table_high = frequency[-1][2] / (n * (right_limit - left_limit))
            frequency[-1][3] = table_high



            # Считаем теор. вероятность попадения
            right = self.cumulat_dist_function(
                right_limit,
                avg=self.avg,
                variance=self.variance,
                alpha=self.alpha,
                beta=self.beta
            )
            left = self.cumulat_dist_function(
                left_limit,
                avg=self.avg,
                variance=self.variance,
                alpha=self.alpha,
                beta=self.beta
            )
            frequency[-1][-1] = right - left

        # Проводим чистку, если где-то меньше MIN элементов, объединяем этот интервал
        i = self.N - 1
        while i > 0:
            if frequency[i][2] < MIN:
                frequency[i - 1][2] += frequency[i][2]
                frequency[i - 1][1] = frequency[i][1]

                del frequency[i]
                i -= 1

                left_limit = frequency[i][0]
                right_limit = frequency[i][1]
                table_high = frequency[i][2] / (n * (right_limit - left_limit))
                frequency[i][3] = table_high

                right = self.cumulat_dist_function(
                    right_limit,
                    avg=self.avg,
                    variance=self.variance,
                    alpha=self.alpha,
                    beta=self.beta
                )
                left = self.cumulat_dist_function(
                    left_limit,
                    avg=self.avg,
                    variance=self.variance,
                    alpha=self.alpha,
                    beta=self.beta
                )

                frequency[i][-1] = right - left
            else:
                i -= 1

        self.prob_list = [round(elem[-1], 6) for elem in frequency]
        self.friq_list = [elem[2] for elem in frequency]
        # Считаем хи-квадрат
        self.x_watch = 0.0
        for elem in frequency:
            self.x_watch += ((elem[2] - n * elem[-1]) ** 2) / (n * elem[-1])

        self.frequency = frequency

    def bar(self, array, name_column, scale_y=1.0, scale_x=1.0):
        dpi = 100
        h,w = (500, 500)

        figsuze = w / float(dpi), h / float(dpi)

        fig = plt.figure(frameon=False, figsize=figsuze, dpi=dpi)
        ax = fig.add_axes([0, 0, 1, 1])

        x = [i * scale_x for i in range(len(array))]
        y = [i * scale_y for i in array]
        ax.bar(x, height=y, color='r', width=scale_x)
        ax.plot(x, y, color='b')

        for name, x_single, y_single in zip(name_column, x, y):
            ax.annotate(f'{name}', xy=(x_single, y_single), textcoords='data')

        fig.canvas.draw()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = np.reshape(data, (h, w, 3))
        plt.close('all')
        return data

    def draw_histograme(self):
        assert self.frequency is not None
        # Рисуем гистограмму
        return self.bar(
            [freq[-2] for freq in self.frequency],
            [round(freq[-2], 6) for freq in self.frequency],
            scale_y=10.0
        )

    def draw_dist(self):
        assert self.frequency is not None
        dpi = 100
        h,w = (500, 500)
        figsuze = w / float(dpi), h / float(dpi)

        numbers = sorted(self.read_numbers())
        dist_value = [
            self.cumulat_dist_function(elem, self.avg, self.variance, self.alpha, self.beta)
            for elem in numbers
        ]
        x = np.linspace(self.a, self.b, num=len(numbers))
        x = x.tolist()

        fig = plt.figure(frameon=False, figsize=figsuze, dpi=dpi)
        plt.plot(x, dist_value)
        plt.xlabel('Значение элементов')
        plt.ylabel('Вероятность')

        fig.canvas.draw()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = np.reshape(data, (h, w, 3))
        plt.close('all')
        return data

    def draw_numbers(self):
        assert self.frequency is not None
        dpi = 100
        h,w = (500, 500)
        figsuze = w / float(dpi), h / float(dpi)

        numbers = self.read_numbers()
        x = [i for i in range(len(numbers))]

        fig = plt.figure(frameon=False, figsize=figsuze, dpi=dpi)
        plt.plot(x, numbers, marker='o', color='r', ls='')
        plt.xlabel('Номер элемента')
        plt.ylabel('Значение')

        fig.canvas.draw()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = np.reshape(data, (h, w, 3))
        plt.close('all')
        return data

    def regenerate_numbers(self, n: int, a: float, b: float, mu: float, std: float):
        generate_numbers(n, a, b, mu, std)

    def read_numbers(self) -> list:
        with open(FILE_NAME) as fp:
            numbers = fp.readlines()
            numbers = [float(i[:-2]) for i in numbers]

        return numbers
