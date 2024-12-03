import matplotlib.pyplot as plt

fig, ax = plt.subplots() #Создаем фигуру, содержащую 1 ось
ax.plot([3, 1, 8, 3], [6, 3, 4, 6]) #Задаем данные для оси


fig2 = plt.figure(figsize=(4, 2), facecolor='lightskyblue',
                 layout='constrained') #Задаем размеры, цвет и планировку фигуры
fig2.suptitle('A nice Matplotlib Figure') #Задаем название фигуры
ax2 = fig2.add_subplot() #Добавляем оси название
ax2.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium') #Задаем параметры названия оси
plt.show() #Выводим фигуру на экран