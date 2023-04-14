numero1=float(input("digite o 1º numero:"))
numero2=float(input("digite o 2º numero:"))
numero3=float(input("digite o 3º numero:"))
numero4=float(input("digite o 4º numero:"))
numero5=float(input("digite o 5º numero:"))

if (numero1 >numero2 and numero1 > numero3 and numero1 > numero4 and numero1  >numero5):
	print("o maior número é o 1º", numero1)
if (numero2 >numero1 and numero2 > numero3 and numero2 > numero4 and numero2  >numero5):
	print("o maior número é o 2º", numero2)
if (numero3 >numero2 and numero3 > numero1 and numero3 > numero4 and numero3  >numero5):
	print("o maior número é o 3º", numero3)	
if (numero4 >numero2 and numero4 > numero3 and numero4 > numero1 and numero4  >numero5):
	print("o maior número é o 4º", numero4)	
elif(numero5 >numero2 and numero5 > numero3 and numero5 > numero1 and numero5  >numero4):
	print("o maior número é o 5º", numero5)