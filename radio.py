class Radio():
	def __init__(self, marca):
		self.marca = marca
		self.encendido = False
		self.en_am = False
		self.emisora_am = 300
		self.emisora_fm = 87.0
		self.volumen = 0
	def encender(self):
		self.encendido = True
	def apagar(Self):
		self.encendido = False
	def subir_volumen(self):
		if self.volumen>=100:
			self.volumen = 100
		else:
			self.volumen += 5
	def bajar_volumen(self):
		if self.volumen<=0:
			self.volumen = 0
		else:
			self.volumen -= 5
	def subir_estacion(self):
		if self.en_am == True:
			self.emisora_am += 40
		else:
			self.emisora_fm += 0.5
		if self.emisora_am > 1300:
			self.emisora_am = 300
		elif self.emisora_fm > 107.0:
			self.emisora_fm = 87.0
	def bajar_estacion(self):
		if self.en_am == True:
			self.emisora_am -= 40
		else:
			self.emisora_fm -= 0.5
		if self.emisora_am < 300:
			self.emisora_am = 1300
		elif self.emisora_fm < 87.0:
			self.emisora_fm = 107.0
	def cambiar_emisora(self):
		self.en_am = not self.en_am

	def __str__(self):
		resultado = ""
		resultado += "Encendido: " + str(self.encendido)
		resultado += "\nam/fm: " + str(self.en_am)
		resultado += "\nemisora am: " + str(self.emisora_am)
		resultado += "\nemisora fm: " + str(self.emisora_fm)
		resultado += "\nvolumen: " + str(self.volumen)
		return resultado