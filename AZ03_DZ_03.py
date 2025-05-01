import pandas as pd
import matplotlib.pyplot as plt

#агрузка данных из CSV-файла
df = pd.read_csv('svet.csv')

#проверка первых строк данных
print("Первые 5 строк данных:")
print(df.head())

#расчет средней стоимости
average_price = df['Стоимость'].mean()
print(f"\nСредняя стоимость светильника: {average_price:.2f} руб.")

#построение гистограммы цен
plt.figure(figsize=(12, 6))
plt.hist(df['Стоимость'], bins=20, color='skyblue', edgecolor='black')

#внешний вид графика
plt.title('Распределение цен на светильники', fontsize=16)
plt.xlabel('Цена (руб)', fontsize=14)
plt.ylabel('Количество светильников', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

#добавление линии среднего значения
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=2,
            label=f'Средняя цена: {average_price:.2f} руб.')
plt.legend()

#график
plt.show()