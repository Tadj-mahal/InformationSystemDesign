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
				"""CREATE TABLE IF NOT EXISTS cars(
					id serial PRIMARY KEY,
					brand varchar(50) NOT NULL,
					fuel_consumption int NOT NULL);"""
			)
		self.cursor.execute(
				"""CREATE TABLE IF NOT EXISTS drivers(
					id serial PRIMARY KEY,
					name varchar(50) NOT NULL UNIQUE,
					kilometers int NOT NULL);"""
		)
		self.cursor.execute(
				"""CREATE TABLE IF NOT EXISTS cars_drivers(
					car_id int REFERENCES cars(id),
					driver_id int REFERENCES drivers(id),
					CONSTRAINT cars_drivers_pk PRIMARY KEY (car_id, driver_id));"""
		)
		print("[INFO] Tables created successfully")

	def add_new_driver(self, name, kilometers, brand_auto, fuel_consumption):

		# Checking the existence of car
		self.cursor.execute("SELECT id FROM cars WHERE brand = %s", (brand_auto, ))
		search_result = self.cursor.fetchall()
		message = ""
		if bool(len(search_result)) == 0:
			self.cursor.execute("INSERT INTO cars (brand, fuel_consumption) VALUES (%s, %s)", (brand_auto, fuel_consumption, ))
		else:
			message += "[INFO] Car was already added.\n"
		
		self.cursor.execute("SELECT id FROM drivers WHERE name = %s", (name, ))
		search_result = self.cursor.fetchall()
		if bool(len(search_result)) == 0:
			self.cursor.execute("INSERT INTO drivers (name, kilometers) VALUES (%s, %s)", (name, kilometers, ))
		else:
			message += "[INFO] Driver was already added.\n"
		
		# Get car and driver IDs to make connection many to many
		
		self.cursor.execute("SELECT id FROM cars WHERE brand = %s", (brand_auto, ))
		car_id = self.cursor.fetchall()
		self.cursor.execute("SELECT id FROM drivers WHERE name = %s", (name, ))
		driver_id = self.cursor.fetchall()

		print(car_id[0][0], driver_id[0][0])
		self.cursor.execute("INSERT INTO cars_drivers (car_id, driver_id) VALUES (%s, %s)", (car_id[0][0], driver_id[0][0], ))
		message += "[INFO] Successfully added elements in tables.\n"
		return message

	def search_by_auto(self, brand_auto):

		self.cursor.execute("SELECT id FROM cars WHERE brand = %s", (brand_auto, ))
		car_id = self.cursor.fetchall()
		owners = ""
		if bool(len(car_id)):
			self.cursor.execute("SELECT driver_id FROM cars_drivers WHERE car_id = %s", (car_id[0], ))
			owners_ids = self.cursor.fetchall()
			for i in range(len(owners_ids)):
				owner_id = int(owners_ids[i][0])
				self.cursor.execute("SELECT name FROM drivers WHERE id = %s", (owner_id, ))
				owner = self.cursor.fetchall()
				owners += str(owner[0][0]) + "\n"

		else:
			owners += "[404] Owners not found or no such car"  
		# make output by name of car owners
		return owners

	def search_by_owners(self, name):

		self.cursor.execute("SELECT id FROM drivers WHERE name = %s", (name, ))
		driver_id = self.cursor.fetchall()
		cars = ""
		if bool(len(driver_id)):
			self.cursor.execute("SELECT car_id FROM cars_drivers WHERE driver_id = %s", (driver_id[0], ))
			car_ids = self.cursor.fetchall()		
			for i in range(len(car_ids)):
				car_id = int(car_ids[i][0])
				self.cursor.execute("SELECT brand FROM cars WHERE id = %s", (car_id, ))
				car = self.cursor.fetchall()
				cars += str(car[0][0]) + "\n"
		else:
			cars += "[404] Cars not found or no such drivers" 

		# make output by brand of cars
		return cars


	def get_cars_data(self):
		self.cursor.execute("SELECT brand from cars")
		car_brands = self.cursor.fetchall()
		self.cursor.execute("SELECT fuel_consumption from cars")
		car_fuel_cons = self.cursor.fetchall()
		self.cursor.execute("SELECT id from cars")
		car_ids = self.cursor.fetchall()

		fuel_consumptions = []
		for i in range(len(car_ids)):
			self.cursor.execute("SELECT driver_id FROM cars_drivers WHERE car_id = %s", (str(car_ids[i][0])))
			driver_ids = self.cursor.fetchall()
			total_kilometers = 0
			for j in range(len(driver_ids)):
				self.cursor.execute("SELECT kilometers FROM drivers WHERE id = %s", (str(driver_ids[j][0])))
				kilometers = self.cursor.fetchone()
				total_kilometers += int(kilometers[0])
			fuel_consump = car_fuel_cons[i][0]
			car_brand = car_brands[i][0]
			# total_fuel_consumption = total_kilometrs * fuel_cosumption/100, because expence is calculated of liters/100km
			fuel_consumptions.append([car_brand, total_kilometers*fuel_consump/100])
		return fuel_consumptions

	def get_drivers_data(self):
		self.cursor.execute("SELECT name FROM drivers")
		driver_names = self.cursor.fetchall()
		self.cursor.execute("SELECT kilometers FROM drivers")
		distance = self.cursor.fetchall()
		self.cursor.execute("SELECT id FROM drivers")
		driver_ids = self.cursor.fetchall()
		
		distances = []
		for i in range(len(driver_ids)):
			self.cursor.execute("SELECT car_id FROM cars_drivers WHERE driver_id = %s", (str(driver_ids[i][0])))
			car_ids = self.cursor.fetchall()
			# total_distance = kilometers*cars_quantity
			distance_personal = len(car_ids) * distance[i][0]
			driver_name = driver_names[i][0]
			distances.append([driver_name, distance_personal])
		return distances