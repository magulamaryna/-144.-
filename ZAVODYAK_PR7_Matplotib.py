import matplotlib.pyplot as plt

labels = ['Цукор', 'Какао', 'Молоко', 'Інше']
values = [20, 30, 25, 25]
colors = ['yellow', 'green', 'red', 'blue']
explode = [0.4, 0, 0, 0]

plt.figure(figsize=(7, 7))
plt.title('Кругова діаграма')

plt.pie(values,
        labels=labels,
        colors=colors,
        explode=explode,
        shadow=True,
        autopct='%1.1f%%',
        startangle=120)

plt.axis('equal')
plt.legend()
plt.show()