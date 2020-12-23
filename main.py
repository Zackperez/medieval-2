
class Personaje():

	def __init__ (self, vida, armadura):
		self.vida = vida
		self.armadura = armadura

class Eleven(Personaje):

	def __init__(self, nombre, vida, armadura, habilidad):
		super().__init__(self, armadura)
		self.nombre = nombre
		self.vida = vida
		self.armadura = armadura
		self.habilidad = habilidad

	def info(self):
		informacion = "nombre:",self.nombre,"armadura:",self.armadura,"vida:",self.vida,"Rol:",self.habilidad
		return print(informacion)

	def ataque(self):
		import random
		frases = ["Golpe crítico", "Brutal", "Criticazo", "Buen golpe"]
		ataque = random.randint(13,20)
		frase_random = random.choice(frases)
		if ataque > 16:
			daño_total = print("Daño:",str(ataque),"¡"+frase_random+"!")
			return daño_total
		else:
			daño_total = print("Daño:",str(ataque))
			return daño_total

class Urbus(Personaje):

	def __init__(self, nombre, vida, armadura, habilidad):
		super().__init__(self, armadura)
		self.nombre = nombre
		self.vida = vida
		self.armadura = armadura
		self.habilidad = habilidad

	def info(self):
		informacion = "nombre:",self.nombre,"armadura:",self.armadura,"vida:",self.vida,"Rol:",self.habilidad
		return print(informacion)

eleven = Eleven("Jose", 100, 0,"Guerrero")

#eleven.info()
