import sqlite3
import bcrypt 
from datetime import datetime

def showDate():
	date =  datetime.now().replace(microsecond=0)
	return date
#cores ANSI
vermelho = "\u001B[31m"
verde = "\u001B[32m"
amarelo = "\u001B[33m"
azul = "\u001B[34m"
magenta = "\u001B[35m"
cyan = "\u001B[36m"
bold = "\033[1;37m"
reseta = "\u001B[00m"

def log(msg):
	print(f"-- [{showDate()}] {msg}")
class DataBase:
	def __init__(self, db):
		self.db = db
		with sqlite3.connect(self.db) as self.conn:
			try:
				self.cursor = self.conn.cursor() #cria um cursor
				query = """
				CREATE TABLE IF NOT EXISTS users(
				id INTEGER  PRIMARY KEY AUTOINCREMENT, 
				username VARCHAR(255), 
				tel VARCHAR(255), 
				senha VARCHAR(255)
				);
				"""
				if self.cursor.execute(query):
						log(f"{verde} Tabela criada com sucesso ! {reseta}")
			except sqlite3.Error as e:
				log(f" {vermelho} Error : {e} {reseta} ")
			
		
	def  insert_data(self, username, tel, password):
		try:
			passwd = password.encode()
			salt = bcrypt.gensalt() #gera salts
			hash_passwd = bcrypt.hashpw(passwd, salt) #gera uma hash
			query = """
			INSERT INTO users(username, tel, senha) VALUES (?, ?, ?);
			"""
			params = (username, tel,hash_passwd,)
			self.cursor.execute(query, params)
			log(f" Usuário {bold} {username} {reseta} inserido com {verde} sucesso{reseta} !")
		except sqlite3.Error as e:
			log(f" {vermelho} Error : {e} {reseta} ")

	def select_from(self):
		try:
			query = "SELECT * FROM users"
			self.cursor.execute(query)
			data = self.cursor.fetchall()
			print(data)

		except sqlite3.Error as e:
			log(f" {vermelho} Error na consulta {query} : {e} {reseta} ")

	def closed(self):
			self.cursor.close()
			self.conn.close()
			
#teste 	
db = DataBase("mydb.db")
db.insert_data("Mateus", "82 10212-2121", "namdaw32")
db.select_from()
db.closed()




			
			
			
