https://replit.com/join/jfwfqqznun-valeriadomingu5 
grasa = int(input("Ingresa cantidad de grasa (gr): "))
azucar = int(input("Ingresa cantidad de azucar (gr): "))
sodio = int(input("Ingresa cantidad de sodio (mg): "))

if grasa <= 5 and azucar <= 10:
    print("El alimento es bajo en grasa y azúcar")
elif sodio <= 100:
    print("El alimento es bajo en sodio.")
else:
    print("El alimento tiene advertencias nutricionales.") 
