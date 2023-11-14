import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.title("Мое приложение")

# Создаем данные для гистограммы
x = [0, 1, 2, 3, 4]
data = [20, 40, 10, 30, 50]

# Создаем график
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.bar(range(len(data)), data)

# Устанавливаем позиции делений на оси x
ax.set_xticks(x)

# Устанавливаем подписи для оси x
labels = ['A', 'B', 'C', 'D', 'E']
ax.set_xticklabels(labels)

# Добавляем подписи к осям
ax.set_xlabel('Название оси X')
ax.set_ylabel('Название оси Y')

# Создаем виджет Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()