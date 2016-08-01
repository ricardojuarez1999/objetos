import radio
resp = 0
while resp !=7:
	rad = radio.radio()
	print (rad)
	print("""
	1.encender el radio
	2.am/fm
	3.emisora, subir
	4.emisora, bajar
	5.subir volimen
	6.bajar volumen
	7.salir
	""")
	resp = int(input("ingrese su opcion: "))
