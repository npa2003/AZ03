import numpy as np
import matplotlib.pyplot as plt

# Генерируем два набора случайных данных
x = np.random.rand(50)  # 50 случайных чисел по оси X
y = np.random.rand(50)  # 50 случайных чисел по оси Y

# Создаем диаграмму рассеяния
plt.figure(figsize=(8, 6))  # Задаем размер графика
plt.scatter(x, y, color='blue', alpha=0.6, edgecolors='w', s=80)  # s - размер точек

# Добавляем заголовок и подписи осей
plt.title('Диаграмма рассеяния случайных данных', fontsize=14)
plt.xlabel('X значения', fontsize=12)
plt.ylabel('Y значения', fontsize=12)

# Добавляем сетку для лучшей читаемости
plt.grid(True, linestyle='--', alpha=0.5)

# Показываем график
plt.show()