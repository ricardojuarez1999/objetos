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
		if self.emisoraa_am > 1300:
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
			self.emisora_fm = 107.0.0