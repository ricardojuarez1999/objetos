from radio import Radio
seguir = True
radio = Radio("pionner")
while seguir:
	if not radio.encendido:
		print ("""
	1. encender radio
	2. salir
			""")
		resp = int(input("ingrese su opcion: "))
	if resp == 1:
		radio.encender()
		print("""
	1.apagar el radio
	2.am/fm
	3.subir emisora
	4.bajar emisora
	5.subir volimen
	6.bajar volumen
	7.salir
		""")
		resp2 = int(input("ingrese su opcion: "))
		if resp2 == 1:
			radio.apagar()
		elif resp2 == 2:
			radio.cambiar_emisora()
		elif resp2 == 3:
			radio.subir_estacion()
		elif resp2 == 4:
			radio.bajar_estacion()
		elif resp2 == 5:
			radio.subir_volumen()
		elif resp2 == 6:
			radio.bajar_volumen()
		else:
			seguir = False
	elif resp == 2:
		seguir = False
	else:
		seguir = False
		print("su opcion no es valida, intente mas tarde")
	print (radio)