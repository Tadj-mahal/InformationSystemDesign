from db import DB
import tkinter as tk


def add_in_database():
    name = e_name.get()
    quantity = int(e_quantity.get())
    price = int(e_price.get())
    msg = database.add_new_product(name, quantity, price)
    label.config(text=f"{msg}")


def search_by_name():
    name = e_search.get()
    msg = database.search_by_name(name)
    if msg[0][0]:
        data = msg[0][1]
        print(data)
        price = data[0][0]
        quantity = data[0][1]
        label_search.config(text=f"Name: {name}\nPrice: {price}\nQuantity: {quantity}")
    else:
        label_search.config(text=f"{msg[0][1]}")


def costs():
    # Проверка на корректное введение месяца
    months = [['1', 'january', 'jan', 'январь', 'янв'], ['2', 'february', 'feb', 'февраль', 'фев'], ['3', 'march', 'mar', 'март', 'мар'], ['4', 'april', 'apr', 'апрель', 'апр'], ['5', 'may', 'май'], ['6', 'june', 'jun', 'июнь', 'июн'], [
    '7', 'july', 'jul', 'июль', 'июл'], ['8', 'august', 'aug', 'август', 'авг'], ['9', 'september', 'sep', 'сентябрь', 'сен'], ['10', 'october', 'oct', 'октябрь', 'окт'], ['11', 'november', 'nov', 'ноябрь', 'ноя'], ['12', 'december', 'dec', 'декабрь', 'дек']]
    month = e_costs.get()
    checker = False
    for i in range(12):
    	if month in months[i]:
    		checker = True
    		month = i+1
    		month_str = months[i][1]
    		break
    print(month, checker)	
    if checker:
    	msg = database.costs_by_date(month)
    	msg_re = ''
    	for i in range(len(msg)):
    		msg_re += 'name: ' + str(msg[i][0]) + '  ' + 'costs: ' + str(msg[i][1]) + '$\n' 
    	output.config(text=f"Costs in {month_str}: \n{msg_re}")
    else:
    	output.config(text=f"[ERROR] Month was input not correctly.\nFix mistake and try again.")


# Подключаемся к базе данных и создаём таблицы
database = DB('production.db')
database.create_table()

# Создаем основное окно
root = tk.Tk()
root.title("Production")

# Создаем рамки для левой и правой панелей
left_frame_top = tk.Frame(root)
left_frame_bottom = tk.Frame(root)
right_frame = tk.Frame(root)

# Создаем 5 поля ввода и кнопку на левой верхней панели
l_name = tk.Label(left_frame_top, text="Name:")
e_name = tk.Entry(left_frame_top)
l_quantity = tk.Label(left_frame_top, text="Quantity:")
e_quantity = tk.Entry(left_frame_top)
l_price = tk.Label(left_frame_top, text="Price:")
e_price = tk.Entry(left_frame_top)
add_product = tk.Button(
    left_frame_top, text="Add in database", command=add_in_database)
label = tk.Label(left_frame_top)

# Размещаем виджеты на левой верхней панели
l_name.grid(row=0, column=0)
e_name.grid(row=0, column=1)
l_quantity.grid(row=1, column=0)
e_quantity.grid(row=1, column=1)
l_price.grid(row=2, column=0)
e_price.grid(row=2, column=1)
add_product.grid(row=3, column=1)
label.grid(row=5, column=0)

# Создаем поле ввода и кнопку на левой нижней панели
l_search = tk.Label(left_frame_bottom, text="Search product:")
e_search = tk.Entry(left_frame_bottom)
search = tk.Button(left_frame_bottom, text="Search", command=search_by_name)
label_search = tk.Label(left_frame_bottom)

# Размещаем виджеты на левой нижней панели
l_search.grid(row=0, column=0)
e_search.grid(row=0, column=1)
search.grid(row=1, column=1)
label_search.grid(row=2, column=0)

# Создаем поле ввода, кнопку и текстовое поле на правой панели
l_costs = tk.Label(right_frame, text="Month:")
e_costs = tk.Entry(right_frame)
costs = tk.Button(right_frame, text="Show costs", command=costs)
output = tk.Label(right_frame)

# Размещаем виджеты на правой панели
l_costs.grid(row=0, column=0)
e_costs.grid(row=0, column=1)
costs.grid(row=1, column=1)
output.grid(row=2, column=0, columnspan=2)

# Размещаем рамки на основном окне
left_frame_top.grid(row=0, column=0, padx=5, pady=5)
left_frame_bottom.grid(row=1, column=0, padx=5, pady=5)
right_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

# Запускаем главный цикл обработки событий
root.mainloop()
