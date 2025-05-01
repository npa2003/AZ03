import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0          # Среднее значение
std_dev = 1       # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')

# Добавление линии плотности нормального распределения для сравнения
x = np.linspace(-4, 4, 100)
plt.plot(x, 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean)/std_dev)**2),
         color='red', linewidth=2)

# Настройка графика
plt.title('Гистограмма нормального распределения', fontsize=16)
plt.xlabel('Значения', fontsize=14)
plt.ylabel('Плотность вероятности', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Отображение графика
plt.show()