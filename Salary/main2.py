from db import DB
import tkinter as tk
from tkinter import ttk

def mid_salary(data):
    sum_salary = 0
    for i in range(len(data)):
        sum_salary += data[i]["salary"]

    mid = sum_salary/len(data)
    return mid

def change_bgcolor():
    # Получаем id выбранного элемента
    item_id = ['I001', 'I002', 'I003', 'I004', 'I005', 'I006']

    print(item_id)
    # Получаем текущий цвет фона выбранного элемента
    for i in range(len(item_id)):
        current_salary = tree.item(item_id[i], 'values')
        print(tree.item(item_id[i]))
        print(current_salary[1])
    # Если цвет фона элемента белый, то меняем его на красный
        if int(current_salary[1]) == int(mid_salary(data)):
            tree.item(item_id[i], tag='bgmid')
            tree.tag_configure('bgmid', background='yellow')
        elif int(current_salary[1]) < int(mid_salary(data)):
            tree.item(item_id[i], tag='bglow')
            tree.tag_configure('bglow', background='red')
        else:
            tree.item(item_id[i], tag='bghigh')
            tree.tag_configure('bghigh', background='green')

def change_hgcolor():

    multiplicity = int(input_entry.get())
    item_id = ['I001', 'I002', 'I003', 'I004', 'I005', 'I006']
    for i in range(len(item_id)):
        
        tr_item = tree.item(item_id[i])
        cur_sal = tree.item(item_id[i], 'values')
        tree.tag_configure('bgmid', background='')
        tree.tag_configure('bghigh', background='')
        tree.tag_configure('bglow', background='')
        if(int(cur_sal[1]) % multiplicity == 0):
            tree.item(item_id[i], tag='fgnot')
            tree.tag_configure('fgnot', foreground='green')
        else:
            tree.item(item_id[i], tag='fg')
            tree.tag_configure('fg', foreground='red')


database = DB('employees.db')
cols = database.get_emp_id(0)
print(database.get_emp_id(0)[0][0])

root = tk.Tk()
root.title("Mein Anwendung")

# Создаем таблицу из трех столбцов

# Создаем Treeview с двумя столбцами
tree = ttk.Treeview(root, columns=("col1", "col2"))
tree.pack(side=tk.LEFT)

# Добавляем заголовки для каждого столбца
tree.heading("#0", text="ID")
tree.heading("col1", text="Name")
tree.heading("col2", text="Salary")

# Добавляем данные в таблицу
data = [
    {"id": cols[0][0], "name": cols[0][1], "salary": cols[0][2]},
    {"id": cols[1][0], "name": cols[1][1], "salary": cols[1][2]},
    {"id": cols[2][0], "name": cols[2][1], "salary": cols[2][2]},
    {"id": cols[3][0], "name": cols[3][1], "salary": cols[3][2]},
    {"id": cols[4][0], "name": cols[4][1], "salary": cols[4][2]},
    {"id": cols[5][0], "name": cols[5][1], "salary": cols[5][2]},
]

for item in data:
    print(item["salary"])
    tree.insert("", "end", text=item["id"], values=(item["name"], item["salary"]))




# Создаем поле для ввода и две кнопки
input_frame = tk.Frame(root)
input_frame.pack(side=tk.RIGHT)

input_label = tk.Label(input_frame, text="Input multiplicity")
input_label.pack()

input_entry = tk.Entry(input_frame)
input_entry.pack()

hl_button = tk.Button(input_frame, text="salary division", command=change_hgcolor) #higlight
hl_button.pack()

bg_button = tk.Button(input_frame, text="salary level", command=change_bgcolor)
bg_button.pack()



root.mainloop()

# def get_information():
	
# 	for i in range(6):
		


# get_information()
