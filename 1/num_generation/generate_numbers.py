import random
from scipy.stats import norm
import numpy as np

FILE_NAME = 'generated_numbers.txt'


def generate_numbers(n=1000, a=0.0, b=6.0, mu=2.5, std=1.0):
	# Считаем параметры для распределения
	alpha = (a - mu) / std
	beta = (b - mu) / std

	# Возвращает рандомное число из усеченного распределения
	def get_random_number():
		x = norm.cdf(alpha) + random.random() * (norm.cdf(beta) - norm.cdf(alpha))
		x = norm.ppf(x) * std + mu
		return x

	# Генерируем значения и сохраняем в файл
	with open(FILE_NAME, 'w') as fp:
		for i in range(n):
			fp.write(str(get_random_number()) + '\n')


