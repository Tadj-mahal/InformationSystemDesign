from db import DB
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

def add_in_database():
	driver_name = driver_name_inp.get()
	distance = int(distance_inp.get())
	car = car_brand_inp.get()
	fuel_consumption = int(fuel_cons_inp.get())
	msg = database.add_new_driver(driver_name, distance, car, fuel_consumption)
	out.config(text=f"Current date and time: {msg}")

def show_cars():
	owner = owner_name_inp.get()
	msg = database.search_by_owners(owner)
	searched_cars.config(text=f"{msg}")

def show_owners():
	car = car_inp.get()
	msg = database.search_by_auto(car)
	searched_owners.config(text=f"{msg}")

def graph_drivers():
	distances = database.get_drivers_data()
	names = []
	dists = []
	for i in range(len(distances)):
		names.append(distances[i][0])
		dists.append(distances[i][1])
	graph(dists, names)

def graph_cars():
	kilometers = database.get_cars_data()
	brands = []
	fuel_consumptions = []
	for i in range(len(kilometers)):
		brands.append(kilometers[i][0])
		fuel_consumptions.append(kilometers[i][1])
	graph(fuel_consumptions, brands)

def graph(data, x_labels):
	# Создаем данные для гистограммы
	x = [int(i) for i in range(len(x_labels))]

	# Создаем график
	fig = Figure(figsize=(5, 4), dpi=100)
	ax = fig.add_subplot(111)
	ax.bar(range(len(data)), data)

	# Устанавливаем позиции делений на оси x
	ax.set_xticks(x)

	# Устанавливаем подписи для оси x
	ax.set_xticklabels(x_labels)

	# Добавляем подписи к осям
	ax.set_xlabel('X')
	ax.set_ylabel('Y')

	#Рассчитываем среднее значение
	mean = np.mean(data)
	ax.axhline(mean, color='r', linestyle='dashed', linewidth=2)

	# Создаем виджет Canvas
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.draw()
	canvas.get_tk_widget().pack()




# Подключаемся к базе данных и создаём таблицы
database = DB('cars.db')
database.create_table()


# Создаем основное окно
root = tk.Tk()
root.title("Autopark")

# Создаем рамки для левой и правой панелей
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)

# Создаем 5 поля ввода и кнопку на левой панели
label_1 = tk.Label(left_frame, text="Driver name:")
driver_name_inp = tk.Entry(left_frame)
label_2 = tk.Label(left_frame, text="Distance (in km):")
distance_inp = tk.Entry(left_frame)
label_3 = tk.Label(left_frame, text="Brand of car:")
car_brand_inp = tk.Entry(left_frame)
label_4 = tk.Label(left_frame, text="Fuel consumption:")
fuel_cons_inp = tk.Entry(left_frame)
button = tk.Button(left_frame, text="Save in database", command=add_in_database)
out = tk.Label(left_frame)



# Размещаем виджеты на левой панели
label_1.grid(row=0, column=0)
driver_name_inp.grid(row=0, column=1)
label_2.grid(row=1, column=0)
distance_inp.grid(row=1, column=1)
label_3.grid(row=2, column=0)
car_brand_inp.grid(row=2, column=1)
label_4.grid(row=3, column=0)
fuel_cons_inp.grid(row=3, column=1)
button.grid(row=4, column=1)
out.grid(row=5, column=0)


# Создаем 2 поля ввода, 2 кнопки и поле вывода на правой панели
label_6 = tk.Label(right_frame, text="Owner name:")
owner_name_inp = tk.Entry(right_frame)
button_get_cars = tk.Button(right_frame, text="Search cars", command=show_cars)
searched_cars = tk.Label(right_frame)


label_7 = tk.Label(right_frame, text="Car in autopark:")
car_inp = tk.Entry(right_frame)
button_get_owners = tk.Button(right_frame, text="Search owners", command=show_owners)
searched_owners = tk.Label(right_frame)

button_1 = tk.Button(right_frame, text="View kilometers graphic", command=graph_drivers)
button_2 = tk.Button(right_frame, text="View fuel consumption graphic", command=graph_cars)

# Размещаем виджеты на правой панели
label_6.grid(row=0, column=0)
owner_name_inp.grid(row=0, column=1)
button_get_cars.grid(row=1, column=0)
searched_cars.grid(row=1, column=1)

label_7.grid(row=2, column=0)
car_inp.grid(row=2, column=1)
button_get_owners.grid(row=3, column=0)
searched_owners.grid(row=3, column=1)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)


# Размещаем левую и правую панели на основном окне
left_frame.pack(side=tk.LEFT, padx=10)
right_frame.pack(side=tk.LEFT, padx=10)

# Запускаем цикл событий
root.mainloop()