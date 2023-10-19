nombre = str(input("Hola, cuál es tu nombre?"))
print("bienvenida a la cafetería de Ana", nombre)
t = int(input("Cuál es la temperatura actual: "))
h = float(input("Hora del día en fomra 24h (ejemplo: 7.00, 14.00, 22.00): "))
b = str(input("café a), té b), chocolate caliente c): "))

if t < 50:
  print("Debe eperar a que se caliente la bebida")
elif 50<t<70:
  print("Se puede servir de inmediato")
elif t > 70:
  print("Bebida muy caliente, debe esperar a que se enfríe")

if 6.00< h < 11.00:
  print("Las bebidas calientes se sirven más rápido")
else:
  print("Espera el turno")

if b == "a" or "b" and 7.00 < h < 9.00:
  print("Te recomendamos una bebida caliente")
elif b == "b" or "c" and 12.00 < h <14.00:
  print("Te recomendamos una bebida fría")
