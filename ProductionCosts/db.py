import psycopg2
from config import host, user, password, db_name


class DB:

	def __init__(self, db_file):
		'''
		Intializing connection with db
		'''
		self.connection = psycopg2.connect(
			host=host,
			user=user,
			password=password,
			database=db_name
		)
		self.connection.autocommit = True
		self.cursor = self.connection.cursor()


	def create_table(self):
		self.cursor.execute(
				"""CREATE TABLE IF NOT EXISTS products(
					id serial PRIMARY KEY,
					name varchar(50) NOT NULL UNIQUE,
					quantity int NOT NULL,
					price int NOT NULL
					);"""
			)

		self.cursor.execute(
				"""CREATE TABLE IF NOT EXISTS costs(
					id serial PRIMARY KEY,
					month int NOT NULL CHECK
						(month>0 and month<13),
					costs int NOT NULL,
					product_id int REFERENCES products(id)
					);"""
			)# Издержки производства - costs
		print("[INFO] Tables created successfully")


	def add_new_product(self, name, quantity, price):
		self.cursor.execute("SELECT id FROM products WHERE name = %s", (name, ))
		search_result = self.cursor.fetchall()
		message = ""
		if bool(len(search_result)) == 0:
			self.cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price, ))
			self.cursor.execute("SELECT id FROM products WHERE name = %s", (name, ))
			product_id = self.cursor.fetchone()
			product_id = product_id[0]
			for i in range(12):
				# price*17%*month/10
				costs = 0.17 * price * (i + 1) / 10
				self.cursor.execute("INSERT INTO costs (month, costs, product_id) VALUES (%s, %s, %s)", (i + 1, costs, product_id,))
			message += "[INFO] Product successfully added"
		else:
			message += "[INFO] Product was already added."
		return message


	def search_by_name(self, name):
		self.cursor.execute("SELECT quantity, price FROM products WHERE name = %s", (name, ))
		search_result = self.cursor.fetchall()
		message = []
		if bool(len(search_result)) != 0:
			message.append([True, search_result])
		else:
			message.append([False, "[INFO] Product not found."])
		return message

	def costs_by_date(self, month):
		self.cursor.execute("SELECT product_id, costs FROM costs WHERE month = %s", (month, ))
		search_result = self.cursor.fetchall()
		products_costs = []
		for i in range(len(search_result)):
			self.cursor.execute("SELECT name FROM products WHERE id = %s", (search_result[i][0], ))
			search_result_name = self.cursor.fetchone()
			products_costs.append([search_result_name[0],search_result[i][1]])
		return products_costs
