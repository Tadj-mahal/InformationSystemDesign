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
		self.cursor = self.connection.cursor()

	'''
	def emp_exists(self, employ_id):

		# Checking availability of user in db

		result = self.cursor.execute("SELECT 'id' FROM 'employees' WHERE 'employ_id' = ?", (employ_id, ))
		return bool(len(result.fetchall()))
	'''

	def get_emp_id(self, user_id):
		'''
		Get data about employeer from db with id helps
		'''
		self.cursor.execute('SELECT * FROM employees')
		result = self.cursor.fetchall()
		# print(user_id,  self.cursor.fetchall())
		return result

	'''
	def add_emp_and_sal(self, employ_id, salary):

		# Adding employeer to database

		self.cursor.execute("INSERT INTO 'employees' ('employ_id', 'salary') VALUES (?, ?)", (employ_id, salary, ))
		return self.connection.commit()
	'''

	def close(self):
		'''
		Closing connection with database
		'''
		self.connection.close()