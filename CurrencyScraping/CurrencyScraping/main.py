# <tr data-currency-code="JPY" data-currency-name="Японская иена" data-test
# ="currency-table-row">
# <td>
# <div class="country-flag flag-jp"></div>
#                                         JPY
#                                 </td>
# <td>100</td>
# <td>
# <a href="/products/currency/jpy/">


#         Японская иена


#         </a>
# </td>
# <td>62.5513</td>
# <td class="color-green">
#                                         +1,0171
#                                 </td>
# </tr>]
import requests
from tkinter import *
from tkinter import ttk
import datetime
from bs4 import BeautifulSoup

def exchange_rates(cur):
	url = "https://www.banki.ru/products/currency/cb/"

	response = requests.get(url)
	soup = BeautifulSoup(response.content, "lxml")

	table = soup.find("table", {"class": "standard-table standard-table--row-highlight", "data-test": "currency-table"})

	exch_rates = [] #exchange rates
	curr_index = cur #currency indexes

	tr = table.find("tr", {"data-currency-code": curr_index})
	tr_course = tr.find_all("td")
	exch_rates.append([tr_course[0].text.replace('\t', '').replace('\n', ''), tr_course[2].text.replace('\t', '').replace('\n', ''), tr_course[3].text])

	return exch_rates

def show_exch_rate():
    cur = currency_combobox.get()
    ex_rate = exchange_rates(cur)

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    cur_index.config(text=f"Currency index: {ex_rate[0][0]}")
    cur_name.config(text=f"Currency name: {ex_rate[0][1]}")
    cur_rate.config(text=f"Current exchange rate: {ex_rate[0][2]} RUB")
    current_data.config(text=f"Current date and time: {formatted_datetime}")

# Create the main window
window = Tk()
window.title("EXCHANGE RATE")
window.geometry("250x150")
 
currency_label = ttk.Label(window, text="Choose index")
currency_label.pack()
currencies = ["USD", "EUR", "KZT", "AED", "GBP", "CZK", "JPY"]
currency_combobox = ttk.Combobox(values=currencies)
currency_combobox.pack(anchor="center", padx=6, pady=6)


update_button = ttk.Button(
    window, text="Get current rate", command=show_exch_rate)
update_button.pack()


# Create a label to display the weather condition
cur_index = ttk.Label(window, text="Currency index: ")
cur_index.pack()

# Create a label to display the temperature
cur_name = ttk.Label(window, text="Currency name: ")
cur_name.pack()


cur_rate = ttk.Label(window, text="Current exchange rate: ")
cur_rate.pack()


current_data = ttk.Label(window, text="Current date and time: ")
current_data.pack()

# Start the main event loop
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))
window.mainloop()